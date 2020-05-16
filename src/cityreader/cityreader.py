# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


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

from city import make_city, in_range
from load_csv import load_csv

def cityreader(file='cities.csv'):
    cities = []
    source = load_csv(file, delimiter=',')

    for row in source.data:
        cities.append(
            make_city(
            columns=source.columns,
            row=row
            )
        )
    return cities


# TODO Get latitude and longitude values from the user

def cityreader_stretch(cities, lat1, lon1, lat2, lon2):
  # within will hold the cities that fall within the specified region
  within = []
  for city in cities[0:5]:
      if in_range(city, lat1, lon1, lat2, lon2):
          within.append(city)
  return within


if __name__ == "__main__":
    # Print the list of cities (name, lat, lon), 1 record per line.
    cities = cityreader()
    [print(city) for city in cities[0:5]]
    print('Stretch')
    print(cityreader_stretch(cities, 27, -77, 47, -122))

