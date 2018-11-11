# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat, and lon.

class City():
  def __init__(self, name, lat, lon):
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
import csv

cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open ('cities.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
      cities.append(City(line[0], line[3], line[4]))

    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(f"{c}")

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by lat and lon.
# These points form the corners of a lat/lon square. Pass these lat and 
# lon values as parameters to the `cityreader_stretch` function, along
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

# # TODO Get lat and lon values from the user
# lat_A = int(input("Enter lat for first set"))
# lon_A = int(input("Enter lon for first set"))
# lat_B = int(input("Enter lat for second set"))
# lon_B = int(input("Enter lon for second set"))

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []
  lat_min = min(float(lat1),float(lat2))
  lat_max = max(float(lat1),float(lat2))
  lon_min = min(float(lon1),float(lon2))
  lon_max = max(float(lon1),float(lon2))

  for city in cities:
    if lat_min <= float(city.lat) <= lat_max and lon_min <= float(city.lon) <= lon_max:
      print(f"{city.name} {city.lat} {city.lon}")
      within.append(city)
 
  return within


  # for city in cities:
  #   if lat1 > lat2:
  #     if lon1 > lon2:
  #       if lat2 <= float(city.lat) <= lat1 and lon2 <= float(city.lon) <= lon1:
  #         print('somethings workin', city)
  #         within.append(city)
  #     else: #lon2 > lon1
  #       if lat2 <= float(city.lat) <= lat1 and lon1 <= float(city.lon) <= lon2:
  #         print('somethings workin', city)
  #         within.append(city)
  #   else:
  #     if lon1 > lon2:
  #       if lat2 <= float(city.lat) <= lat1 and lon2 <= float(city.lon) <= lon1:
  #         print('somethings workin', city)
  #         within.append(city)
  #     else: #lon2 > lon1
  #       if lat2 <= float(city.lat) <= lat1 and lon1 <= float(city.lon) <= lon2:
  #         print('somethings workin', city)
  #         within.append(city)


  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

first = input("Enter first group").split(",")
second = input("Enter second group").split(",")

cityreader_stretch(first[0], first[1], second[0], second[1], cities)