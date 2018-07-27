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
class City:
    def __init__(name, latitude, longitude):
        self.name = name

cities = []

file = open('cities.csv', newline='')
reader = csv.reader(file)
header = next(reader)
data = [row for row in ]