class House:
    houses_history = []
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('No floor')
        else:
            for n in range(1, new_floor+1):
                print(n)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        if isinstance(other, House):

            return self.number_of_floors < other.number_of_floors
        return False
    def __le__(self, other):
        if isinstance(other, House):

            return self.number_of_floors <= other.number_of_floors
        return False
    def __gt__(self, other):
        if isinstance(other, House):

           return self.number_of_floors > other.number_of_floors
        return False
    def __ge__(self, other):
        if isinstance(other, House):

            return self.number_of_floors >= other.number_of_floors
        return False
    def __ne__(self, other):
        if isinstance(other, House):

          return self.number_of_floors != other.number_of_floors
        return False
    def __add__(self, value):
        if isinstance(value, int):

            return House(self.name, self.number_of_floors+value)
        return self
    def __radd__(self, other):
        return self.__add__(other)
    #    self.number_of_floors += value.numbers_of_floors
    def __iadd__(self, other):
        self.number_of_floors += other

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super(House, cls).__new__(cls)
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории"')
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

