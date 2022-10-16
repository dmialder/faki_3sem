import math
from tkinter import N
"""Class has methods that override __add__, __sub__, __mul__ and __abs__"""

class Vector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        _new_x = self.y * other.z - self.z * other.y
        _new_y = self.x * other.z + self.z * other.x
        _new_z = self.x * other.y - self.y * other.x
        return Vector(_new_x, -_new_y, _new_z)
    
    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    @classmethod
    def constructor(cls, inp):
        return cls(*inp.split(','))
    

    def __str__(self):
        return f"x = \t{self.x}\ny = \t{self.y}\nz = \t{self.z}"


def task_2(vectors, num_of_nums):
    
    max_length = 0
    max_length_vector = Vector(0, 0, 0)

    for i in range(num_of_nums):    
        if abs(vectors[i]) > max_length:
            max_length_vector = vectors[-1]

    return max_length_vector


def task_3(vectors, num_of_nums):
    sum_x = 0
    sum_y = 0
    sum_z = 0
    for item in vectors:
        sum_x += item.x
        sum_y += item.y
        sum_z += item.z
    return Vector(sum_x/num_of_nums, sum_y/num_of_nums, sum_z/num_of_nums)


num_of_nums = int(input())
vectors = []
for i in range(num_of_nums):
    vectors.append(Vector.constructor(input()))


print(task_2(vectors, num_of_nums))
print(task_3(vectors, num_of_nums))