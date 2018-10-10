# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
import csv

# TODO
class City:
    def __init__(self, name, latitude, longitude):
        self.name=name
        self.lat=lat
        self.lon=lon

    # Incorrect >>>
    # def read(self):
    #     with open('cities.csv') as csvfile:
    #         readCSV = csv.reader(csvfile, delimiter=',')
    #         for row in readCSV:
    #             print(row)
    #             print(row[0])
    #             print(row[0],row[3],row[4],)
    # Incorrect ^^^^

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



 with open('cities.csv', newline="") as csvfile:
            cityreader= csv.reader(csvfile, delimiter=',', quotechar='|')
            passedHeader= False
            for row in cityreader:
                if passedHeader:
                  cities.append(City(row[0],row[3],row[4]))
                else:
                    passedHeader= True

# TODO

# Print the list of cities (name, lat, lon), 1 record per line.



for city in cities:
    print(f'({city.name}, {city.lat}, {city.lon})')

# TODO

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

# solution:

# latlon1Valid= False
# latlon2Valid= False

# while not latlon1Valid:
#     latlon1= input('Enter lat1, lon1:')
#     latlon1list=latlon1.split(',')
#     if len(latlon1list== 2:
#         lat1= float(latlon1list[0])
#         lon1= float(latlon1list[1])
#         latlon1Valid= True
#     else:
#         print('Invalid input')

# while not latlon2Valid:
#     latlon2= input('Enter lat2, lon2:')
#     latlon2list=latlon2.split(',')
#     if len(latlon2list== 2:
#         lat2= float(latlon1list[0])
#         lon2= float(latlon1list[1])
#         latlon2Valid= True
#     else:
#         print('Invalid input')

# latMin=min(lat1, lat2)
# latMax= max(lat1, lat2)
# lonMin= min(lon1, lon2)
# lonMax= max(lon1, lon2)

# print(f'{latMin}, {latMax}, {lonMin}, {lonMax}')

# for city in cities:
#     if city.lat>= latMin and city.lat<= latMax \
#         and city.lon>= lonMin and city.lon <=


# alternate solution:
# lat1, lon1= [float(v) for v in input("Enter lat1, lon1: ").split(',')]
# lat2, lon2= [float(v) for v in input("Enter lat1, lon1: ").split(',')]

# if lat2< lat1:
#     lat1, lat2=lat2, lat1 ---swap

# if lon2< lon1:
#     lon1, lon2=lon2, lon1 ---swap

# Filter