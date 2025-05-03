# Порахувати кількість унікальних символів в рядку. Якщо їх більше ніж 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

print(len({char for char in input("Print something to count: ")if char != " "}) > 10)
