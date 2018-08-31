import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f"{self.name}: {self.lat} / {self.lon}"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# Use Python's built-in "csv" module to read this file so that each record is
# imported into a City instance. (You're free to add more attributes to the City
# class if you wish, but this is not necessary.) Google "python 3 csv" for
# references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

cities = []
with open("cities.csv", newline="") as csvfile:
    cityreader = csv.reader(csvfile)
    for row in list(cityreader)[1:]: # First line is cruft
        city = City(row[0], float(row[3]), float(row[4])) # Name, lat, lon from the data
        cities.append(city)

# Print the list of cities (name, lat, lon), 1 record per line.

[print(city) for city in cities]

# *** STRETCH GOAL! ***
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other (what is latMin, latMax?)
# then search for cities.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

points = [
    input("Input a lat/lon pair separated by a comma: "),
    input("Input a second lat/lon pair separated by a comma: ")
]

points = [[int(c) for c in point.split(",")] for point in points]
lats = [point[0] for point in points]
lons = [point[1] for point in points]

def city_in_bounds(city, points):
    if city.lat > max(lats) or city.lat < min(lats):
        return False
    if city.lon > max(lons) or city.lon < min(lons):
        return False

    return True

[print(city) for city in cities if city_in_bounds(city, points)]