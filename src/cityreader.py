import math
import numpy

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

class City:
    def __init__(self, name, state, county, latitude, longitude, population, density, timezone, zips):
        self.name = name
        self.state = state
        self.county = county 
        self.latitude = latitude
        self.longitude = longitude
        self.population = population
        self.density = density
        self.timezone = timezone
        self.zips = zips
        pass

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

import csv
with open('cities.csv') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')
    csv_read.next() # exclude first row
    for row in csv_read:
        cities.append(City(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))


# Print the list of cities (name, lat, lon), 1 record per line.

# for city in cities:
#     print(city.name, city.latitude, city.longitude) 

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

print('We will now attempt to find all the cities within a rectangular area defined by two sets of coordinates:')
print()
print('Please input a pair of coordinates: ')
lat1 = int(input('- latitude: '))
lon1 = int(input('- longitude: '))

print('Please input a pair of coordinates: ')
lat2 = int(input('- latitude: '))
lon2 = int(input('- longitude: '))

# if 3 in numpy.arange(math.floor(min(lat1, lat2)), math.ceil(max(lat1, lat2))):
#     print('pass')

for city in cities:
    if int(float(city.latitude)) in numpy.arange(math.floor(min(lat1, lat2)), math.ceil(max(lat1, lat2))):
        if int(float(city.longitude)) in numpy.arange(math.floor(min(lon1, lon2)), math.ceil(max(lon1, lon2))):
            print(city.name + ': (' + city.latitude + ',' + city.longitude +')') 

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

# 