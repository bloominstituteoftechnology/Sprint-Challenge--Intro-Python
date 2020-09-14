import pandas as pd #was going to try pd.read_csv but decided to google first and used open csv function
import csv

class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

# Google
# https://docs.python.org/3/library/csv.html
# csvreader.__next__()
#     Return the next row of the reader’s iterable object as a list (if the object was returned from reader()) or a
#     dict (if it is a DictReader instance), parsed according to the current dialect. Usually you should call this as next(reader).

# https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module

cities = []

def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # Ensure that the lat and lon valuse are all floats
    # For each city record, create a new City instance and add it to the
    # `cities` list
    with open('cities.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        next(reader)
        for row in reader:
            cities.append(City(row[0], float(row[3]), float(row[4])))
        return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c.name, c.lat, c.lon) # needed to call each item separately to print.
    # print(c)
    # returns:
    # <test.City object at 0x7fbcb8b45bd0>