class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)


p = Point(1, 2)
print(p)


name = 'marcog'
number = 42
print('%s %d' % (name, number))


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Human: %s, %d>" % (self.name, self.age)


b = Human("hilal", 33)
print(b)
print(b.__repr__())


s = 'Hello, Geeks.'
print(repr(s))
print(repr(2.0/11.0))
print(str(s))
print(str(2.0/11.0))

list = [1, 3, 4, 5, 6, 6]
l = list.__len__()
print(l)
d = list.__repr__()
print(d)


class Foo():
    def __init__(self):
        self.l = 4


foo = Foo()
repr(foo.__init__)
# print(foo)
