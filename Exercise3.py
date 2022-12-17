# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 2, 2: 2,25, 3: 3,37, 4: 2,44, 5: 2,49, 6: 2,52}

num = int(input("Введите число: "))
my_list = {}

for i in range(1, num + 1):
    my_list[i] = round(((1 + (1 / i)) ** i), 2)

summ = 0
for i in range(1, len(my_list) + 1):
    summ += my_list[i]

print(my_list)
print(f"Сумма чисел в словаре равна {summ}")