class City():
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        return
    def __str__(self):
        return f'City("{self.name}", {self.lat}, {self.lon})'
