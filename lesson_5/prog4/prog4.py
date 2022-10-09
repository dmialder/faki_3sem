import random


class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age


# object of class zebra takes name, age and description
class Zebra(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
        

# object of class dolphin takes name, age and description
class Dolphin(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)


class Bird(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)
    

class Cheiroptera(Animal):
    pass


class Bat(Cheiroptera):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.wings = [Webbed()]


class Insect(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Wings:
    pass


class Feather_wing(Wings):
    pass


class Webbed_wing(Wings):
    def __init__(self):
        super().__init__()
        self.amount = 2

