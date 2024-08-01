from geographiclib.geodesic import Geodesic

locations = {
    "dcem": (39.891878, 32.783405),
    "niki": (47.4979, 19.0402)
}


def get_bearing(point1, point2):
    lat1, long1 = point1
    lat2, long2 = point2
    brng = Geodesic.WGS84.Inverse(lat1, long1, lat2, long2)['azi1']
    brng = (brng + 360) % 360
    return brng
