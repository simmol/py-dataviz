import math


def haversine(lon1, lat1, lon2, lat2):
    # Convert coordinates to floats
    lon1, lat1, lon2, lat2 = [float(lon1), float(lat1), float(lon2), float(lat2)]

    # Convert to radians from degrees.
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # Compute distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    km = 6367 * c

    return km


def calc_dist(row, airports):
    dist = 0

    try:
        # Match source and destination get coordinates
        source = airports[airports["id"].isin([row["source_id"]])].iloc[0]
        dest = airports[airports["id"].isin([row["dest_id"]])].iloc[0]

        # Use coordinates to compute distance
        dist = haversine(dest["longtitude"], dest["latitude"], source["latitude"], source["longtitude"])
    except (ValueError, IndexError):
        pass

    return dist
