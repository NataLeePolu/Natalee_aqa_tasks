"""Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:
Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__."""



class Rhombus:
    def __init__(self, side, angle_a):
        setattr(self, "side", side)
        setattr(self, "angle_a", angle_a)

    def __setattr__(self, key, value):
        if key == "side":
            if value <= 0:
                raise ValueError("Сторона ромба повинна бути більшою за 0")
        elif key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут А повинен бути в межах 0–180 градусів")
            super().__setattr__("angle_b", 180 - value)
        super().__setattr__(key, value)

    def show_info(self):
        print(f"Сторона: {self.side}")
        print(f"Кут A: {self.angle_a}°")
        print(f"Кут B: {self.angle_b}°")

#перевірки
r = Rhombus(15,80)
r.show_info()

print("\nЗмінюємо кут A...\n")
setattr(r,"angle_a", 95)
r.show_info()

print("\nПеревіримо,чи може бути сторона 0...\n")
try:
    r = Rhombus(0,80)
except ValueError as e:
    print("Помилка:", e)

print("\nПеревіримо,чи може бути кут А бульше 180...\n")
try:
    r = Rhombus(5,180)
except ValueError as e:
    print("Помилка:", e)