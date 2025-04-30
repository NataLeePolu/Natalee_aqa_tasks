
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

numerous_list = [1,2,3,4,56,7,8,9,10,11,143,1256,32,6]
pair_numbers = []
for number in numerous_list:
    if number%2 == 0:
        pair_numbers.append(number)
print(sum(pair_numbers))