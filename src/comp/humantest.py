class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

Marc = Human('Marco Polo', 23)
James = Human('James Smith', 93)
arr = [Marc, James]

print(type(Marc))
print(Marc.name[1])
print(arr)
