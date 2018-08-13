import csv
import math
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
# TODO
class City:
    def __init__( self, name, latitude, longitude ):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__( self ):
        return f'{self.name}, {self.latitude}, {self.longitude}: '

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

with open('cities.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        cities.append( City(row[0], row[3], row[4]))

# TODO

# Print the list of cities (name, lat, lon), 1 record per line.


def city_print(city_list):
    for i in city_list:
        print(str(i))

# def city_print_coords(city_list):
#     for i in city_list:
#         print(f'{i.latitude}, {i.longitude}')

def city_print_coords(city):
    print(str(city))
city_print(cities)
# TODO

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
# TODO
coordinates = ''
while not coordinates == 'q':

    print('Welcome to city square location finder program thing that does stuff\n')
    print('Please have two points designated by proper longitude and latitude values available before continuing. Press q at any time to exit program \n')

    coordinates = input('Please enter a valid (latitude(-90 to +90) longitude(-180 to +180)) for point 1: ')
    coordinate_split = coordinates.split()
    if coordinate_split[0].isdigit():
        if -90 <= int(coordinate_split[0]) <= 90 and -180 <= int(coordinate_split[1]) <= 180:
            latitude1 = float(coordinate_split[0])
            longitude1 = float(coordinate_split[1])
            coordinates = input('Please enter a valid (latitude(-90 to +90) longitude(-180 to +180)) for point 2: ')
            coordinate_split = coordinates.split()
        if coordinate_split[0].isdigit():
            if -90 <= int(coordinate_split[0]) <= 90 and -180 <= int(coordinate_split[1]) <= 180:
                latitude2 = float(coordinate_split[0])
                longitude2 = float(coordinate_split[1])
                if latitude1 > latitude2:
                    latitude1, latitude2 = latitude2, latitude1
                    if longitude1 > longitude2:
                        longitude1, longitude2 = longitude2, longitude1
                        for i in cities:
                            if latitude1 <= math.floor(float(i.latitude)) <= latitude2:
                                if longitude1 <= math.floor(float(i.longitude)) <= longitude2:
                                    print(f'\t{i}')

                    else:
                        for i in cities:
                            if latitude1 <= math.floor(float(i.latitude)) <= latitude2:
                                if longitude1 <= math.floor(float(i.longitude)) <= longitude2:
                                    print(f'\t{i}')

                else:
                    if longitude1 > longitude2:
                        longitude1, longitude2 = longitude2, longitude1
                        for i in cities:
                            if latitude1 <= math.floor(float(i.latitude)) <= latitude2:
                                if longitude1 <= (math.floor(float(i.longitude))) <= longitude2:
                                    print(f'\t{i}')

                    else:
                        for i in cities:
                            if latitude1 <= math.floor(float(i.latitude)) <= latitude2:
                                if longitude1 <= (math.floor(float(i.longitude))) <= longitude2:
                                    print(f'\t{i}')

    else:
        print('please enter valid numbers')


