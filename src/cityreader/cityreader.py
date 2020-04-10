# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City():
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f'{self.name}, {self.lat}, {self.lon}'

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

import os.path
import csv

cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    with open(os.path.dirname(__file__) +  '/cities.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
          # print(f'Column names are {", ".join(row)}')
          line_count += 1
        else:
          # print(f'\tCity: {row[0]}  State: {row[1]} County: {row[2]} Lat: {row[3]} Lon {row[4]}')
          cities.append(City(row[0], float(row[3]), float(row[4]))) #Added float to get test to pass
          line_count += 1
      # print(f'Processed {line_count} lines.')
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
#     print(c)

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

# TODO Get latitude and longitude values from the user
# first = input('Enter first lat, lon: ')
# second = input('Enter second lat, lon: ')
# firsts = first.split(',')
# seconds = second.split(',')

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.
  print(f'----------------Inputs: {lat1}, {lon1}, {lat2}, {lon2}')
  # 
  clat1 = float(lat1)
  clat2 = float(lat2)
  clon1 = float(lon1)
  clon2 = float(lon2)
  if lat1 > lat2: #Arranges inputs to correct order (low to high)
    # print(f'lat1 is greater')
    clat1 = lat2
    clat2 = lat1
  if lon1 > lon2: #Arranges inputs to correct order (low to high)
    # print(f'lon1 is greater')
    clon1 = lon2
    clon2 = lon1
# -----------First attempt, no floats--------------
  # for city in cities:
  #   # print (float(city.lat))
  #   if int(city.lat) in range(int(clat1), int(clat2)):
  #     if int(city.lon) in range(int(clon1), int(clon2)):
  #       print(city)
  #       within.append(city)
# -----------Second attempt, with floats------------
  for city in cities:
    if city.lat >= clat1 and city.lat <= clat2:
      if city.lon >= clon1 and city.lon <= clon2:
        print(city)
        within.append(city)

  return within

cityreader_stretch(42, -120, 32, -100, cities)
# cityreader_stretch(int(firsts[0]), int(firsts[1]), int(seconds[0]), int(seconds[1]), cities)
# cityreader_stretch(45, -100, 32, -120, cities)