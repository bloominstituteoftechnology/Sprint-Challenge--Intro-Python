# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
import csv # (comma separeted values) import and export format for spreadsheets and database

class City:
      def __init__(self, name, lat, lon):
            self.name = name
            self.lat = lat
            self.lon = lon
      
      def __str__(self):
            return f'City({self.name}, {self.lat}, {self.lon})'

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

  # with open("src/cityreader/cities.csv") as file: 
  #   reader = csv.DictReader(file) # used DictReader to map the information in each row to a dictionary whose keys are given by the optional fieldnames parameter.
  #   for city in reader:           # I did not use fieldname / trying to make it less code /puts  key / gets value 
  #         new_city = City(city["city"], float(city["lat"]), float(city["lng"]))
  #         cities.append(new_city)

   with open("src/cityreader/cities.csv") as cvsfile:
     reader = csv.DictReader(cvsfile)
     for dictionary in reader: 
           cities.append(City(dictionary["city"], float(dictionary["lat"]), float(dictionary["lng"]))) # city lat long is the value 

    
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

input1 = input("Enter lat1,lon1: ").split(",") 
input2 = input("Enter lat2,lon2: ").split(",")
lat1, lon1 = float(input1[0]), float(input1[1])
lat2, lon2 = float(input2[0]), float(input2[1])

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
      
  # within will hold the cities that fall within the specified region

  # within = [print(city) for city in cities if city.lat <= max(lat1, lat2) and city.lat >= min(lat1, lat2)if city.lon <=max(lon1, lon2) and city.lon >= min(lon1, lon2)]
  within = []

  for city in cities:
        if city.lat <= max(lat1, lat2) and city.lat >= min(lat1, lat2): #comparing my inputs with the cities latitude 
              if city.lon <= max(lon1, lon2)  and city.lon >= min(lon1, lon2): #comparing my inputs with the cities longitude 
                  within.append(city)
                  print(city) 
              else:
                print(f"{city.name} longitude is not between {lon1} and {lon2}")

        else:
          print(f"{city.name} latitude is not between {lat1} and {lat2}")
                
  # within = [city for city in cities
  # if float(city.lat) >= city.lat[0]]
  # for city in cityreader_stretch(lat1, lon1, lat2, lon2, cities):
  #   print(city.name)
  #   within.append(city)
  
  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within

cityreader_stretch(lat1, lon1, lat2, lon2, cities)

