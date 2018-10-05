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

with open('cities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        name = row[0]
        latitude = row[3]
        longitude = row[4]
        if line_count > 0:
            cities.append(City(name, latitude, longitude))
        line_count += 1

# Print the list of cities (name, lat, lon), 1 record per line.
# for city in cities:
#     print(city.name, city.latitude, city.longitude)

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

def find_city():
    latitude_1 = input('Please enter first latitude:  ')
    longitude_1 = input('Please enter first longitude:  ')
    latitude_2 = input('Please enter second latitude:  ')
    longitude_2 = input('Please enter second longitude:  ')

    if latitude_1 > latitude_2:
        latitude_max = latitude_1 
        latitude_min = latitude_2
    else:
        latitude_max = latitude_2
        latitude_min = latitude_1

    if longitude_1 > longitude_2:
        longitude_max = longitude_1 
        longitude_min = longitude_2
    else:
        longitude_max = longitude_2
        longitude_min = longitude_1

    def __check_latitude__(latitude):
        return latitude <= latitude_max and latitude >= latitude_min

    def __check_longitude__(longitude):
        return longitude <= longitude_max and longitude >= longitude_min

    for city in cities:
        if __check_latitude__(city.latitude) and __check_longitude__(city.longitude):
            print(f"{ city.name }: ({ city.latitude }, { city.longitude })")


find_city()