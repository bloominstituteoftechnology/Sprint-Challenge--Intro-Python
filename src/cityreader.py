import csv
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

# TODO
class City:
    """City object holds city location data."""
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    def __repr__(self):
        return "<City Name: {}, Lat: {}, Lon: {}>".format(self.name, self.lat, self.lon)

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
with open('cities.csv', newline='') as csvfile:
    city_reader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    city_list = [city[0].split(',') for city in city_reader] #Stores each city as a list of relevant values for easier access

cities = [City(city_info[0], float(city_info[3]), float(city_info[4])) for city_info in city_list[1:]]

# Print the list of cities (name, lat, lon), 1 record per line.
for city in cities:
    print(city)

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
# Enter lat1,lon1: 45,-100 upper/right
# Enter lat2,lon2: 32,-120 lower/left
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)


coordinates_1 = input("Enter lat1, lon1: ").split(',')
coordinates_2 = input("Enter lat2, lon2: ").split(',')

#convert inputs to floats
coordinates_1 = list(map(lambda x: float(x), coordinates_1))
coordinates_2 = list(map(lambda x: float(x), coordinates_2))

#normalize data to lower-left/upper-right
if coordinates_1[0] > coordinates_2[0]:
    lat_one = coordinates_1[0]
    lon_one = coordinates_1[1]
    lat_two = coordinates_2[0]
    lon_two = coordinates_2[1]
    coordinates_2[0] = lat_one
    coordinates_2[1] = lon_one
    coordinates_1[0] = lat_two
    coordinates_1[1] = lon_two


coordinates = coordinates_1 + coordinates_2

#finds cities within coordinate square
locatedCities = [city for city in cities if coordinates[0] <= city.lat <= coordinates[2] and coordinates[1] < city.lon < coordinates[3]]


for city in locatedCities:
    print(city)
