import csv
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.latitude = float(lat)
        self.longitude = float(lon)

    def __repr__(self):
        return self.name + ' ' + str(self.latitude) + ' ' + str(self.longitude)
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

with open('cities.csv', newline='') as csvfile:
    cities_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    for row in cities_reader:
        if count:
            cities.append(City(row[0], row[3], row[4]))
        else:
            count += 1

# TODO
for city in cities:
    print (city)
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

coord1 =  str(input('Enter your first coordinates'))
coord2 =  str(input('Now second set of coordinates'))

coord1 = coord1.replace(',', ' ')  #remove any commas user may have entered
coord2 = coord2.replace(',', ' ')

coord1 = coord1.split()  #being a str with no ',', we can split into two nums
coord2 = coord2.split()

for i in range(2):
    coord1[i] = float(coord1[i])  #coerce into float
    coord2[i] = float(coord2[i])

coord1[0] = coord1[0]%-90 if coord1[0]<0 else coord1[0]%90    #handle out-of-bounds inputs
coord2[0] = coord2[0]%-90 if coord2[0]<0 else coord2[0]%90
coord1[1] = coord1[1]%-180 if coord1[1]<0 else coord1[1]%180
coord2[1] = coord2[1]%-180 if coord2[1]<0 else coord2[1]%180
lats = [coord1[0], coord2[0]]
longs = [coord1[1], coord2[1]]

for city in cities:
    if city.latitude > min(lats) and city.latitude < max(lats):
        if city.longitude > min(longs) and city.longitude < max(longs):
            print (city)
