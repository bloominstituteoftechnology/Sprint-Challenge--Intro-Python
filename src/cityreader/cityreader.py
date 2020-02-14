# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

import csv
import re


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f"City: {self.name}\nCoordinates({self.lat,self.lon})"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):

    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list

    with open('/Users/mr.ball/Documents/coding/lambda/python/python-intro/Sprint-Challenge--Intro-Python-1/src/cityreader/cities.csv', 'rt') as f:
        data = csv.reader(f)
        line_count = 0
        for row in data:
            if line_count > 0:
                cities.append(City(row[0], float(row[3]), float(row[4])))
            line_count += 1

        return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
#     print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
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

# TODO Get latitude and longitude values from the user


def range_check(val1, val2):
    if val1 < val2:
        return [val1, val2]
    else:
        return [val2, val1]


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
        # within will hold the cities that fall within the specified region
    lat_range = range_check(lat1, lat2)
    lon_range = range_check(lon1, lon2)

    print(lat_range, lon_range)

    within = [i for i in cities if i.lat >
              lat_range[0] and i.lat < lat_range[1] and i.lon > lon_range[0] and i.lon < lon_range[1]]

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    return within


def handleInput(coords1, coords2):
    concat = f"{coords1},{coords2}"
    return [float(x.strip()) for x in concat.split(',')]


coords1 = input(
    "Enter first Coordinates Seperated by comma. Example 1111,2222:\n\n>>>> ")

coords2 = input(
    "Enter second Coordinates Seperated by comma. Example 1111,2222:\n\n>>>> ")

coordsArr = handleInput(coords1, coords2)

print(cityreader_stretch(
    coordsArr[0], coordsArr[1], coordsArr[2], coordsArr[3], cities))
