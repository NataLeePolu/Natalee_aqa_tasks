# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
text = "Hello world!"
for letter in "Hello world!":
    print(text)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 4
banana = apples*4

print (apples, banana)


# task 05 == виправте назви змінних
side_one = 1
side_two = 2
side_three = 3
side_four = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = side_one+side_two+side_three+side_four
print(perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
# У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?
"""
apples = 4
pears = apples+4
plums = apples-2
print("У саду посадили", apples, "яблунь,", pears, "груш та ", plums, "слив. Усього посадили", apples+pears+plums, "дерев.")

# task 08
"""
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_temperature = 5
day_temperature = morning_temperature-10
evening_temperature = day_temperature+4
print("Температура надвечір складала", evening_temperature, "градусів.")
# task 09
"""
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys/2
theater_group_today = (boys+girls)-3
print("Сьогодні у театральному гуртку", int(theater_group_today), "дітей")

# task 10
"""
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book = 8
second_book = first_book+2
third_book = (first_book+second_book)/2
purchase = first_book+second_book+third_book
print("Якщо купити по одному примірнику книг, то вартісь покупки складатиме", purchase, "грн.")
