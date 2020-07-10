# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
    """ A class that holds information about a City """
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    
    def __str__(self):
        """ prints the name, lat, and lon """
        return f"City: {self.name} ({self.lat}, {self.lon})"

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

import csv

cities = []

def cityreader(cities=[]):
    # For each city record, create a new City instance and add it to the 
    # `cities` list
    with open('cities.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # not used, just get the row out of the way

        for row in csvreader:
            cities.append(City(name=row[0], 
                               lat=float(row[3]), 
                               lon=float(row[4])))
    
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

# Get latitude and longitude values from the user
print("------------------")
point1 = input("Enter lat1, lon1: ").split(",")
point1 = (float(point1[0]), float(point1[1]))

point2 = input("Enter lat2, lon2: ").split(",")
point2 = (float(point2[0]), float(point2[1]))

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # Ensure that the lat and lon valuse are all floats
    lat1 = float(lat1)
    lat2 = float(lat2)
    lon1 = float(lon1)
    lon2 = float(lon2)
    
    # Find which bounds go where
    if lat1 > lat2:
        top, bottom = lat1, lat2
    else:
        top, bottom = lat2, lat1
    
    if lon1 > lon2:
        left, right = lon2, lon1
    else:
        left, right = lon1, lon2

    # Go through each city and check to see if it falls within 
    # the specified coordinates.  Return the results.
    return [city for city in cities if (city.lat <= top and
                                        city.lat >= bottom and
                                        city.lon >= left and
                                        city.lon <= right)]

# call the stretch function
within = cityreader_stretch(point1[0], point1[1], point2[0], point2[1], cities)
print(f"Found {len(within)} cities")
# Print the results
for c in within:
    print(c)

if len(within) == 0:
    print("No cities found within those coordinates")
