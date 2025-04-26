# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()



text_count = set({char for word in input("print something to count: ").split() for char in word})
print(text_count)
if len(text_count) > 10:
    print(True)
else:
    print(False)