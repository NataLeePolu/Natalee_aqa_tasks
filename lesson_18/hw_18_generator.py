"""1.Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
2.Створіть генератор, який генерує послідовність Фібоначчі до певного числа N."""

def pair_numbers_generator(n):
    count = 0
    while count <= n:
        yield count
        count += 2

for num in pair_numbers_generator(135):
    print(num)


def fibonacci_generator(r):
    a, b = 0, 1
    while a <= r:
        yield a
        a, b = b, a + b


fib = fibonacci_generator(168)

while True:
    try:
        print(next(fib))
    except StopIteration:
        print("Iterator finished")
        break