import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)


# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

def cityreader():
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list

  with open("./src/cityreader/cities.csv") as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

    cities = [City(info[0], float(info[3]), float(info[4])) for info in reader]
  
    return cities

cities = cityreader()
print(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c.name, c.lat, c.lon)

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

# # TODO Get latitude and longitude values from the user

lat1 = float(input('Enter in first latitude: '))
lon1 = float(input('Enter in first longitude: '))
lat2 = float(input('Enter in first latitude: '))
lon2 = float(input('Enter in second longitude: '))

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):

  within = []
  
  coords = [lat1, lon1, lat2, lon2]

  lat = [coords[0], coords[2]]
  lon = [coords[1], coords[3]]

  lat = sorted(lat)
  lon = sorted(lon)

  for city in cities:
    if (city.lat > lat[0] and city.lat < lat[1]) and (city.lon > lon[0] and city.lon < lon[1]):
      within.append(city)
  return within


cityreader_stretch(lat1, lat2, lon1, lon2)

# ooooold code :
# lat1 = float(input("\nEnter in the latitude for point 1:\n"))
# lon1 = float(input("Enter in the longitude 1:\n"))

# lat2 = float(input("\nEnter in the latitude for point 2:\n"))
# lon2 = float(input("Enter in the longitude 2:\n"))

# def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
#   # within will hold the cities that fall within the specified region

#   lat_1, lon_1, lat_2, lon_2 = lat1, lon1, lat2, lon2

#   within = []
#   print("lat1:", lat1)
#   print("lat2:", lat2)

#   if lat_1 > lat_2:
#     print("HI1")
#     bigger_lat = lat_1
#     smaller_lat = lat_2
#   elif lat_2 < lat_1:
#     print("HI2")
#     bigger_lat = lat_2
#     smaller_lat = lat_1
  
#   if lon_1 > lon_2:
#     print("HI3")
#     bigger_lon = lon_1
#     smaller_lon = lon_2
#   elif lon_2 > lon_1:
#     print("HI4")
#     bigger_lon = lat_2
#     smaller_lon = lat_1

#   for city in cities:
#     print("bigger lat:", bigger_lat)
#     print("smaller lat:", smaller_lat)
#     if city.lat <= bigger_lat and city.lat >= smaller_lat:
#       print(city)
  
#   # within = [city for city in cities if ((city.lat <= bigger_lat and city.lat >= smaller_lat) and (city.lon <= bigger_lon and city.lon >= smaller_lon))]

#   # TODO Ensure that the lat and lon valuse are all floats
#   # Go through each city and check to see if it falls within 
#   # the specified coordinates.

#   print(within)
#   return within




