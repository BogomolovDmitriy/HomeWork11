# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def fact(arg):
    if arg == 0:
        return 1
    return fact(arg-1) * arg

num = int(input("Введите число: "))
my_list = []
for i in range(1, num + 1):
    my_list.append(fact(i))

print(my_list)