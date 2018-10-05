# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

import csv 

# TODO
class CityLocation():
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


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

# with open('cities.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader: 
#         print(row['city'], row['lat'], row['lng'])


# cities = [city.name for city in 'cities.csv']

# TODO

# Print the list of cities (name, lat, lon), 1 record per line.

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

global maxLat
global maxLng
global minLng
global maxLng

class Point():
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

inputA = input('insert lat1, lng1:   ')
modA = [x.strip() for x in inputA.split(',')]
if 2 < len(inputA) < 1:
    print('invalid input, please use comma to seperate')
else: 
    inputB = input('insert lat2, lng2:   ')
    modB = [x.strip() for x in inputB.split(',')]
    if 2 < len(inputB) < 1:
        print('invalid input, please use comma to seperate')
    else: 
        print("modA", modA, 'modB', modB)
        modA = Point(modA[0], modA[1])
        modB = Point(modB[0], modB[1])
        print(modB.lat, modB.lng)
        print('modB.lat', 'modB.lng')
        if modB.lat > modA.lat: 
            maxLat = modB.lat
            minLat = modA.lat
        else: 
            maxLat = modA.lat
            minLat = modB.lat
        if modB.lng > modA.lng: 
            maxLng = modB.lng
            minLng = modA.lng
        else: 
            maxLng = modA.lng
            minLng = modB.lng
        print("maxLng", maxLng, "minLng", minLng, "maxLat", maxLat, "minLat", minLat)
        with open('cities.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # data = [row['city'] for row in reader if (minLat < row['lat'] < maxLat) and (minLng < row['lng'] < maxLng)]
            # print(data)
            print(f"\nList of Cities located within ({maxLng},{maxLat}) & ({minLng},{minLat})\n")
            for row in reader:
                if (minLat < row['lat'] < maxLat) and (minLng < row['lng'] < maxLng):
                    print(f"    {row['city']}: ({row['lat']}, {row['lng']})")

            
        # coolList = [f"{city.city}: ({city.lat}, {city.lng})" for city in row if minLat < city.lat < maxLat and minLng < city.lng < maxLng ]
        # return coolList

# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120

'''
45,-100
32,-120
'''