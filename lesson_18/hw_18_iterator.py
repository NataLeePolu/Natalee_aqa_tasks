"""1.Реалізуйте ітератор для зворотного виведення елементів списку.
2.Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N."""


class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value


my_list = [1, 3, 5, 6, 19, 35, 47, 456]
my_list_reversed = ReverseIterator(my_list)
while True:
    try:
        print(next(my_list_reversed))  # Тут буде StopIteration
    except StopIteration:
        print("First Iterator finished")
        break

class PairNumber:
    def __init__(self, number):
        self.number = number
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.number):
            current = self.number[self.index]
            self.index += 1
            if current % 2 == 0:
                return current
        raise StopIteration



number_list = [0, 34, 56, 35, 67, 468, 346 , -234, -34, 76]

pair_number_list = PairNumber(number_list)

while True:
    try:
        print(next(pair_number_list))  # Тут буде StopIteration
    except StopIteration:
        print("Second Iterator finished")
        break

