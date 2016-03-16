import pandas

# Read in the airports data
airports = pandas.read_csv("data/airports.dat", header=None, dtype=str)
airports.columns = [
    "id", "name", "city", "country", "code", "icao", "latitude",
    "longtitude", "altitude", "offset", "dst", "timezone"
]

# Read in the airlines data
airlines = pandas.read_csv("data/airlines.dat", header=None, dtype=str)
airlines.columns = [
    "id", "name", "alias", "iata", "icao", "callsign", "country", "active"
]

# Read in the routes data
routes = pandas.read_csv("data/routes.dat", header=None, dtype=str)
routes.columns = [
    "airline", "airline_id", "source", "source_id", "dest", "dest_id",
    "codeshare", "stops", "equipment"
]

routes = routes[routes["airline_id"] != "\\N"]

if __name__ == "__main__":
    tmp = routes.head()
    print(tmp)
