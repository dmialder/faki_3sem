class Animal():
    name = None
    age = None
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_description(self):
        return "this is animal"


# object of class zebra takes name, age and description
class Zebra(Animal):
    name = None
    age = None
    if_I_was_Zebra = None

    def __init__(self, name, age, if_I_was_Zebra):
        super().__init__(name, age)
        self.if_I_was_Zebra = if_I_was_Zebra
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_description(self):
        return self.if_I_was_Zebra
        

# object of class dolphin takes name, age and description
class Dolphin(Animal):
    name = None
    age = None
    if_I_was_Dolphin = None
    
    def __init__(self, name, age, if_I_was_Dolphin):
        super().__init__(name, age)
        self.if_I_was_Dolphin = if_I_was_Dolphin
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_description(self):
        return self.if_I_was_Dolphin


#--------------------------------------------------------------
if_I_was_Dolphin = "I would not study maths"
if_I_was_Zebra = "I would count my strips"

dolphin = Dolphin("Micky", 26, if_I_was_Dolphin)
zebra = Zebra("Ricky", 19, if_I_was_Zebra)

print(dolphin.get_description())
print(zebra.get_description())
