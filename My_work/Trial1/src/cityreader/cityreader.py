# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City():
    def __init__(self,lat, lon):
        self.lat = lat
        self.lon = lon
a_city = city(23,35)
print(a_city)
#that f string thing


#DS approach?
df = pd.read_csv ("cities.csv", skiprows = )
# probably wont work how they intend

#From python-Intro-1

fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.close()

#and that concludes my current time






# what was here
cities = []

def cityreader(cities=[]):

    return cities

cityreader(cities)

for c in cities:
    print(c)


"""
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
#find that working with matts folder

# TODO Implement the functionality to read from the 'cities.csv' file
# For each city record, create a new City instance and add it to the
# `cities` list

# Print the list of cities (name, lat, lon), 1 record per line.


"""
