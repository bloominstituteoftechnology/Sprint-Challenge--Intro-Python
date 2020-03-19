import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City():
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon
  
  def __repr__(self):
    return(f'{self.name}: ({self.lat}, {self.lon})')

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

# Implement the functionality to read from the 'cities.csv' file
# For each city record, create a new City instance and add it to the 
# `cities` list

def cityreader(cities=[]):
  """
  Method to read from cities.csv and return a list of cities
  """
  with open('cities.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # count is used to skip the header line
    count = 0
    for row in reader:
        if count>0:
          city_name = row[0]
          lat = row[3]
          lon = row[4]
          cities.append(City(city_name, float(lat), float(lon)))
        count+=1
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

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

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  """
  Method to return what cities are within a rectangle created by
  two latitude and longitude pairs
  """
  # normalize inputs
  min_lat = min([lat1, lat2])
  min_lon = min([lon1, lon2])
  max_lat = max([lat1, lat2])
  max_lon = max([lon1, lon2])

  # get list of cities
  cities = cityreader()

  # within will hold the cities that fall within the specified region
  within = []

  for city in cities:
    lat = float(city.lat)
    lon = float(city.lon)
    # if city lat and lon are within their respective max and min values
    # then add the city to within
    if  lat >= min_lat and lat <= max_lat and \
        lon >= min_lon and lon <= max_lon:
        within.append(city)

  return within

# get latitude and longitude values from the user
print('This program allows you to search for major U.S. cities in the ', \
        'rectangle between two latitude and longitude coordinate pairs')

lat1 = float(input('Please input the latitude of the first point\n'))
lon1 = float(input('Please input the longitude of the first point\n'))

lat2 = float(input('Please input the latitude of the second point\n'))
lon2 = float(input('Please input the longitude of the second point\n'))

print(cityreader_stretch(lat1, lon1, lat2, lon2))
