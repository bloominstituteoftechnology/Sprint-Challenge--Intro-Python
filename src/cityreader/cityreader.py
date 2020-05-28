import csv

class City():

    def __init__(self,name,lat,lng):
        self.name = name
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lng}" 

cities = []

with open(r'cities.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        cities.append(City(row[0], row[3], row[4]))

for city in cities:
    print("{}, {}, {}".format(city.name, city.lat, city.lon))