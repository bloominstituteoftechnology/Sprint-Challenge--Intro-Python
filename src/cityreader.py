import csv

class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

with open('cities.csv') as file:
    reader = csv.reader(file)
    city = [City(i[0], i[3], i[4]) for i in reader]

for i in city:
    print('{}, {}, {}'.format(i.name, i.latitude, i.longitude))