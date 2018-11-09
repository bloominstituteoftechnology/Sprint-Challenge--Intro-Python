import csv  # this is to read in the csv file

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.


# City class with name, lat and lon fields to hold the city name the latitude and the longditude
class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon


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

# opening the ciyies.csv file and reading in the data to a list
# found this useful when thinking about this: https://www.youtube.com/watch?v=q5uM4VKywbA

with open('cities.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        cities.append(City(row[0], row[3], row[4]))

# Print the list of cities (name, lat, lon), 1 record per line.

# for in loop printing cities (name, lat, lon), 1 record per line
for city in cities:
    print("{}, {}, {}".format(city.name, city.lat, city.lon))

# *** STRETCH GOAL! ***
#
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

# create a list of the first coordinate set using the list constructor and mapping over the input casting the input to float
latlon1 = list(map(float, input("Enter lat1,lon1: ").strip().split(",")))

# create a list of the second coordinate set using the list constructor and mapping over the input casting the input to float
latlon2 = list(map(float, input("Enter lat2,lon2: ").strip().split(",")))

# use sorted() for normalization normalize the lats and the lons
lats = sorted([latlon1[0], latlon2[0]])
lons = sorted([latlon1[1], latlon2[1]])

# TODO: set the data using a list comprehension outputting the result to the console