# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
  
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __repr__(self):
    return f'{self.name}, {self.lat},{self.lon}'

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
import csv

cities = []

def cityreader(cities=[]):

  # Implement the functionality to read from the 'cities.csv' file
  with open('/Users/audreywelch/Dropbox/Lambda School/Computer_Science/Sprint_01_Python/Sprint_Challenge/Sprint-Challenge--Intro-Python/src/cityreader/cities.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0

    # For each city record, create a new City instance and add it to the `cities` list
    for row in csv_reader:
      if line_count == 0:
        line_count += 1
      else:
        cities.append(City(str(row[0]), float(row[3]), float(row[4])))
        line_count += 1

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

# TODO Get latitude and longitude values from the user
first_raw_input = input("Enter lat1,lon1: ")
second_raw_input = input("Enter lat2,lon2: ")

first_split_input = first_raw_input.split(",")
second_split_input = second_raw_input.split(",")

# Ensure that the lat and lon values are all floats
input1 = [float(each) for each in first_split_input]
input2 = [float(each) for each in second_split_input]

lat1 = input1[0]
lat2 = input2[0]
lon1 = input1[1]
lon2 = input2[1]

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  
  # within will hold the cities that fall within the specified region
  within = []

  # Ensure that the lat and lon values are all floats
  lat_float1 = float(lat1)
  lat_float2 = float(lat2)
  lon_float1 = float(lon1)
  lon_float2 = float(lon2)

  latsBool = False
  lonsBool = False

  # Go through each city and check to see if it falls within 
  # the specified coordinates.
  for each_city in cities:
    if each_city.lat >= lat_float1 and each_city.lat <= lat_float2 or each_city.lat >= lat_float2 and each_city.lat <= lat_float1:
      latsBool = True
    
    if each_city.lon >= lon_float1 and each_city.lon <= lon_float2 or each_city.lon >= lon_float2 and each_city.lon <= lon_float1:
      lonsBool = True

    if latsBool and lonsBool == True:
      within.append(each_city)

  #print(within)
  return within

#cityreader_stretch(lat1, lon1, lat2, lon2, cities)