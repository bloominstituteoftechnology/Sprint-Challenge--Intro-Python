import csv
import sys

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.name}: {self.lat}, {self.lon}"


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
    with open("cities.csv") as cities_file:
        cities_file.readline()
        for row in csv.reader(cities_file):
            cities.append(City(row[0], float(row[3]), float(row[4])))

    # print(cities[0].name, cities[0].lat, cities[0].lon)

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


def get_lat_lons():
    # get user input
    lat_lon1 = input("Enter lat1,lon1: ")
    lat_lon2 = input("Enter lat2,lon2: ")

    # split lat/lon
    (lata, lona) = lat_lon1.split(",")
    (latb, lonb) = lat_lon2.split(",")

    return ((float(lata), float(lona)), (float(latb), float(lonb)))


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # turn into floats
    (ltn1, lnn1, ltn2, lnn2) = (float(lat1), float(lon1), float(lat2), float(lon2))

    # put in ascending order
    if lat2 < lat1:
        (ltn1, ltn2) = (ltn2, ltn1)
    if lnn2 < lnn1:
        (lnn1, lnn2) = (lnn2, lnn1)

    within = [
        c
        for c in cities
        if c.lat > ltn1 and c.lat < ltn2 and c.lon > lnn1 and c.lon < lnn2
    ]

    return within


((lata, lona), (latb, lonb)) = get_lat_lons()

citiesInside = cityreader_stretch(lata, lona, latb, lonb, cities)

print(citiesInside)
