#Multiple inheritance
#parent classes
class Animal:
    def __init__(self, name):
        print(f"{name} is an animal.")
        super().__init__(name)

class HatesWaterBaths:
    def __init__(self, name):
        print(f"{name} hates getting a water bath.")
        super().__init__(name)

class LoveSunBaths:
    def __init__(self,name):
        print(f"{name} loves laying in the sun.")

#child class
class Cat(Animal, HatesWaterBaths, LoveSunBaths):
    def __init__(self, name):
        print(f"{name} is a cat.")
        super().__init__(name)

#----end class definitions-------

cat = Cat("Pandemica")