import csv

class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

arr = []


with open('cities.csv', newline ='') as csvfile:
    c = csv.reader(csvfile)
    for row in c:
        arr.append(row)

arr.pop(0)


cities = [City(city[0], city[3], city[4]) for city in arr]

# TODO

for city in cities:
    print(city.name, city.lat, city.lon)
# TODO

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

# TODO