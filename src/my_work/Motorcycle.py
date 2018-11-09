class Motorcycle:
    def __init__(self, name):
        self.name = name
        
    def motorcycle_sound(self, sound):
        if sound == True:
            print("BRAAP!!")
        else:
            print("That's not the sound a motorcycle makes.")