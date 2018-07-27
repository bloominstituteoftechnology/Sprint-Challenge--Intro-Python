import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

# TODO

class City:
  def __init__(self, name, latitude, longitude):
    self.name = name
    self.latitude = float(latitude)
    self.longitude = float(longitude)

  def in_range(self, p_1, p_2):
    # Account for string input
    p_1 = [int(val) for val in p_1]
    p_2 = [int(val) for val in p_2]

    # Normalize input values
    min_lat, max_lat = min(p_1[0], p_2[0]), max(p_1[0], p_2[0])
    min_lon, max_lon = min(p_1[1], p_2[1]), max(p_1[1], p_2[1])

    # Test range boundaries
    lat_in_range = self.latitude >= min_lat and self.latitude <= max_lat
    lon_in_range = self.longitude >= min_lon and self.longitude <= max_lon

    return lat_in_range and lon_in_range


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

with open('cities.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)

  for city in reader:
    cities.append(City(city['city'], city['lat'], city['lng']))

# Print the list of cities (name, lat, lon), 1 record per line.

# TODO

[print(f'{city.name}: {city.latitude}, {city.longitude}') for city in cities]

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

## Hard coded test case
# p_1 = '45,-100'.split(',')
# p_2 = '32,-120'.split(',')

p_1 = input('Please input a latitude and longitude value pair seperated by a comma: ').split(',')
p_2 = input('Please input another latitude and longitude value pair seperated by a comma: ').split(',')

# Moved logic into city class for more concise evaluation
[print(f'{city.name}: {city.latitude}, {city.longitude}') for city in cities if city.in_range(p_1, p_2)]