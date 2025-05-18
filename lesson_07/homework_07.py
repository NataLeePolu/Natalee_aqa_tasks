# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)

# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def pair_sum(number_1:int, number_2:int):  # рахує суму двох чисел
    return number_1 + number_2

result = pair_sum(234,66)
print(f"Сума двoх чисел дорівнює {result}")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_of_list(*args:int|float): # рахує середнє арифметичне списку чисел
   if not args:
       return None
   return sum(args) / len(args)

average = average_of_list(234,66,5,6,7,8,8,9)
if average is not None:
    print(f'Середнє арифметичне дорівнює {average}')
else:
    print(f"Список чисел порожній")

# # task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text): # приймає рядок та повертає його у зворотному порядку
    if not text:
        return None
    return text[::-1]

string = reverse_string("The sun shines brightly!")

if string is not None:
    print(f'Рядок у зворотньому порядку: "{string}"')
else:
    print("Рядок порожній.")

# # task 5
# """  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
# """
def longest_word(words: list[str]):  # приймає список слів та повертає найдовше слово у списку
    if not words:
        return None
    max_length = max(len(word) for word in words)
    return [word for word in words if len(word) == max_length]

words = ['The','sun','shines','brightly', 'but', 'you', 'can', 'get', 'sunburnt']
printed_word = longest_word(words)
print(f'Найдовше слово в списку буде "{printed_word}"')


# # task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# """  Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.
# """

#  task 7

""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
def count_h(text): # рахує скільки разів зустрічається літера 'h'
    return text.lower().count("h")

text = "The sun shines brightly!"
count =  count_h(text)
print(f"Літера \"h\" зустрічається в тексті {count} разів")

# task 8
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
def words_upper(text):
    words_row = text.split() # розбиває текст на окремі слова
    count = 0
    for every_word in words_row:
        words_upper = every_word.strip(".,;\"'()?!") # очищає слова від розділових знаків
        if words_upper and words_upper[0].isupper(): # перевіряє чи перша літера кожного слова велика
            count += 1 # рахує такі слова
    return count
text = "The sun is shining brightly! Clouds in the sky in the shape of strange animals."
count_words_upper = words_upper(text)
print(f"В тексті {count_words_upper} слів починається з великої літери")

# task 9
""" Розділіть змінну text по кінцю речення.
Збережіть результат у змінній splited_text
"""
import re
def sentances(text):
    if text is None:
        return None
    return re.split(r'[.!?]\s*', text.strip()) # розділяємо речення по символам закінчення речення

text = "The sun is shining brightly! Clouds in the sky in the shape of strange animals."
splited_text = [s for s in sentances(text) if s]
print(splited_text)

# task 10

""" Виведіть друге речення з text.
Перетворіть рядок у нижній регістр.
"""
import re

def lower_sentance(text):
     if text is None:
         return None  # якщо тексту нема повертає None
     splited_text = [s for s in re.split(r'[.!?]\s*', text.strip()) if s] # розділяє текст на речення
     if len(splited_text) > 1:
         return splited_text[1].lower() # із списку вибирає друге та перетворює його на нижній регістр
     else:
         return None # якщо другого речення нема, повертає None

text = "The sun is shining brightly! Clouds in the sky in the shape of strange animals."
lower = lower_sentance(text)
print(lower)







