"""
Create a class to hold a city location. Call the class "City". It should have
fields for name, lat and lon (representing latitude and longitude).

We have a collection of US cities with population over 750,000 stored in the
file "cities.csv". (CSV stands for "comma-separated values".)

In the body of the `cityreader` function, use Python's built-in "csv" module 
to read this file so that each record is imported into a City instance. Then
return the list with all the City instances from the function.
Google "python 3 csv" for references and use your Google-fu for other examples.

Store the instances in the "cities" list, below.

Note that the first line of the CSV is header that describes the fields--this
should not be loaded into a City object.
"""

import csv


class City:
    def __init__(self, name: str, lat: float, lon: float):
        """Constructor for the base City class.
        
        :param name (str) : Name of city.
        :param lat (float) : Latitude of city.
        :param lon (float) : Longitude of city.
        """
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"'{self.name} @ ({self.lat, self.lon})'"

    def __repr__(self):
        return f"<{self.name} @ ({self.lat, self.lon})>"


cities = []


def cityreader(cities: list = [], csv_file: str = "cities.csv"):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list
    # Open the cities csv using a context manager
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        # Skip header by calling the reader's `next()` method once
        header = next(reader)
        for row in reader:
            cities.append(City(row[0], float(row[3]), float(row[4])))

    return cities


cityreader(cities)

# # Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
#     print(c)

"""
STRETCH GOAL!

Allow the user to input two points, each specified by latitude and longitude.
These points form the corners of a lat/lon square. Pass these latitude and
longitude values as parameters to the `cityreader_stretch` function, along
with the `cities` list that holds all the City instances from the `cityreader`
function. This function should output all the cities that fall within the
coordinate square.

Be aware that the user could specify either a lower-left/upper-right pair of
coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
the input data so that it's always one or the other, then search for cities.
In the example below, inputting 32, -120 first and then 45, -100 should not
change the results of what the `cityreader_stretch` function returns.

Example I/O:

Enter lat1,lon1: 45,-100
Enter lat2,lon2: 32,-120
Albuquerque: (35.1055,-106.6476)
Riverside: (33.9382,-117.3949)
San Diego: (32.8312,-117.1225)
Los Angeles: (34.114,-118.4068)
Las Vegas: (36.2288,-115.2603)
Denver: (39.7621,-104.8759)
Phoenix: (33.5722,-112.0891)
Tucson: (32.1558,-110.8777)
Salt Lake City: (40.7774,-111.9301)
"""

print("Enter two pairs of latitude, longitude values, comma-separated:")
# Remove any whitespace and split on the comma
lat1, lon1 = input("Enter lat,lon:").replace(" ", "").split(",")
lat2, lon2 = input("Enter lat,lon:").replace(" ", "").split(",")
# Convert values to float
lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)


def cityreader_stretch(lat1: float, lon1: float, lat2: float, lon2: float, cities=[]):
    # Within will hold the cities that fall within the specified region
    within = []

    # Ensure lat and lon values are floats
    lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)

    # Normalize the coordinates by sorting into ascending order
    # That will result in lat1,lon1 always representing the top-right corner of the square
    lat1, lat2 = sorted([lat1, lat2])
    lon1, lon2 = sorted([lon1, lon2])

    # Go through each city and check to see if it falls within the specified coordinates.
    for city in cities:
        if lat1 <= city.lat <= lat2 and lon1 <= city.lon <= lon2:
            # print(f"{city.name}: ({city.lat}, {city.lon})")
            within.append(city)

    return within


cityreader_stretch(lat1, lon1, lat2, lon2, cities)

cityreader_stretch(45, -100, 32, -120, cities)
