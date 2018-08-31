# Write classes for the following class hierarchy:
#
#             [Vehicle]         
#    |                       |
#    v                       v
# [GroundVehicle]         [FlightVehicle]                       
#   |       |               |       |
#   v       v               v       v
# [Car]  [Motorcycle]   [Airplane]  [Starship]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: #Base class
    pass

class GroundVehicle(Vehicle): #Secondary class
    pass

class Car(GroundVehicle): #Tertiary class
    pass

class Motorcycle(GroundVehicle): #Tertiary class
    pass



class FlightVehicle(Vehicle): #Secondary class
    pass

class Airplane(FlightVehicle): #Tertiary class
    pass

class Starship(FlightVehicle): #Tertiary class
    pass