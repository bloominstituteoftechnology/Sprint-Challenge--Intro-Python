# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

# TODO
class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __repr__(self):
    return f"{self.name}, {self.lat}, {self.lon}"

  def __str__(self):
    return f"{self.name}, {self.lat}, {self.lon}"

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
import csv

#cities = []

'''with open('C:/Users/Michelle/LambdaCS13/Week-16-Intro-to-Python/Sprint-Challenge--Intro-Python/src/cities.csv', 'r') as f:
  csv_reader = csv.reader(f)
  next(csv_reader)
  data=[tuple(line) for line in csv_reader]
  cities.append(data)
  print(cities)'''

'''with open('C:/Users/Michelle/LambdaCS13/Week-16-Intro-to-Python/Sprint-Challenge--Intro-Python/src/cities.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)
  
  next(csv_reader)

  for line in csv_reader:
    print(line[0], line[3], line[4])
    cities.append(line)

    for i in cities:
      print(cities)'''

# TODO

# Print the list of cities (name, lat, lon), 1 record per line.

# TODO
'''cities = [
    City('Seattle', 47.6217, -122.3238),
    City('Richmond', 37.5294,-77.4755),
    City('Virginia Beach', 36.7335, -76.0435),
    City('Washington', 38.9047, -77.0163),
    City('Milwaukee', 43.0640, -87.9669),
    City('Orlando', 28.4801, -81.3448),
    City('Miami', 25.7840, -80.2102),
    City('Tampa', 27.9937, -82.4454),
    City('Jacksonville', 30.3322, -81.6749),
    City('Albuquerque', 35.1055, -106.6476),
    City('Fort Worth', 32.7813, -97.3466),
    City('McAllen', 26.2203, -98.2457),
    City('El Paso', 31.8478, -106.4310),
    City('Dallas', 32.7938, -96.7659),
    City('Austin', 30.3038, -97.7545),
    City('Houston', 29.7871, -95.3936),
    City('San Antonio', 29.4722, -98.5247),
    City('New Orleans', 30.0687, -89.9288),
    City('Charlotte', 35.2080, -80.8308),
    City('Raleigh', 35.8323, -78.6441),
    City('Omaha', 41.2634, -96.0453),
    City('Memphis', 35.1047, -89.9773),
    City('Nashville', 36.1714, -86.7844),
    City('Buffalo', 42.9016, -78.8487),
    City('Queens', 40.7498, -73.7976),
    City('New York', 40.6943, -73.9249),
    City('Bronx', 40.8501, -73.8662),
    City('Brooklyn', 40.6501, -73.9496),
    City('Manhattan', 40.7834, -73.9662),
    City('Philadelphia', 40.0076, -75.1340),
    City('Pittsburgh', 40.4396, -79.9763),
    City('Sacramento', 38.5666, -121.4683),
    City('Riverside', 33.9382, -117.3949),
    City('San Francisco', 37.7561, -122.4429),
    City('San Diego', 32.8312, -117.1225),
    City('San Jose', 37.3020, -121.8488),
    City('Los Angeles', 34.1140, -118.4068),
    City('Las Vegas', 36.2288, -115.2603),
    City('Denver', 39.7621, -104.8759),
    City('Chicago', 41.8373, -87.6861),
    City('Atlanta', 33.7627, -84.4231),
    City('Indianapolis', 39.7771, -86.1458),
    City('Oklahoma City', 35.4677, -97.5138),
    City('Phoenix', 33.5722, -112.0891),
    City('Tucson', 32.1558, -110.8777),
    City('Bridgeport', 41.1909, -73.1958),
    City('Hartford', 41.7661, -72.6834),
    City('Baltimore', 39.3051, -76.6144),
    City('Boston', 42.3189, -71.0838),
    City('Cleveland', 41.4766, -81.6805),
    City('Columbus', 39.9859, -82.9852),
    City('Cincinnati', 39.1412, -84.5060),
    City('Salt Lake City', 40.7774, -111.9301),
    City('Saint Louis', 38.6358, -90.2451),
    City('Kansas City', 39.1239, -94.5541),
    City('Minneapolis', 44.9635, -93.2679),
    City('Detroit', 42.3834, -83.1024),
    City('Providence', 41.8229, -71.4186),
    City('Louisville', 38.1662, -85.6488),
    City('Portland', 45.5372, -122.6500),
]'''

'''r = [(city.name, city.lat, city.lon) for city in cities]
print(r)'''

'''flat_list = [item for sublist in cities for item in sublist]
print(flat_list)'''

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

# TODO