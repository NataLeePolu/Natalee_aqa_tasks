"""Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""

class Student:
    def __init__(self, name: str, second_name: str, age: int, average_score: float):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.average_score = average_score

    def __setattr__(self, key, value):
        if key == "average_score":
            if not (0 <= value <= 100):
                raise ValueError("Середній бал має бути від 0 до 100!")
        super().__setattr__(key, value)

    def show_info(self):
        print(f"Ім'я: {self.name} {self.second_name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.average_score}")

student1 = Student("Dmytro", "Krylenko", 22, 84.5) #instance
student1.show_info()

print("\nЗмінюємо середній бал на валідне значення...\n")
student1.average_score = 89.0
student1.show_info()

print("\nЗмінюємо середній бал на невалідне значення...\n")
try:
    student1.average_score = 109.0
except ValueError as e:
    print("Помилка:", e)

