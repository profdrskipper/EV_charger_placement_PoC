import math


def haversine(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


map_dict = {
    'E1': (25.09511857, 55.15520035),
    'E2': (25.11112987, 55.19719364),
    'E3': (25.11322246990363, 55.19491389140763),
    'E4': (25.235698355149307, 55.32898092071243),
    'E5': (25.164757363987757, 55.22886110646065),
    'E6': (25.212285990761828, 55.260842282712616),
    'E7': (25.266877762775987, 55.3114781160367),
    'E8': (25.216613065884044, 55.362447010349534),
    'E9': (24.989075707062398, 55.09255818207395),
    'E10': (25.217101907919254, 55.40785530838673)
}

for key, val in map_dict.items():
    for i, j in map_dict.items():
        distance = haversine(val, j)
        print(key, distance, i)