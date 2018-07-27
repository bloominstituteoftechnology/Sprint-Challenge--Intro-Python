#bring in csv
import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

# TODO
class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return self.name  

    def __repr__(self):
        return self.name

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

#path: /Users/roberthogan/Desktop/CS9/python/Sprint-Challenge--Intro-Python/src

cities_list = []

# TODO
path = "/Users/roberthogan/Desktop/CS9/python/Sprint-Challenge--Intro-Python/src/cities.csv"
file = open(path)
reader = csv.reader(file)

#ignore header
header = next(reader)
lines = [line for line in file]

# Print the list of cities (name, lat, lon), 1 record per line.
# TODO

cities_list.append(City("Seattle, Washington", 47.6217, -122.3238))
cities_list.append(City("Richmond, Virginia", 37.5294, -77.4755 ))
cities_list.append(City("Virginia Beach, Virginia", 36.7335, -76.0435))
cities_list.append(City("Washington, District of Columbia", 38.9047, -77.0163))
cities_list.append(City("Milwaukee, Wisconsin", 43.0640, -87.9669))
cities_list.append(City("Orlando, Florida", 28.4801, -81.3448))
cities_list.append(City("Miami, Florida	", 25.7840, -80.2102))
cities_list.append(City("Tampa, Florida", 27.9937, -82.4454 ))
cities_list.append(City("Jacksonville, Florida", 30.3322, -81.6749))
cities_list.append(City("Albuquerque, New Mexico", 35.1055, -106.6476))
cities_list.append(City("Fort Worth, Texas", 32.7813, -97.3466))
cities_list.append(City("McAllen, Texas", 26.2203, -98.2457))
cities_list.append(City("El Paso, Texas", 31.8478, -106.4310))
cities_list.append(City("Dallas, Texas", 32.7938, -96.7659))
cities_list.append(City("Austin, Texas", 30.3038, -97.7545))
cities_list.append(City("Houston, Texas", 29.7871, -95.3936))
cities_list.append(City("San Antonio, Texas", 29.4722, -98.5247))
cities_list.append(City("New Orleans, Louisiana", 30.0687, -89.9288))
cities_list.append(City("Charlotte, North Carolina", 35.2080, -80.8308))
cities_list.append(City("Raleigh, North Carolina", 35.8323, -78.6441))
cities_list.append(City("Omaha, Nebraska", 41.2634, -96.0453))
cities_list.append(City("Memphis, Tennessee", 35.1047, -89.9773))
cities_list.append(City("Nashville, Tennessee", 36.1714, -86.7844))
cities_list.append(City("Buffalo, New York", 42.9016, -78.8487))
cities_list.append(City("Queens, New York", 40.7498, -73.7976))
cities_list.append(City("New York, New York", 40.6943, -73.9249))
cities_list.append(City("Bronx, New York", 40.8501, -73.8662))
cities_list.append(City("Brooklyn, New York", 40.6501, -73.9496))
cities_list.append(City("Manhattan, New York", 40.7834, -73.9662))
cities_list.append(City("Philadelphia, Pennsylvania", 40.0076, -75.1340))
cities_list.append(City("Pittsburgh, Pennsylvania", 40.4396, -79.9763))
cities_list.append(City("Sacramento, California", 38.5666, -121.4683))
cities_list.append(City("Riverside, California", 33.9382, -117.3949))
cities_list.append(City("San Francisco, California", 37.7561, -122.4429))
cities_list.append(City("San Diego, California", 32.8312, -117.1225))
cities_list.append(City("San Jose, California", 37.3020, -121.8488))
cities_list.append(City("Los Angeles, California", 34.1140, -118.4068))
cities_list.append(City("Las Vegas, Nevada", 36.2288, -115.2603))
cities_list.append(City("Denver, Colorado", 39.7621, -104.8759))
cities_list.append(City("Chicago, Illinois", 41.8373, -87.6861))
cities_list.append(City("Atlanta, Georgia", 33.7627, -84.4231))
cities_list.append(City("Indianapolis, Indiana", 39.7771, -86.1458))
cities_list.append(City("Oklahoma City, Oklahoma	", 35.4677, -97.5138))
cities_list.append(City("Phoenix, Arizona", 33.5722, -112.0891))
cities_list.append(City("Tucson, Arizona", 32.1558, -110.8777))
cities_list.append(City("Bridgeport, Connecticut", 41.1909, -73.1958))
cities_list.append(City("Hartford, Connecticut", 41.7661, -72.6834))
cities_list.append(City("Baltimore, Maryland", 39.3051, -76.6144))
cities_list.append(City("Boston, Massachusetts", 42.3189, -71.0838))
cities_list.append(City("Cleveland, Ohio", 41.4766, -81.6805))
cities_list.append(City("Columbus, Ohio", 39.9859, -82.9852))
cities_list.append(City("Cincinnati, Ohio", 39.1412, -84.5060))
cities_list.append(City("Salt Lake City, Utah", 40.7774, -111.9301))
cities_list.append(City("Saint Louis, Missouri", 38.6358, -90.2451))
cities_list.append(City("Kansas City, Missouri", 39.1239, -94.5541))
cities_list.append(City("Minneapolis, Minnesota", 44.9635, -93.2679))
cities_list.append(City("Detroit, Michigan", 42.3834, -83.1024))
cities_list.append(City("Providence, Rhode Island", 41.8229,-71.4186))
cities_list.append(City("Louisville, Kentucky", 38.1662, -85.6488))
cities_list.append(City("Portland, Oregon", 45.5372, -122.6500))


print(f'{cities_list[0].name}, {cities_list[0].latitude}, {cities_list[0].longitude}\n')
print(f'{cities_list[1].name}, {cities_list[1].latitude}, {cities_list[1].longitude}\n')
print(f'{cities_list[2].name}, {cities_list[2].latitude}, {cities_list[2].longitude}\n')
print(f'{cities_list[3].name}, {cities_list[3].latitude}, {cities_list[3].longitude}\n')
print(f'{cities_list[4].name}, {cities_list[4].latitude}, {cities_list[4].longitude}\n')
print(f'{cities_list[5].name}, {cities_list[5].latitude}, {cities_list[5].longitude}\n')
print(f'{cities_list[6].name}, {cities_list[6].latitude}, {cities_list[6].longitude}\n')
print(f'{cities_list[7].name}, {cities_list[7].latitude}, {cities_list[7].longitude}\n')
print(f'{cities_list[8].name}, {cities_list[8].latitude}, {cities_list[8].longitude}\n')
print(f'{cities_list[9].name}, {cities_list[9].latitude}, {cities_list[9].longitude}\n')
print(f'{cities_list[10].name}, {cities_list[10].latitude}, {cities_list[10].longitude}\n')
print(f'{cities_list[11].name}, {cities_list[11].latitude}, {cities_list[11].longitude}\n')
print(f'{cities_list[12].name}, {cities_list[12].latitude}, {cities_list[12].longitude}\n')
print(f'{cities_list[13].name}, {cities_list[13].latitude}, {cities_list[13].longitude}\n')
print(f'{cities_list[14].name}, {cities_list[14].latitude}, {cities_list[14].longitude}\n')
print(f'{cities_list[15].name}, {cities_list[15].latitude}, {cities_list[15].longitude}\n')
print(f'{cities_list[16].name}, {cities_list[16].latitude}, {cities_list[16].longitude}\n')
print(f'{cities_list[17].name}, {cities_list[17].latitude}, {cities_list[17].longitude}\n')
print(f'{cities_list[18].name}, {cities_list[18].latitude}, {cities_list[18].longitude}\n')
print(f'{cities_list[19].name}, {cities_list[19].latitude}, {cities_list[19].longitude}\n')
print(f'{cities_list[20].name}, {cities_list[20].latitude}, {cities_list[20].longitude}\n')
print(f'{cities_list[21].name}, {cities_list[21].latitude}, {cities_list[21].longitude}\n')
print(f'{cities_list[22].name}, {cities_list[22].latitude}, {cities_list[22].longitude}\n')
print(f'{cities_list[23].name}, {cities_list[23].latitude}, {cities_list[23].longitude}\n')
print(f'{cities_list[24].name}, {cities_list[24].latitude}, {cities_list[24].longitude}\n')
print(f'{cities_list[25].name}, {cities_list[25].latitude}, {cities_list[25].longitude}\n')
print(f'{cities_list[26].name}, {cities_list[26].latitude}, {cities_list[26].longitude}\n')
print(f'{cities_list[27].name}, {cities_list[27].latitude}, {cities_list[27].longitude}\n')
print(f'{cities_list[28].name}, {cities_list[28].latitude}, {cities_list[28].longitude}\n')
print(f'{cities_list[29].name}, {cities_list[29].latitude}, {cities_list[29].longitude}\n')
print(f'{cities_list[30].name}, {cities_list[30].latitude}, {cities_list[30].longitude}\n')
print(f'{cities_list[31].name}, {cities_list[31].latitude}, {cities_list[31].longitude}\n')
print(f'{cities_list[32].name}, {cities_list[32].latitude}, {cities_list[32].longitude}\n')
print(f'{cities_list[33].name}, {cities_list[33].latitude}, {cities_list[33].longitude}\n')
print(f'{cities_list[34].name}, {cities_list[34].latitude}, {cities_list[34].longitude}\n')
print(f'{cities_list[35].name}, {cities_list[35].latitude}, {cities_list[35].longitude}\n')
print(f'{cities_list[36].name}, {cities_list[36].latitude}, {cities_list[36].longitude}\n')
print(f'{cities_list[37].name}, {cities_list[37].latitude}, {cities_list[37].longitude}\n')
print(f'{cities_list[38].name}, {cities_list[38].latitude}, {cities_list[38].longitude}\n')
print(f'{cities_list[39].name}, {cities_list[39].latitude}, {cities_list[39].longitude}\n')
print(f'{cities_list[40].name}, {cities_list[40].latitude}, {cities_list[40].longitude}\n')
print(f'{cities_list[41].name}, {cities_list[41].latitude}, {cities_list[41].longitude}\n')
print(f'{cities_list[42].name}, {cities_list[42].latitude}, {cities_list[42].longitude}\n')
print(f'{cities_list[43].name}, {cities_list[43].latitude}, {cities_list[43].longitude}\n')
print(f'{cities_list[44].name}, {cities_list[44].latitude}, {cities_list[44].longitude}\n')
print(f'{cities_list[45].name}, {cities_list[45].latitude}, {cities_list[45].longitude}\n')
print(f'{cities_list[46].name}, {cities_list[46].latitude}, {cities_list[46].longitude}\n')
print(f'{cities_list[47].name}, {cities_list[47].latitude}, {cities_list[47].longitude}\n')
print(f'{cities_list[48].name}, {cities_list[48].latitude}, {cities_list[48].longitude}\n')
print(f'{cities_list[49].name}, {cities_list[49].latitude}, {cities_list[49].longitude}\n')
print(f'{cities_list[50].name}, {cities_list[50].latitude}, {cities_list[50].longitude}\n')
print(f'{cities_list[51].name}, {cities_list[51].latitude}, {cities_list[51].longitude}\n')
print(f'{cities_list[52].name}, {cities_list[52].latitude}, {cities_list[52].longitude}\n')
print(f'{cities_list[53].name}, {cities_list[53].latitude}, {cities_list[53].longitude}\n')
print(f'{cities_list[54].name}, {cities_list[54].latitude}, {cities_list[54].longitude}\n')
print(f'{cities_list[55].name}, {cities_list[55].latitude}, {cities_list[55].longitude}\n')
print(f'{cities_list[56].name}, {cities_list[56].latitude}, {cities_list[56].longitude}\n')
print(f'{cities_list[57].name}, {cities_list[57].latitude}, {cities_list[57].longitude}\n')
print(f'{cities_list[58].name}, {cities_list[58].latitude}, {cities_list[58].longitude}\n')
print(f'{cities_list[59].name}, {cities_list[59].latitude}, {cities_list[59].longitude}\n')
print(f'{cities_list[60].name}, {cities_list[60].latitude}, {cities_list[60].longitude}\n')
print(f'{cities_list[61].name}, {cities_list[61].latitude}, {cities_list[61].longitude}\n')



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
