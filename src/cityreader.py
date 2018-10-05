# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
import csv

# TODO
class City():
    def __init__(self, name, latitude, longitude):
        self.name=name
        self.latitude=latitude
        self.longitude=longitude


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

f = open('cities.csv')
city_file = csv.reader(f)

citiesAll=[City(row[0], row[3], row[4]) for row in city_file]

cities=citiesAll[2:]



# TODO

# Print the list of cities (name, lat, lon), 1 record per line.
print('\nList of cities:')
for c in cities:
    print(f'name:{c.name},lat:{c.latitude},lon:{c.longitude}')
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

input1=input('\nEnter lat1, lon1 separated by comma:').split(",")
input2=input('\nEnter lat2, lon2 separated by comma:').split(",")


if len(input1) ==1 and len(input2)==1:
    print('\n input values should be separated by a comma')
else:
    lat=[int(input1[0]),int(input2[0])]
    lon=[int(input1[1]),int(input2[1])]

    lat.sort()
    lon.sort()

    result=[f'{c.name}: ({c.latitude}, {c.longitude})' for c in cities if float(c.latitude) > lat[0] and float(c.latitude) < lat[1] and float(c.longitude) > lon[0] and float(c.longitude) < lon[1]]

    for row in result:
        print(row)
