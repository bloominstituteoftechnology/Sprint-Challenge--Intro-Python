## `oop1.py`: class hierarchies
- [ ] [Vehicle]
-------------------------------------
- [ ] [Vehicle]->[GroundVehicle]
- [ ] [GroundVehicle]->[Car]
- [ ] [GroundVehicle]->[Motorcycle]
-------------------------------------
- [ ] [Vehicle]->[FlightVehicle]
- [ ] [FlightVehicle]->[Starship]
- [ ] [FlightVehicle]->[Airplane]
-------------------------------------

## `oop2.py`: subclassing and method overriding
- [ ] GroundVehicle class, add method drive() that prints "vroooom".
- [ ] Also change it so the num_wheels defaults to 4 if not specified when the object is constructed.
- [ ] Subclass Motorcycle from Vehicle.
- [ ] Make it so when you instantiate a Motorcycle, it automatically sets the number of wheels to 2 by passing that to the constructor of its superclass.
- [ ] Override the drive() method in Motorcycle so that it prints "BRAAAP!!"
- [ ] Go through the vehicles list and call drive() on each.
-------------------------------------
## `comp.py`: list comprehensions
- [ ] Starts with D
- [ ] Ends with e:
- [ ] Starts between C and G, inclusive
- [ ] Ages plus 10
- [ ] Name hyphen age
- [ ] Names and ages between 27 and 32
- [ ] All names capitalized
- [ ] Square root of ages
-------------------------------------
## `cityreader.py`: modules and CSV file reading
- [ ] Create a class to hold a city location. Call the class "City". 
- [ ] It should have fields for: (name, latitude, longitude)
- [ ] Use Python's built-in "csv" module to read this file so that each record is imported into a City instance.
    * Store the instances in the "cities" list.
    * Hint: the first line of the CSV is header that describes the fields --this should not be loaded into a City object.
- [ ] Print the list of cities (name, lat, lon), 1 record per line.
## `cityreader.py`: Stretch
- [ ] Allow the user to input two points, each specified by latitude and longitude.
- [ ] These points form the corners of a lat/lon square. Output the cities that fall within this square.
-------------------------------------