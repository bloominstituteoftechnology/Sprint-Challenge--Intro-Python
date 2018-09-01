import csv
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.


class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

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

with open('cities.csv') as f:
    reader = csv.reader(f)
    next(reader)  # skips the first row
    for row in reader:
        cities.append(row)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    #      city  lat   lon
    print((c[0], c[3], c[4]))

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
# lat is n/s; lon is e/w
firstCorner = input("Enter lat1, lon1: ")
secondCorner = input("Enter lat2, lon2: ")
lat1 = tuple(map(float, firstCorner.split(',')))
lat2 = tuple(map(float, secondCorner.split(',')))
# normalize for top of rectangle
if lat1[0] > lat2[0]:
    top = lat1[0]
    bottom = lat2[0]
else:
    top = lat2[0]
    bottom = lat1[0]

# normalize for left of rectangle
if lat1[1] < lat2[1]:
    left = lat1[1]
    right = lat2[1]
else:
    left = lat2[1]
    right = lat1[1]

citiesContained = []
for c in cities:
    if float(c[3]) > bottom and float(c[3]) < top:
        if float(c[4]) > left and float(c[4]) < right:
            citiesContained.append(f'{c[0]}: ({c[3]},{c[4]})')

for c in citiesContained:
    print(c)
