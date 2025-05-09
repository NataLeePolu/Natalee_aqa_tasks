# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
# print(alice_in_wonderland)
# alice_in_wonderland = """
# "Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
# """
# alice_in_wonderland = alice_in_wonderland.replace("'","\'")
# print(alice_in_wonderland)

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)
#
# """
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
# """
# task 04
# """
# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# ське моря разом?
# """
azov = 37800
black = 436402
azov_and_black = azov+black
print(f"Площа Азовського та Чорного морів разом становить {azov_and_black} км2.")

# # task 05
# """
# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.
# """
storage_1_and_2 = 250449
storage_2_and_3 = 222950
all_storages = 375291

storage_1 = all_storages - storage_2_and_3
storage_2 = storage_1_and_2 - storage_1
storage_3 = storage_2_and_3 - storage_2
print(f"На першому складі було розміщено {storage_1} товарів, на другому складі - {storage_2} товари, а на третьому {storage_3} товари.")

# # task 06
# """
# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.
# """
month_payment = 1179
count_payment = 18
print(f"Вартість компʼютера складатиме {count_payment*month_payment} грн.")

# # task 07
# """
# Знайди остачу від діленя чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9
# """
print(f"a){8019%8}, b){9907%9}, c){2789%5}, d){7248%6}, e){7128%5}, f){19224%9}")
#
# # task 08
# """
# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн
# """
big_pizza = 274*4
middle_pizza = 2*218
juice = 4*35
cake = 1*350
water = 3*21
print(f"Для оплати замовлення Іринці знадобиться {big_pizza+middle_pizza+juice+cake+water} грн.")

# # task 09
# """
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?
# """
all_photos = 232
one_page_photos = 8
page_number = all_photos/one_page_photos
page_number_plus = all_photos%one_page_photos
if page_number_plus>0:
    print(f"Ігорю знадобиться {int(page_number+1)} сторінок.")
else:
    print(f"Ігорю знадобиться {int(page_number)} сторінок.")
#
# # task 10
# """
# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?
# """
full_distance = 1600
fuel_consumption_100 = 9
tank = 48

full_fuel_consumption = 1600/100*9
stops_count = full_fuel_consumption/48
if full_fuel_consumption%48 == 0:
    print(f"1) Родині знадобиться {int(full_fuel_consumption)} літрів бензину для подорожі.\n2) Родині доведеться робити щонайменше {int(stops_count)} зупинки для заправки.")
else:
    print(f"1) Родині знадобиться {int(full_fuel_consumption)} літрів бензину для подорожі.\n2) Родині доведеться робити щонайменше {int(stops_count+1)} зупинки для заправки.")