# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
import csv 
# import os
# cwd = os.getcwd()
# files = os.listdir(cwd)
# print(files)
# TODO
class City(object):
    def __init__(self, name,latitude,longitude):
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
count = 0 
with open('src/cities.csv', newline="") as csvfile:
    cityReader = csv.reader(csvfile, delimiter=",", quotechar = "|")
    for row in cityReader:
        if count > 0: 
            print(row[0], row[3], row[4])
            cities.append( City(row[0],float(row[3]), float(row[4])) )
        count+= 1 
# TODO

# Print the list of cities (name, lat, lon), 1 record per line.
#Completed on the same line as the append to cities. 
# TODO

# *** STRETCH GOAL! ***

# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#


# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other (what is latMin, latMax?)
# then search for cities.
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


""" Completed the stretch goal here because the system we are using doesn't allow me to enter inputs. Read only terminal
 https://repl.it/@codejoncode/NarrowInfatuatedElements
  """
# TODO
points1 = input("Min's Enter two points latitude and longitude(seperate by comma or space)::-> ")
#
points1.split()
if "," in points1:
  points1 = points1.replace(",", " ")
if "  " in points1:
  points1 = points1.replace("  ", " ")
  print(points1)
  points1 = points1.split()
else:
  points1 = points1.split()
#
points2 = input("Max's Enter two points latitude and longitude(seperate by comma or space)::-> ")

points2.split()
if "," in points2:
  points2 = points2.replace(",", " ")
if "  " in points2:
  points2 = points2.replace("  ", " ")
  points2 = points2.split()
else:
  points2 = points2.split()
#


points1[0] = int(points1[0]); points1[1] = int(points1[1]);
points2[0] = int(points2[0]); points2[1] = int(points2[1]);


for city in cities:
  if city.latitude <= points1[0] and city.latitude >= points2[0]:
    # new line for readiablity could use just another set of and's.
    if city.longitude <= points1[1] and city.longitude >= points2[1]:
      print (f"{city.name}: ({city.latitude}, {city.longitude})")
#