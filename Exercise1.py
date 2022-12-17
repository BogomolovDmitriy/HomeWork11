# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

num = (input("Введите вещественное число: "))
temp_num = num.split(",")

def summ(arg):
    summ = 0
    while arg > 0:
        summ += (arg % 10)
        arg //= 10
    return summ

my_summ = 0
if len(temp_num) == 1:
   my_summ = summ(int(temp_num[0]))
elif len(temp_num) == 2:
    my_summ = summ(int(temp_num[0])) + summ(int(temp_num[1]))
    
print(f"Сумма цифр числа {num} = {my_summ}")
