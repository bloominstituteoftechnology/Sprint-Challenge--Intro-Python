class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latiude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.name}, {self.latitude}, {self.longitude}"
