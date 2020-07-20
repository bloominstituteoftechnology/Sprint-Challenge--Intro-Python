# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


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


class City():
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.lon = long


cities = []


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # Ensure that the lat and lon values are all floats
    # For each city record, create a new City instance and add it to the
    # `cities` list
    with open('cities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            city_name = row[0]
            latitude = float(row[3])
            longitude = -float(row[4][1:])
            cities.append(City(city_name, latitude, longitude))

    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c.name, c.lat, c.lon)

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
user_input = input("Enter lat long e.g 45 -100: ")


words = user_input.split()
lati1 = float(words[0])
long1 = float(words[1][1:])

user_input = input("Enter lat long e.g 32 -120: ")
words = user_input.split()
lati2 = float(words[0])
long2 = -float(words[1][1:])


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    if lat1 < lat2:
        low_lat = lat1
        high_lat = lat2
    else:
        low_lat = lat2
        high_lat = lat1

    if lon1 > lon2:
        low_lon = abs(lon1)
        high_lon = abs(lon2)
    else:
        low_lon = abs(lon2)
        high_lon = abs(lon1)

    # Go through each city and check to see if it falls within
    # the specified coordinates.
    within = [City(city.name, city.lat, city.lon) for city
                                                  in cities
                                                  if city.lat > low_lat and
                                                     city.lat < high_lat and
                                                     abs(city.lon) > low_lon and
                                                     abs(city.lon) < high_lon]

    return within


results = cityreader_stretch(lati1, long1, lati2, long2, cities)

for i in results:
    print(i.name)
