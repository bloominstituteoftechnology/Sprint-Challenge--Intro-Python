# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        pass

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples
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
    import csv
    firstline = True
    with open("cities.csv") as csvfile:
        citycsv = csv.reader(csvfile, delimiter=",")
        for row in citycsv:
            if firstline:  # Skip first row.
                firstline = False
                continue
            cities.append(City(row[0], float(row[3]), float(row[4])))
        return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c.name, c.lat, c.lon)

# STRETCH GOAL!

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

lat1, lon1 = input("Enter lat1,lon1:").split(",")
lat2, lon2 = input("Enter lat2,lon2:").split(",")


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []
    lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)
    big_lat = max(lat1, lat2)
    lil_lat = min(lat1, lat2)
    big_lon = max(lon1, lon2)
    lil_lon = min(lon1, lon2)
    for place in cities:
        if lil_lat <= place.lat <= big_lat and lil_lon <= place.lon <= big_lon:
            within.append(place)
            print(f"{place.name}: ({place.lat},{place.lon})")
    return within
