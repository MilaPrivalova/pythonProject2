
# 3.	Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# lst_new = []
# [lst_new.append(i) for i in lst if i not in lst_new]
# print(f"Список неповторяющихся элементов: {lst_new}")

# 4.	Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

from random import randint
k = int(input('Введите число k - '))
s = []
f = open('file.txt', 'w')
for i in range(k, -1, -1):
    if i > 0:
        a = randint(0, 100)
        if a != 0:
            s.append(f'{a} * x ^ {i} + ')
    elif i == 0:
        a = randint(0, 100)
        if a != 0:
            s.append(f'{a} = 0')
        else:
            s.append('= 0')
f.writelines(s)
f.close()