
class City():
  def __init__(self, name, lat, lon):
    self.name = name 
    self.lat = lat
    self.lon = lon 


def cityreader(filename = 'cities.csv'):
    import csv


    cities = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        list_thing = [index for index, column  in enumerate(next(csvreader)) if column in ['city', 'lat', 'lng']]
        for row in csvreader:
            cities.append(City(name = row[list_thing[0]]
            , lat = float(row[list_thing[1]])
            , lon = float(row[list_thing[2]])
            ))

    return cities

cities = cityreader('cities.csv')


for c in cities:
    print(c.name, c.lat, c.lon)
