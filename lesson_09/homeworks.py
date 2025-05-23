#homework_08

def summ_numbers(numbers):
    try:
        return sum(map(lambda x: int(x.strip()), numbers.split(',')))
    except ValueError:
        return "Не можу це зробити"

numbers = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3', '23,44,5', 'amalia12', '23,4,7.8']
for num_list in numbers:
    print(summ_numbers(num_list))

#homework_07

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


"""  Написати функцію, яка обчислює суму двох чисел.
"""
def pair_sum(number_1:int, number_2:int):  # рахує суму двох чисел
    return number_1 + number_2

result = pair_sum(234,66)
print(f"Сума двoх чисел дорівнює {result}")




