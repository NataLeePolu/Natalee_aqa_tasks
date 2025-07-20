"""1.Напишіть декоратор, який логує аргументи та результати викликаної функції.
2.Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції."""


import logging
#Decorator1
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_arguments_and_result(current_func):
    def wrapper(*args, **kwargs):
        logging.info(f"Виклик функції '{current_func.__name__}' з аргументами: args={args}, kwargs={kwargs}")
        result = current_func(*args, **kwargs)
        logging.info(f"Функція '{current_func.__name__}' повернула: {result}")
        return result
    return wrapper

@log_arguments_and_result
def calculate_sum(*numbers):
    return sum(numbers)


@log_arguments_and_result
def greet(name="Ганна"):
    return f"Привіт, {name}!"

calculate_sum(1,45,35,56,-23,345)
greet(name="Андрій")


# Decorator2

def log_with_errors(func):
    def wrapper(*args, **kwargs):
        try:
            print(f"[CALL] {func.__name__}({args}, {kwargs})")
            result = func(*args, **kwargs)
            print(f"[SUCCESS] Result: {result}")
            return result
        except Exception as e:
            print(f"[ERROR] {func.__name__} з аргументами {args}, {kwargs} викликало помилку: {e}")

    return wrapper

@log_with_errors
def divide(a, b):
    return a / b

divide(10, 2)
divide(35, [3,3])
divide(10, 0)
divide(10, "аваа")

