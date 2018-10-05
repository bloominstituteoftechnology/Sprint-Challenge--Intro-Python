import csv
import os 
# import numpy as pynum

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.


class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "<City: %s, %s, %s>" % (self.name, self.latitude, self.longitude)


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

f = open('cities.csv', 'r')

with f:

    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        cities.append(City(row[0], row[3], row[4]))

# Print the list of cities (name, lat, lon), 1 record per line.

for city in cities:
    print(
        f'{city.name}, Latitude: {city.latitude}, Longitude: {city.longitude} ')


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

while True:
    coordinates_1 = input("Enter lat1,lon1: ")
    if coordinates_1 == "q":
        break
    coordinates_2 = input("Enter lat2,lon2: ")
    if coordinates_2 == "q":
        break
    else:
        coordinates_1 = coordinates_1.replace(",", " ").split()
        coordinates_2 = coordinates_2.replace(",", " ").split()
        lat1 = int(coordinates_1[0])
        lon1 = int(coordinates_1[1])
        lat2 = int(coordinates_2[0])
        lon2 = int(coordinates_2[1])
        if lat1 in range(-90, 91) and lat2 in range(-90, 91) and lon1 in range(-180, 181) and lon2 in range(-180, 181):
            # print(lat1)
            # print(lon1)
            # print(lat2)
            # print(lon2)
            # continue
            for city in cities:
                if city.latitude in range(lat1, lat2 + 1) and city.longitude in range(lon1, lon2 + 1):
                    # problem installing numpy due to this errorh ttps://github.com/pypa/pipenv/issues/2871
                    # if can find a fix it will let me do range with floats and print what i want
                    print(
                        f'{city.name}, Latitude: {city.latitude}, Longitude: {city.longitude} ')
                else:
                    os.system("clear")
                    continue

        else:
            print("Invalid. Please enter valid coordinates.")
