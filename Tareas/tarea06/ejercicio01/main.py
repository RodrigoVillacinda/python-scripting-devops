#!/usr/bin/env python3

class Person:
    def __init__(self, weight, height):
        self._weight = weight
        self._height = height

        def getWeight(self):
            return self._weight
        
        def setWeight(self):
            self._weight = weight

        def delWeight(self):
            del self._weight

        def getHeight(self):
            return self._height
         
        def setHeight(self):
            self._height = height

        def delHeight(self):
            del self._height

        weight = property(getWeight, setWeight, delWeight) 
        height = property(getHeight, setHeight, delHeight)

    def BMI_Values(self):
        return self._weight / self._height ** 2

p1 = Person(75, 2)
print(p1.BMI_Values())
