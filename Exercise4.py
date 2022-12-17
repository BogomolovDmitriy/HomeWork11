# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - 
# списко на основе n, а позиции элементов lst2=[3,1].
# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

from random import randint

N = int(input("Введите положительное число: "))

my_list = []
pos_list = [2, 1]

multiply = 1

for i in range(N):
    my_list.append(randint(-N, N))

for i in range(len(pos_list)):
    multiply *= my_list[pos_list[i]]

def shuffle_list(list):
    num = len(list)
    temp_list = []
    for i in range(num):
        index = randint(0, num - 1 - i)
        temp_list.append(list[index])
        del list[index]
    return temp_list

print(f"Список из {N} элементов: {my_list}")
print(F"Произведение элементов списка на позициях {pos_list} равно {multiply}")
print(f"Список после перемешивания: {shuffle_list(my_list)}")