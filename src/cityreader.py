import csv
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.


class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "({}, {}, {})".format(self.name, self.latitude, self.longitude)

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
skipFirstLine = 0


def readCSV(file):
    global skipFirstLine
    reader = csv.reader(file)
    for row in reader:
        if skipFirstLine:
            cities.append(City(row[0], row[3], row[4]))
        skipFirstLine = 1


readCSV(open("cities.csv"))

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

print("")

choice1 = input("Enter lat1,lon1: ")
choice1 = choice1.split(',')
choice2 = input("Enter lat2,lon2: ")
choice2 = choice2.split(',')

lat1, lon1 = float(choice1[0]), float(choice1[1])
lat2, lon2 = float(choice2[0]), float(choice2[1])

if lat1 < lat2:  # switch if user entered other start corner
    lat1, lat2 = lat2, lat1
    lon1, lon2 = lon2, lon1

c = [city for city in cities if (lat1 > float(city.latitude) > lat2)
     and (lon1 > float(city.longitude) > lon2)]

print("")

for city in c:
    city = "{}: ({},{})".format(city.name, city.latitude, city.latitude)
    print(city)
