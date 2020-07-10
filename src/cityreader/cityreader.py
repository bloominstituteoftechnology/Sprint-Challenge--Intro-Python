# Import libraries, packages, modules, functions:
import csv


# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City():
    """
    Represents a city, with attributes representing information about that city.
    """
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    
    def __repr__(self):
        return f"City(name={self.name}, lat={self.lat}, lon={self.lon})"
    
    def __str__(self):
        return f"City(name={self.name}, lat={self.lat}, lon={self.lon})"

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

def cityreader():  # If no set unit test, then would add param filename:str.
    """
    Reads cities and city information in from a CSV file, makes City objects for 
    each one, and returns a list of City objects for each city (row) in the CSV file.
    """
    filename = "cities.csv"
    cities = []
    # Read in the cities and city info as rows from a CSV file:
    with open(filename, "r") as file:
        # Initialize Python csv reader:
        csv_reader = csv.reader(file)
        # Get column names from first row in CSV (also ensures 
        # we don't load the headers in as a city below):
        column_names = next(csv_reader)
        # Get cities data from all remaining rows in the CSV:
        for row in csv_reader:
            city = City(name=row[0], lat=float(row[3]), lon=float(row[4]))
            cities.append(city)

    return cities

cities = cityreader()

# Print the list of cities (name, lat, lon), 1 record per line.
for num, city in enumerate(cities):
    print(f"{num + 1}. {city}")


# -------------------------------------------------------------------------------
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

# # TODO Get latitude and longitude values from the user

# def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
#     # within will hold the cities that fall within the specified region
#     within = []

#     # TODO Ensure that the lat and lon valuse are all floats
#     # Go through each city and check to see if it falls within 
#     # the specified coordinates.

#     return within
