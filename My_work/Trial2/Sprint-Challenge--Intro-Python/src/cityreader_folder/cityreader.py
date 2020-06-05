
class City():
    def __init__(self,name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

#    def __str__(self):
#        return "{}\n=====\n{}\nValue: {}\n".format(self.lat, self.lon)


a_city = City('name', 23,35)
print(a_city)
print(a_city.name)
print(a_city.lat)
print(a_city.lon)
