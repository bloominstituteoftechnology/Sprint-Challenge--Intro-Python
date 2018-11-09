import csv
import sys
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

class City:
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

cities = []

with open('cities.csv') as csvfile:
    reader = csv.reader(csvfile)
    firstline = True
    for row in reader:
        if firstline:
            firstline = False
            continue
        cities.append(City(row[0],row[3],row[4]))

# Print the list of cities (name, lat, lon), 1 record per line.

for city in cities:
    print(f'{city.name}- lat:{city.latitude} lon:{city.longitude}')

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
def get_point(num):
    if num==1:
        point = input('Enter a lat1,lon1: ')
    elif num==2:
        point = input('Enter a lat2,lon2: ')
    else:
        print('check() used incorrectly')
        sys.exit(0)
    lon = ''
    lat = ''
    found_comma = False
    for char in point:
        if char ==',':
            found_comma = True
            continue
        elif not found_comma:
            lon += char
        elif found_comma:
            if(char==' '):
                continue
            lat += char
    if not found_comma:
        print('Please enter two numbers separated by a comma.')
        sys.exit(0)
    else:
        return (float(lon), float(lat))

def normalize(point1, point2):
    lat1, lon1 = point1
    lat2, lon2 = point2
    latMax = lat1 if lat1>lat2 else lat2
    latMin = lat1 if latMax==lat2 else lat2
    lonMax = lon1 if lon1>lon2 else lon2
    lonMin = lon1 if lonMax==lon2 else lon2
    return (latMax, latMin, lonMax, lonMin)

point1 = get_point(1)
point2 = get_point(2)
points = normalize(point1, point2)
latMax, latMin, lonMax, lonMin = points
for city in cities:
    if latMin<=float(city.latitude)<=latMax and lonMin<=float(city.longitude)<=lonMax:
        print(f'{city.name}- lat:{city.latitude} lon:{city.longitude}')
