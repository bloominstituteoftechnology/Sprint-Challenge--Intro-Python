# Create a class to hold a city location. Call the class "City". It should have
# fields for nam
#e, lat and lon (representing latitude and longitude).
import csv

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
cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open('./src/cityreader/cities.csv', 'r') as c:
    readlist = csv.reader(c)
    for row in readlist:
      if row[0] != 'city':
        cities.append(City(row[0],float(row[3]),float(row[4])))
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c.name + ', ' + str(c.lat) + ', ' + str(c.lon))