# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
import csv

class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = float(latitude)
        self.longitude = float(longitude)

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

# TODO
# MVP1 RIGHT HERE \/\/\/
with open("cities.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    
    for row in readCSV:
        print (row[0],row[3],row[4])

#MVP2
with open("cities.csv", newline="") as csvfile:
    cityreader = csv.reader(csvfile, delimiter=",", quotechar="|")
    passedHeader = False
    for row in cityreader:
        if passedHeader:
            cities.append(City(row[0], row[3], row [4]))
        else:
            passedHeader = True

# for city in cities:
#     print(f"({city.name}, {city.latitude}, {city.longitude})")

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

#THIS IMPLEMENTATION WORKS ON OWN
#THIS WILL ASK FOR SPECIFIC LAT/LONG
#AND RETURN BOTH IN THE PRINT
# with open("cities.csv") as csvfile:
#     readCSV = csv.reader(csvfile, delimiter = ',')

#     lats = []
#     longs = []

#     for row in readCSV:
#         lat = row[3]
#         lon = row[4]

#         lats.append(lat)
#         longs.append(lon)

#     print(lats)
#     print(longs)

#     whatLat = input("What lat do you wish to see?:")
#     whatLon = input("what lon do you wish to see?:")
#     latidex = lats.index(whatLat)
#     longidex = longs.index(whatLon)
#     print(f"the lat/lon is:", whatLat, whatLon)

#THIS IS 1 IMPLEMENTATION FOR STRETCH
# latlon1Valid = False
# latlon2Valid = False

# while not latlon1Valid:
#     latlon1 = input("Enter lat1,lon1: ")
#     latlon1list = latlon1.split(",")
#     if len(latlon1list) == 2:
#         lat1 = float(latlon1list[0])
#         lon1 = float(latlon1list[1])
#         #PUT VALIDATOR HERE TO TELL IF INPUTS ARE IN RANGE
#         latlon1Valid = True
#     else:
#         print("invalid input")

# while not latlon2Valid:
#     latlon2 = input("Enter lat2,lon2: ")
#     latlon2list = latlon2.split(",")
#     if len(latlon2list) == 2:
#         lat2 = float(latlon2list[0])
#         lon2 = float(latlon2list[1])
#         #PUT VALIDATOR HERE TO TELL IF INPUTS ARE IN RANGE
#         latlon2Valid = True
#     else:
#         print("invalid input")

# latMin = min(lat1, lat2)
# lonMin = min(lon1, lon2)
# latMax = max(lat1, lat2)
# lonMax = max(lon1, lon2)

# # PRINT THESE TO DOUBLE CHECK FOR ERROR
# # print(f"{latMin}, {latMax}, {lonMin}, {lonMax}")

# for city in cities:
#     if city.latitude >= latMin and city.latitude <= latMax \
#             and city.longitude >= lonMin and city.longitude <= lonMax:
#         print(f"{city.name}: ({city.latitude}, {city.longitude})")



#ANOTHER IMPLEMENTATION OF STRETCH
lat1, lon1 = [float(v) for v in input("enter lat1,lon1: ").split(",")]
lat2, lon2 = [float(v) for v in input("enter lat2,lon2: ").split(",")]

if lat2 < lat1:
    lat1, lat2 = lat2, lat1

if lon2 < lon1:
    lon1, lon2 = lon2, lon1

for city in cities:
    if city.latitude >= lat1 and city.latitude <= lat2 \
            and city.longitude >= lon1 and city.longitude <= lon2:
        print(f"{city.name}: ({city.latitude}, {city.longitude})")