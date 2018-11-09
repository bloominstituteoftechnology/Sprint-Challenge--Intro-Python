import csv
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

class City:
	def __init__(self, name, latitude, longitude):
		self.name = name
		self.latitude = latitude
		self.longitude = longitude

	def __str__(self):
		return f'{self.name}: ({self.latitude},{self.longitude})'

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

filename = 'cities.csv'

with open(filename, 'r') as csvfile:
	csvreader = csv.DictReader(csvfile)

	for row in csvreader:
		cities.append(City(row['city'], row['lat'], row['lng']))

# Print the list of cities (name, lat, lon), 1 record per line.

for city in cities:
	print(city)

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

print('\n*** STRETCH GOAL! ***')

def get_cities_in_region(tuple1, tuple2):
	latMin = min(tuple1[0], tuple2[0])
	latMax = max(tuple1[0], tuple2[0])
	lonMin = min(tuple1[1], tuple2[1])
	lonMax = max(tuple1[1], tuple2[1])

	for city in cities:
		if latMin <= float(city.latitude) <= latMax and lonMin <= float(city.longitude) <= lonMax:
			print(city)

get_cities_in_region((45, -100), (32, -120))
