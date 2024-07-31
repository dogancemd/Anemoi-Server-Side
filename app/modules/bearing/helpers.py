from geographiclib.geodesic import Geodesic


def get_bearing(point1, point2):
    lat1, long1 = point1
    lat2, long2 = point2
    brng = Geodesic.WGS84.Inverse(lat1, long1, lat2, long2)['azi1']
    brng = (brng + 360) % 360
    return brng