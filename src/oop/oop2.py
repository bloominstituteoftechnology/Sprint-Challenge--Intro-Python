# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    """ 
    This is a class to hold a ground vehicle's information. 
      
    Attributes
    ----------
    num_wheels : int
        The number of wheels on the vehicle.
      
    Methods
    -------
    drive():
        prints the sound the vehicle makes.
    """
    def __init__(self, num_wheels=4):
        """ 
        The constructor for the GroundVehicle class. 
  
        Parameters
        ----------
        num_wheels : int
            The number of wheels on the vehicle (default is 4).  
        """
        
        self.num_wheels = num_wheels

    def drive(self):
        """
        prints the sound the vehicle makes.
        """
        return "vroooom"


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    """ 
    This is a class to hold a motorcycle's information. 
      
    Attributes
    ----------
    num_wheels : int
        The number of wheels on the motorcycle.
      
    Methods
    -------
    drive():
        prints the sound the motorcycle makes.
    """    
    
    def __init__(self, num_wheels=2):
        """ 
        The constructor for the Motorcycle class. 
  
        Parameters
        ----------
        num_wheels : int
            The number of wheels on the motorcycle (default is 2).  
        """        
        super().__init__(num_wheels)

    def drive(self):
        """
        prints the sound the motorcycle makes.
        """
        return 'BRAAAP!!'


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for vehicle in vehicles:
    print(vehicle.drive())
