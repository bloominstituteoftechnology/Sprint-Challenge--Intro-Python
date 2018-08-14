import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

class City:
  def __init__(self, name, latitude, longitude, population):
    self.name = name
    self.latitude = latitude
    self.longitude = longitude
    self.population = population

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

with open('cities.csv', 'rt', encoding='utf8') as f:
  data = csv.DictReader(f)
  cities = [City(row['city'], row['lat'], row['lng'], row['population']) for row in data]

for city in cities:
  print(city.name, city.latitude, city.longitude, city.population)

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

first_coordinates = input('\n\n📍 Enter first point (latitude, longitude): ').split()
second_coordinates = input('\n\n📍 Enter second point (latitude, longitude): ').split()

min_lat = min(first_coordinates[0], second_coordinates[0])
max_lat = max(first_coordinates[0], second_coordinates[0])
min_lng = min(first_coordinates[1], second_coordinates[1])
max_lng = max(first_coordinates[1], second_coordinates[1])

matching_cities = [
  city for city in cities
  if city.latitude >= min_lat and city.latitude <= max_lat and city.longitude >= min_lng and city.longitude <= max_lng
]

for city in matching_cities:
  print(f'{city.name}: ({city.latitude},{city.longitude})')
