# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._attack = 50
        self._experience = 0
    
    def attack(self, target):
        super().attack(target)

