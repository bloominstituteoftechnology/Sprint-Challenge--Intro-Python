# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
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
class Vehicle:
    pass

class GroundVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class FlightVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

# class Vehicle:
#     def __init__(self, name, category, color):
#         self.name = name
#         self.category = category
#         self.color = color

#     def __str__(self):
#         output = f"This is the Vehicle class: {self.name}"
#         return output

# class FlightVehicle(Vehicle):
#     def __init__(self, name, category, color, size, weight):
#         super().__init__(name, category, color)
#         self.size = size
#         self.weight = weight

#     def __repr__(self):
#         return f"{self.name}, {self.category}, {self.color}, {self.size}"

# class Starship(FlightVehicle):
#     def __init__(self, name, category, color, size, weight, gravity):
#         super().__init__(name, category, color, size, weight)
#         self.gravity = gravity

#     def __repr__(self):
#         return f"{self.name}, {self.category}, {self.color}, {self.size}, {self.gravity}, {self.weight}"

# class Airplane(FlightVehicle):
#     def __init__(self, name, category, color, size, brand, capacity, weight):
#         super().__init__(name, category, color, size, weight)
#         self.capacity = capacity
#         self.brand = brand

#     def __repr__(self):
#         return f"{self.name}, {self.category}, {self.color}, {self.size}, {self.brand},  {self.weight}"

# class GroundVehicle(Vehicle):
#     def __init__(self, name, category, color, seat_max, brand):
#         super(name, category, color)
#         self.seat_max = seat_max
#         self.brand = brand

#     def __repr__(self):
#         return f"{self.name}, {self.category}, {self.color}, {self.seat_max}, {self.brand}"


# class Car(GroundVehicle):
#     def __init__(self, name, category, color, seat_max, brand, music_capability ):
#         super(name, category, color, seat_max, brand)
#         self.music_capability = music_capability

#     def __repr__(self):
#         return f"{self.name}, {self.category}, {self.color}, {self.seat_max}, {self.brand}, {self.music_capability}"

# class Motorcycle(GroundVehicle):
#     def __init__(self, name, category, color, seat_max, brand, speed_limit):
#         super(name, category, color)
#         self.speed_limit = speed_limit

#     def __repr__(self):
#         return f"{self.name}, {self.category}, {self.color}, {self.seat_max}, {self.brand}, {self.speed_limit}"
