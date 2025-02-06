"""
Class to manage alerts when the bus's assigned route does not match the
physical route it is taking by comparing its current location with the planned
route path.
"""

import datetime
import os
import threading

from loguru import logger
from pyproj import Transformer  # type: ignore
from shapely.geometry import MultiLineString, Point, shape  # type: ignore

from its_system_alerts.system.alerts.alert_tracker import AlertTracker


class PathRouterChecker(AlertTracker):
    """
    Init class
    """

    def __init__(self, company_id: int, route_list: list, buffer_distance_meters: int = 10):
        """
        Init class with route list and batch positions

        Args:
            route_list: List of dictionaries with the route path (GeoJSON format)
            buffer_distance_meters: Buffer distance in meters to compare the bus position with the route path (default 10)

        Returns:
            None
            Instance of the class with:
                - route_buffers: Dictionary with the route ITS code as key and the buffer as value
        """

        # WGS84 (EPSG:4326) to UTM 18N (EPSG:32618) in order to use meters in the next buffer
        self.transformer_to_32618 = Transformer.from_crs("EPSG:4326", "EPSG:32618", always_xy=True)
        self.company_id = company_id

        # iterate over the route list and transform the coordinates to UTM 18N
        self.route_buffers = {}
        for route in route_list:
            geojson_geom = route["geometry_path"]["features"][0]["geometry"]
            buffer_utm = self._create_buffer(
                geojson_geom, buffer_distance_meters, transformer_to_utm=self.transformer_to_32618
            )
            route_its_code = route["its"]
            route_tako_id = route["id"]
            self.route_buffers[f"{route_its_code}_{route_tako_id}"] = buffer_utm

        logger.info(f"Created {len(self.route_buffers)} route buffers")

    @staticmethod
    def _create_buffer(geojson_geometry, buffer_meters, transformer_to_utm):
        """
        Convierte GeoJSON a MultiLineString, reproyecta a UTM 18N y crea buffer.

        Args:
            geojson_geometry (dict): Geometría en formato GeoJSON (MultiLineString)
            buffer_meters (int): Radio del buffer en metros

        Returns:
            Shapely Polygon: Buffer de la ruta en EPSG:32618
        """
        # Convertir GeoJSON a Shapely MultiLineString al ser rutas
        geom = shape(geojson_geometry)

        # reproyectar coordenadas
        def reproject(coords):
            return [transformer_to_utm.transform(lon, lat) for lon, lat, *_ in coords]

        # Reprojectar todas las líneas
        utm_lines = []
        if geom.geom_type == "MultiLineString":
            for line in geom.geoms:
                utm_line = reproject(line.coords)
                utm_lines.append(utm_line)
        elif geom.geom_type == "LineString":
            utm_lines.append(reproject(geom.coords))

        # Crear nuevo MultiLineString en UTM
        utm_geom = MultiLineString(utm_lines)

        # Crear buffer (en metros, por estar en UTM)
        return utm_geom.buffer(buffer_meters)

    def send_whatsapp_notification(self, message: str):
        raise NotImplementedError

    def send_email_notification(self, message: str):
        raise NotImplementedError

    def process_alert(self, data: list):  # type: ignore
        """
        Check if the bus router matches with its physical location

        Args:
            data -> batch_positions (list): List with the bus positions to check
            [{ "idVehiculo": "bus_1", "latitud": 4.123, "longitud": -74.123, "idRuta": "route_1" }, ...]

        Returns:
            list: List with the bus positions that with a flag indicating if the bus is on the route.
            Adding on_route key True or False
            [{ "idVehiculo": "bus_1", "latitud": 4.123, "longitud": -74.123, "idRuta": "route_1", "on_route": True }, ...]
        """
        for bus_position in data:
            route_id = bus_position["idRuta"]

            possible_routes = {key: value for key, value in self.route_buffers.items() if key.startswith(route_id)}

            if not possible_routes:
                bus_position["on_route"] = False
                bus_position["found_route"] = False
            else:
                latitude = bus_position["localizacionVehiculo"]["latitud"]
                longitude = bus_position["localizacionVehiculo"]["longitud"]

                x_utm, y_utm = self.transformer_to_32618.transform(longitude, latitude)
                bus_point = Point(x_utm, y_utm)

                bus_position["on_route"] = False
                for route_buffer in possible_routes.values():
                    if bus_point.within(route_buffer):
                        bus_position["on_route"] = True
                        break

                bus_position["found_route"] = True

        return self.post_alerts_into_database(data)

    def post_alerts_into_database(self, data: list) -> list:
        """
        Post alerts into the database
        Only we need to save the alerts that are not on the route, "on_route" = False and "found_route" = True

        This method makes the filter and post the alerts into the database

        Args:
            data (list): List with the bus positions to check
            [{ "idVehiculo": "bus_1", "latitud": 4.123, "longitud": -74.123, "idRuta": "route_1", "on_route": True }, ...]

        Returns:
            list: List with the bus positions that are not on the route
            [{ "idVehiculo": "bus_1", "latitud": 4.123, "longitud": -74.123, "idRuta": "route_1", "on_route": True }, ...]
        """
        data_to_save = [
            bus_position for bus_position in data if not bus_position["on_route"] and bus_position["found_route"]
        ]

        url_post = os.getenv("URL_POST_ALERT", "")
        url_login = os.getenv("URL_LOGIN_TAKO", "")
        token_tako = self.login_tako(url_login=url_login)

        for dt in data_to_save:
            timestamp = dt["fechaHoraLecturaDato"]
            date = datetime.datetime.strptime(timestamp, "%d/%m/%Y %H:%M:%S.%f")
            formatted_timestamp = date.strftime("%Y-%m-%d %H:%M:%S.%f")

            alert = {
                "vehicle": dt["idVehiculo"],
                "longitud": dt["localizacionVehiculo"]["longitud"],
                "latitud": dt["localizacionVehiculo"]["latitud"],
                "last_reported_time": formatted_timestamp,
                "total_events": 1,
                "id_alert_type": 5,
                "send_whatsapp": False,
                "send_email": False,
                "company_id": self.company_id,
                "reported_its_route": dt["idRuta"],
            }

            # I'm not complete sure about how many alerts will receive the system, so I decided to use threads
            thread = threading.Thread(target=self.save_to_postgres, args=(url_post, url_login, alert, token_tako))
            thread.start()

        logger.info(f"Posted {len(data_to_save)} alerts")
        return data_to_save
