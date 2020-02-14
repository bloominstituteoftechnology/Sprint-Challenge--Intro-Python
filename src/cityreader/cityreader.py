# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
import csv

class City():
    """City class w/ name, lat and lon """
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f'{self.name}: {self.lat}, {self.lon}'



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
        readfile = csv.reader(csvfile, delimiter = ',') # the cray comma
        count=0
        for locs in readfile:
            if count>0:
                name = locs[0]
                lat = locs[3]
                lon = locs[4]
                cities.append(City(name, lat, lon))
            count += 1
        return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# print('\n'.join(cities))
for c in range(len(cities)):
    print(cities[c])


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
lat1 = float(input("Please enter a lat value:"))
lat2 = float(input("Please enter another lat value:"))
lon1 = float(input("Please enter a lon value:"))
lon2 = float(input("Please enter another lon value:"))

# normalizing the input data:
# Very important! otherwise nothing would be printed lol
lat_min = min([lat1, lat2])
lon_min = min([lon1, lon2])
lat_max = max([lat1, lat2])
lon_max = max([lon1, lon2])

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  # we get the cities from the cityreader() function
  cities = cityreader()

  within = []

  for city in cities:
      lat = float(city.lat)
      lon = float(city.lon)

      if lat >= lat_min and lat <= lat_max and \
         lon >= lon_min and lon <= lon_max:
         within.append(city)

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within
  # the specified coordinates.
  return within

print(cityreader_stretch(lat1, lon1, lat2, lon2))
