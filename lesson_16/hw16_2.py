"""Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
 Наслідуйте від нього декілька (> 2) інших фігур,
 та реалізуйте математично вірні для них методи для площі та периметру.
 Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
 та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур,
 та у циклі порахуйте та виведіть в консоль площу та периметр кожної."""
import math
from abc import ABC, abstractmethod

# Абстрактний клас фігур
class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

# Клас прямокутник, що успадковує абстрактний клас Figure
class Rectangle(Figure):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def area(self):
        return self.__a * self.__b
    def perimetr(self):
        return 2 * (self.__a + self.__b)

# Клас трикутника, що успадковує абстрактний клас Figure
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        s = (self.__a + self.__b + self.__c)/2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def perimetr(self):
        return self.__a + self.__b + self.__c

# Клас коло, що успадковує абстрактний клас Figure
class Circle(Figure):
    def __init__(self, r):
        self.__r = r
    def area(self):
        return math.pi * self.__r**2
    def perimetr(self):
        return 2*(math.pi * self.__r)

figures = [
    Circle(2),
    Triangle(3,4,5),
    Rectangle(2,5)
    ]

for figure in figures:
    area = figure.area()
    perimeter = figure.perimetr()
    print(f"Фігура \"{figure.__class__.__name__}\":")
    print(f"Площа: {area:.2f}")
    print(f"Периметр: {perimeter:.2f}")
