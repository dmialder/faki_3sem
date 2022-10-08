class Mother:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return " ".join(["This is mother", "\n", "My name is", self.name, "\nI am", self.age, "years old\n"])

class Daughter(Mother):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def __str__(self):
        return " ".join(["This is daughter", "\n", "My name is", self.name, "\nI am", self.age, "years old", "\n",
        "I go to", self.school, "school"])

mother = Mother("Jane", "35")
daughter = Daughter("Lucie", "15", "high")
print(mother)
print(daughter)