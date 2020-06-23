import csv
from typing import List

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
  def __init__(self, name: str, lat: float, lon: float):
    self.name = name
    self.lat = lat
    self.lon = lon

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

def cityreader(cities=[]) -> List[City]:
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open('cities.csv', mode='r', newline='') as cities_file:
    reader = csv.reader(cities_file)
    next(reader)
    for row in reader:
      cities.append(City(row[0], float(row[3]), float(row[4])))
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(f"Name: {c.name} Lat: {c.lat} Lon: {c.lon}")

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

def search_for_cities():
  user_input = input("Enter the first coordinate (lat,lon)")
  coord = user_input.split(',')

  lat1 = coord[0]
  lon1 = coord[1]

  user_input = input("Enter the second coordinate (lat,lon)")
  coord = user_input.split(',')

  lat2 = coord[0]
  lon2 = coord[1]

  results = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
  city_names = [city.name for city in results]

  print(city_names)


# This function doesn't account for the anti-meridian

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):

  try:
    lat1 = float(lat1)
    lat2 = float(lat2)
    lon1 = float(lon1)
    lon2 = float(lon2)
  except ValueError as error:
    print(f"Invalid input: {error}")  
    return [] 

  min_lat = min(lat1, lat2)
  max_lat = max(lat1, lat2)
  min_lon = min(lon1, lon2)
  max_lon = max(lon1, lon2)   

  return [city for city in cities if min_lat <= city.lat <= max_lat and min_lon <= city.lon <= max_lon]


# cityreader_stretch(45, -100.0, 32.0, -120.0, cities)
# search_for_cities()