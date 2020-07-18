# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City(object):
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self. lon = lon


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

import os # importing for platform agnostic filepath building
import csv # needed for csvs


def cityreader(cities=[]):
    '''
    Reads from cites.csv and creates a list of of city instances from the file
    '''

    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cities.csv')
    
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        first = True
        for row in csv_reader:
            if first:
                first = False
            else:
                cities.append(City(row[0], float(row[3]), float(row[4])))
    csv_file.close()

    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

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


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    #normalizing inputs, a1, b1 are upper right, and a2, b2 are lower right
    if lat1 > lat2:
        a1 = lat1
        a2 = lat2
    else:
        a1 = lat2
        a2 = lat1
    if lon1 > lon2:
        b1 = lon1
        b2 = lon2
    else:
        b1 = lon2
        b2 = lon1
    
    # Go through each city and check to see if it falls within 
    # the specified coordinates.

    for city in cities:
        if (city.lat <= a1) \
        and (city.lat >= a2) \
        and (city.lon <= b1) \
        and (city.lon >= b2):

            within.append(city)

    return within

while True:
    print('Please enter two corners to construct a latitude and longitude square.')
    in1 = input('Enter lat1, lon1:')
    in2 = input('Enter lat2, lon2:')
    try:
        lat1, lon1 = in1.split(', ')
        lat2, lon2 = in2.split(', ')
        lat1 = float(lat1)
        lon1 = float(lon1)
        lat2 = float(lat2)
        lon2 = float(lon2)

        break
    except:
        print('Incorrect input. Please enter latitude and longitude like the following:')
        print('Enter lat1, lon1: 45, -100')
        print('or')
        print('Enter lat2, lon2: 45.68, -99.45')

inside = cityreader_stretch(lat1, lon1, lat2, lon2, cities)

print('The following cities are within the specified square:')
for c in inside:
    print(f'{c.name}: ({c.lat}, {c.lon})')