# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


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
import os
class City:
      def __init__(self, name, lat, lon):
            self.name = name
            self.lat = lat
            self.lon = lon

cities = []

def cityreader(cities=[]):
      # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    with open('cities.csv', 'r') as city_file:
      dictionary = csv.DictReader(city_file, delimiter=',', quotechar='|')
      
      for row in dictionary:
            city = City(row['city'],row['lat'],row['lng'])
            cities.append(city)
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
city_list = []
for c in cities:
      city = 'City: %s, Lat: %s, Long: %s' %(c.name, c.lat, c.lon)
      city_list.append(city)


print(*city_list, sep = '\n')


