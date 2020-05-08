import csv
import os

datafile_name = 'cities.csv'
cwd = os.getcwd()
path_name = cwd + '/' + datafile_name

class City():
    def __init__(self, name, lat, lon):
        """Store the name, latitude, and longitude
        for a city.
        Input is received as three strings.  The 
        lat and log values are converted to floats."""
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)
        
    def __str__(self):
        """Print out strings in (City): (lat, long) format."""
        return f'{self.name}: ({self.lat}, {self.lon})'

def get_required_data(row):
    """Index 0: city name
    Index 3: latitude
    Index 4: longitude"""
    return [row[0]]+row[3:5]
    
def cityreader(cities=[]):
    """Read a CSV file, and create, collect, and return 
    a list of 'City' objects."""
    # Open the file, expected to be in the same directory.
    with open(path_name) as f:
        # Instantiate a reader object
        rowreader = csv.reader(f)
        # iterate past the header row, which is not ueful.
        rowreader.__next__()
        # Iterate over remaining rows, 
        for row in rowreader:
            # creating a City object for each, and collecting
            # in the list 'cities'
            cities.append(City(*(get_required_data(row))))
    # 'with' structure automatically closes file.        
    return cities


def __main__():
    cities = cityreader()
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
    
    
    
def get_input():
    print("We need two pairs of lat/long coordinates.")
    print("Please enter a comma separated pair of latitude, longitude.")
    print("Example: 45, -100")
    corner_1 = input("~~~~~~~~~> ")
    validate_input(corner_1)
    print("Thanks. Please enter one more pair.")
    print("Example: 32, -120")
    corner_2 = input("~~~~~~~~~> ")


# In[9]:


# get west longitude (more negative)
# get east longitude (less negative)
# get north latitide (bigger)
# get south latitude (smaller)

def in_box(lat1, lon1, lat2, lon2 city):
    """Report whether a city's lat/lon is within a box 
    defined by north and south latitudes, and east and west
    longitude."""
    lat = city.lat
    lon = city.lon
    
#     return (lat, lon)
#     return type(lat)
    return (n > lat > s)
#             and (w > lon > e))

# test
my_city = cities[0]
my_lat_lon = (my_city.lat, my_city.lon)
my_lat_lon

in_box(90, -130, my_city)


# In[7]:


def validate_input(to_check):
    """Make sure that input is a string that can be parsed
    into two numbers.
    TODO: specific error messages
    TODO: range limits"""


    maybe_valid = [mv for mv in to_check.split(',')]
    # test that exactly two data were entered
    try:
        assert len(maybe_valid) == 2
    except:
        print("Please enter two numbers.")
    
    lat, lon = maybe_valid
    # test that the first value can be converted to a float
    try:
        lat = float(lat)
    except:
        print(f'Could not ensure {lat} is a floating point number.')    
        print("Please enter two numbers.")

    # test that the second value can be converted to a float    
    try:
        lon = float(lon)
    except:
        print(f'Could not ensure {lon} is a floating point number.')
        print("Please enter two numbers.")
        
    # test that the latitude entered is valid    
    try:
        -90 < lat < 90
    except:
        print(f'Latitude must be between -90 and 90.')
        
    # test that the longitude entered is valid    
    try:
        -180 < lon < 180
    except:
        print(f'Longitude must be between -90 and 90.')


        


