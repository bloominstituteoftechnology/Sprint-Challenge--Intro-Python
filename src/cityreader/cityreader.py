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
cities = []

class City:
    def __init__(self, n, sn, cn, lat, lng, p, d, tz, z):
        self.name = n;
        self.state_name = sn;
        self.country_name = cn;
        self.lat = float(lat);
        self.lng = float(lng);
        self.population = int(p);
        self.density = int(d);
        self.timezone = tz;
        self.zips = z;
    def __repr__(self):
        return "(" + self.name + ", " + str(self.lat) + ", " + str(self.lng) + ")";
    def __str__(self):
        return self.__repr__();
        
def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    f = open("cities.csv",'r');
    l = f.readline();#ignore header;
    l = f.readline();
    while(l): #each line is one city object;
        obj = l.split(",");
        cities.append(City(obj[0],obj[1],obj[2], obj[3], obj[4], obj[5], obj[6], obj[7], obj[8].split(" ")));
        try:
            pass;
        except:
            print("could not read line: \n" + l);
        l = f.readline();
	f.close();
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []
  slat = lat1 if lat2 > lat1 else lat2;
  slon = lon1 if lon2 > lon1 else lon2;
  #slon and slat represent the top left corner of our box, so we need cordnate values that are >= both this x and this y
  import math;
  #now we need the bottom corner (the reson we do it this way is so we can garrentee that slat is always the smallest corner and elat is the lowest corner
  
  elat = lat1 if lat2 < lat1 else lat2;
  elon = lon1 if lon2 < lon1 else lon2;

  #well save some time if we know our center and our longest side;
  dlat = elat-slat; #remember we already made e lat the greater one so no abs needed
  dlon = elon-slon;
  
  dist = math.pow(dlat,2) if dlat > dlon else math.pow(dlon,2);
  #note this is our c^2 of the a^2 + b^2 = c^2;

  clat = elat-(dlat/2);
  clon = elon-(dlon/2);

  #now time for a messy if statement, we need to see if any point in our cities object
  #is less than the farthest point (elat,elon) but greater than our nearest point(slat,slon)
  for c in cities:
      #this is very slow way of doing this, because our points arent spacially sorted (this is called a brute force method
      #but we will optimize this slightly with a quick distance test, we know that a circle of the longest length of a rectangle
      #whos diamater is is that same length and whos center is the center of the rectangle contains all space of that rectangle + roughly 1/3 extra
      #this 1/3 rule is based on a square as a rectangle it would be based on the poportion of the large size to the short size
      #as these deviate so does the 1/3 rule becoming larger. The reson for testing a circle first is its a much faster call then a aabb test. [Axis Aligned Bounding Box]
    #now to do a distance test on a circle we just need to know the distance from the 2 points, this test is very easy to do because of the paraprium theorum (that a^2 + b^2 thing :P
      #we find the distance along each axis to sad point and if that squared distance is > then our sqared max they dont exist in this circle
      if(math.pow((c.lat - clat),2) + math.pow(c.lng-clon,2) > dist):
      
          continue;
      #now we get to some nasty checking calls
      if(c.lat >= slat and c.lat <= elat and c.lng >= slon and c.lng <= elon):
          within.append(c);
  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within

if(__name__ == "__main__"):
    while(True):
        try:
            p1 = "".join(input("Enter lat1, lon1").split(" ")).split(",");
            p2 = "".join(input("Enter lat1, lon1").split(" ")).split(",");
            if(len(p1) < 2 or len(p2) < 2):
                throw
            print(cityreader_stretch(float(p1[0]),float(p1[1]),float(p2[0]),float(p2[1]),cities));
            break;
        except:
            print("please try again with commons seperating values");
