import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):

        if self.__is_valid_sides(*sides) and len(sides)==self.sides_count:
            self._sides= list(sides)
        else:
            self._sides= [1]*self.sides_count
        if self.__is_valid_color(*color):
            self._color = list(color)
        else:
            self._color= [0,0,0]
        self.filled = False
    def get_color(self):
        return self._color
    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and 0 <= r <= 255 and isinstance(g, int) and 0 <= g <= 255 and isinstance(b, int) and 0 <= b <= 255
            return True
        else:
            return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides)
    def get_sides(self):
        return self._sides
    def __len__(self):
        return sum(self._sides)
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self._sides[0] / (2*math.pi)
    def get_square(self):
        return math.pi * self.__radius **2




class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)



class Cube: