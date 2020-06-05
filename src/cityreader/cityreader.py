import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
  """ 
  This is a class to hold a city location. 
      
  Attributes: 
      name (str): The name of the city. 
      lat (float): The latitude of the city.
      lon (float): The longitude of the city. 
      
  Methods:
  """
  
  def __init__(self, name, lat, lon):
    """ 
    The constructor for the City class. 
  
    Parameters: 
        name (str): The name of the city. 
        lat (float): The latitude of the city.
        lon (float): The longitude of the city.   
    """
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f"({self.name}, {self.lat}, {self.lon})"

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
    """
    Read in cities.csv file. For reach city record, create a ney City instance
    and add it to an empty list "cities"
    """
    file_path = 'C:\\Users\\dougcohen\\Desktop\\Sprint-Challenge--Intro-Python\\src\\cityreader\\cities.csv'

    with open(file_path, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')

      # set line_count to 0 so that we can skip the first line
      line_count = 0
      
      for row in reader:
        if line_count > 0:
          city = City(row[0], float(row[3]), float(row[4]))
          cities.append(city)
        line_count += 1

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

# Get latitude and longitude values from the user
lat_1 = float(input("Please input first latitude value: "))
lat_2 = float(input("Please input second latitude value: "))
lon_1 = float(input("Please input first latitude value: "))
lon_2 = float(input("Please input second latitude value: "))

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  """
  Takes in two latitudes, two longitudes, and a list of City instances, and
  finds cities that lie within those coordinates.
  
  Parameters:
      lat1 (float): first latitude value
      lat2 (float): second latitude value
      lon1 (float): first longitude value
      lon2 (float): second longitude value
      cities (list): list of City class instances
      
  Returns: list of City instances that fall within the coordinates inputed
  """
  # within will hold the cities that fall within the specified region
  within = []

  # TODO Ensure that the lat and lon valuse are all floats
  coord_list = [lat1, lon1, lat2, lon2]

  # separate and sort lat and lon coordinates 
  lat_coords = [coord_list[0], coord_list[2]]
  lon_coords = [coord_list[1], coord_list[3]]
  lat_coords = sorted(lat_coords)
  lon_coords = sorted(lon_coords)

  # Loop through each city and check to see if it falls within 
  # the specified coordinates.
  for city in cities:
    if (city.lat > lat_coords[0] and city.lat < lat_coords[1]) and (
        city.lon > lon_coords[0] and city.lon < lon_coords[1]):
      within.append(city)

  return within
