import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.

# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []
def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  with open("cities.csv", "r") as f:
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames

    for line in d_reader:
      cities.append(line['city'])
    return cities

class City:
  def __init__(self, name, lon, lat):
    self.name = name
    self.lon = lon
    self.lat = lat

cities = cityreader(cities)
for c in cities:
    city_instance_list = []
    with open("cities.csv", "r") as f:
        d_reader = csv.DictReader(f)
        headers = d_reader.fieldnames

        for line in d_reader:
            city_instance = City(line['city'],line['lng'],line['lat'])
            city_instance_list.append(city_instance.name)
            city_instance_list.append(city_instance.lon)
            city_instance_list.append(city_instance.lat)

print(city_instance_list)


# t = City(cityreader(cities))

# print(cityreader(cities))