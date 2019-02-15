# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon
  def __repr__(self):
        return f'\nCity("{self.name}", {round(self.lat, 4)},{round(self.lon, 4)})'
import csv
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

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    with open('cities.csv', newline='') as csvfile:
      # next(csvfile, None)
      reader = csv.DictReader(csvfile)
      for row in reader:
        cities.append(City(row['city'], float(row['lat']),float(row['lng'])))
    return cities

cityreader(cities)
# print(cities)
# print(cityreader(cities))

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


# TODO Get latitude and longitude values from the user
# first_latitude = float(input('first latitude ->'))
# first_longitude = float(input('first longitude ->'))
# second_latitude = float(input('second latitude ->'))
# second_longitude = float(input('second longitude ->'))

                      #32    -120  45    -100
def cityreader_stretch(lat2, lon2, lat1, lon1, cities=[]):
  # within will hold the cities that fall within the specified region
  # with open('cities.csv', newline='') as csvfile:
  #     # next(csvfile, None)
  #     reader = csv.DictReader(csvfile)
  #     for row in reader:
  #       cities.append(City(row['city'], round(float(row['lat']), 4),round(float(row['lng']), 4)))
  
  # global first_latitude
  # global first_longitude
  # global second_latitude
  # global second_longitude
  # lat2 = int(first_latitude)
  # lon2 = int(first_longitude)
  # lat1 = int(second_latitude)
  # lon1 = int(second_longitude)

  # # TODO Ensure that the lat and lon valuse are all floats
  # # Go through each city and check to see if it falls within 
  # # the specified coordinates.
  # lat2 = int(first_latitude)
  # lon2 = int(first_longitude)
  # lat1 = int(second_latitude)
  # lon1 = int(second_longitude)
  min_lat, max_lat = min(lat1, lat2), max(lat1, lat2)
  min_lon, max_lon = min(lon1, lon2), max(lon1, lon2)
  print(min_lat)
  print(max_lat)
  # print([x.lat for x in cities])
  # within = []
  within = [x for x in cities if int(x.lat) in range(min_lat, max_lat) and int(x.lon) in range(min_lon, max_lon)]
  print(within)
  return within
  

# cityreader_stretch(first_latitude, first_longitude, second_latitude, second_longitude, cities)