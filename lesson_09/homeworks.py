#task1

def summ_numbers(numbers):
    try:
        return sum(map(lambda x: int(x.strip()), numbers.split(',')))
    except ValueError:
        return "Не можу це зробити"

numbers = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3', '23,44,5', 'amalia12', '23,4,7.8']
for num_list in numbers:
    print(summ_numbers(num_list))


#task2

def pair_sum(number_1:int, number_2:int):  # рахує суму двох чисел
    return number_1 + number_2

result = pair_sum(234,66)
print(f"Сума двoх чисел дорівнює {result}")

#task3

def multiplication_table(number, max_abs_result=25):
    try:
        number = int(str(number).strip())
    except ValueError:
        raise ValueError("Функція приймає лише цілі числа")

    if number == 0:
        raise ValueError("Функція не приймає 0")

    multiplier = 1
    result_list = []

    while abs(number * multiplier) <= max_abs_result:
        result = number * multiplier
        result_list.append(f"{number}x{multiplier}={result}")
        multiplier += 1

    return result_list



