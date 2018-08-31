# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
import csv


class City():
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

# TODO


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
with open('./src/cities.csv', newline='') as csvfile:
    file_content = csv.reader(csvfile)
    for item in file_content:
        cities.append(City(item[0], item[3], item[4]))
cities.pop(0)


# TODO

# Print the list of cities (name, lat, lon), 1 record per line.
for city in cities:
    print(city.name, city.latitude, city.longitude)

endpoints = input('Enter Lat1, Lon1: ')
endpoints2 = input('Enter Lat2, Lon2: ')
new_endpoints = endpoints.split(', ')
new_endpoints2 = endpoints2.split(', ')

print(type(float(city.latitude)))
"""range(min(int(new_endpoints[0]), int(new_endpoints2[0])), max(int(new_endpoints[0]), int(new_endpoints2[0]))) and city.longitude in range(min(int(new_endpoints[1]), int(new_endpoints2[1])), max(int(new_endpoints[1]), int(new_endpoints2[1])))"""

for city in cities:
    # >= min(35, 45):
    if float(city.latitude) >= min(int(new_endpoints[0]), int(new_endpoints2[0])) and float(city.latitude) <= max(int(new_endpoints[0]), int(new_endpoints2[0])) and float(city.longitude) >= min(int(new_endpoints[1]), int(new_endpoints2[1])) and float(city.longitude) <= max(int(new_endpoints[1]), int(new_endpoints2[1])):
        print(city.name, (float(city.latitude), float(city.longitude)))


# TODO

# *** STRETCH GOAL! ***
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
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
