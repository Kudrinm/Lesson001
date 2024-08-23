class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False
class Plant:
    def __init__(self, name):
        self.edible = True
        self.name = name
class Mammal(Animal):
    def eat(self, food):
        if food.edible == False:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Predator(Animal):
    pass
class Flower(Plant):
   edible = True

class Fruit(Plant):
    edible = True



