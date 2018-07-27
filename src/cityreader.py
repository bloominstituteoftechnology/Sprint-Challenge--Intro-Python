# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

# TODO

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

class City():
    def __init__(self,city,state_name,county_name,lat,lng,population,density,timezone,zips):
        self.name = city
        self.state_name = state_name
        self.county_name = county_name
        self.latitude = lat
        self.longitude = lng
        self.population = population
        self.density = density
        self.timezone = timezone
        self.zips = zips.split(' ')

    def __repr__(self):
        return "<City: %s, %f, %f>" % (self.name, self.latitude, self.longitude)


            
# for row in reader:
#     print(row['city'], row['lat'], row['lng'])

cities = []

# TODO

# Print the list of cities (name, lat, lon), 1 record per line.
with open('cities.csv', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    my_arr = [row for row in reader]
    # remove the top row from the list
    my_arr.pop(0)
    for city in my_arr:
        cities.append(City(city[0],city[1],city[2],float(city[3]),float(city[4]),city[5],city[6],city[7],city[8]))


# TODO

city_list = [''.join(['Name:   ' + city.name, '\nLat: '+ str(city.latitude), '\tLon: '+ str(city.longitude)+'\n']) for city in cities]
print('\n'.join(city_list))

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