import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

class City:
  def __init__(self, name, latitude, longitude):
    self.name = name
    self.latitude = latitude
    self.longitude = longitude

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

with open("cities.csv") as csvfile:
  readCSV = csv.DictReader(csvfile)
  [cities.append(City(x["city"], x["lat"], x["lng"])) for x in readCSV]


# Print the list of cities (name, lat, lon), 1 record per line.

[print(x.name, x.latitude, x.longitude) for x in cities]

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

print("\nSeperate lat/long numbers with [, ] (comma + space)")


user_input_1 = input("\n\tEnter first set of latitude/longitude coordinates (lat, lng): ")
user_input_2 = input("\n\tEnter second set of latitude/longitude coordinates (lat, lng): ")


parse_input_1 = user_input_1.split(", ")
parse_input_2 = user_input_2.split(", ")


lats = [parse_input_1[0], parse_input_2[0]]
longs = [parse_input_1[1], parse_input_2[1]]


def validateData(city):
  if city.latitude > max(lats) or city.latitude < min(lats): None
  
  elif city.longitude > max(longs) or city.longitude < min(longs): None

  else: print(city.name, city.latitude, city.longitude)


print() # for terminal aesthetics


[validateData(city) for city in cities]