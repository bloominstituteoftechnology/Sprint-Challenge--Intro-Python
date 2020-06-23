class City():
    def __init__(
        self,
        city,
        lat,
        lng,
        state_name=None,
        county_name=None,
        population=None,
        density=None,
        timezone=None,
        zips=None):
        self.name = city
        self.state_name = state_name
        self.county_name = county_name
        self.lat = float(lat)
        self.lng = float(lng)
        self.population = population
        self.density = density
        self.timezone = timezone
        self.zips = zips

    def __repr__(self):
        return f"<City: {self.name}>"


def make_city(columns, row):
    assert len(columns) == len(row), "Length names must equal data length"
    city_kwargs = {}
    for index, key in enumerate(columns):
        city_kwargs.update({key: row[index]})
    return City(**city_kwargs)


def in_range(city, lat1, lon1, lat2, lon2):
    lats = sorted([lat1, lat2])
    lngs = sorted([lon1, lon2])
    # print(lats, lngs)
    if (lats[0] <= city.lat <= lats[1]) and \
            (lngs[0] <= city.lng <= lngs[1]):
        return True
    return False