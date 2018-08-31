# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

# TODO
class City:
    def __init__(self, name, state_name=None, county_name=None, lat=None, lng=None, population=None, density=None, timezone=None, zips=None):
        self.name = name
        self.state_name = state_name
        self.county_name = county_name
        self.latitude = lat
        self.longitude = lng
        self.population = population
        self.density = density
        self.timezone = timezone
        self.zips = zips

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

# TODO
with open('cities.csv', 'r') as f:
    next(f)
    for line in f:
        cities.append(line.split(','))

for city in cities:
    city = City(city[0], city[3], city[4])

# Print the list of cities (name, lat, lon), 1 record per line.

# TODO
print('\nPrint the list of cities (name, lat, lon), 1 record per line.')
for city in cities:
    print(f'({city[0]}, {city[3]}, {city[4]})')

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

# TODO
input_1 = input('\nEnter lat1, lon1: ')
input_2 = input('Enter lat2, lon2: ')
inputs_1 = [int(n) for n in input_1.split(',')]
inputs_2 = [int(n) for n in input_2.split(',')]
x1 = inputs_1[0] if inputs_1[0] < inputs_2[0] else inputs_2[0]
x2 = inputs_2[0] if inputs_2[0] > inputs_1[0] else inputs_1[0]
y1 = inputs_1[1] if inputs_1[1] < inputs_2[1] else inputs_2[1]
y2 = inputs_2[1] if inputs_2[1] > inputs_1[1] else inputs_1[1]
print('\nCities that match coordinates.')
for city in cities:
     if (int(float(city[3])) in range(x1, x2 + 1) and int(float(city[4])) in range(y1, y2 + 1)):
        print(f'{city[0]}: ({city[3]}, {city[4]})')
