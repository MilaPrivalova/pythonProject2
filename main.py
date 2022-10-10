
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

# from random import randint
# k  = int(input('Введите число k - '))
# s = []
# f = open('file.txt', 'w')
# for i in range(k, -1, -1):
#     if i > 0:
#        a = randint(0, 100)
#        if a != 0:
#            s.append(f'{a} * x ^ {i} + ')
#    elif i == 0:
#        a = randint(0, 100)
#        if a != 0:
#            s.append(f'{a} = 0')
#        else:
#            s.append('= 0')
# f.writelines(s)
# f.close()

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

f = open('file.txt', 'r')
numbers1 = []
for line in f:
    data = line.split()
    for i in data:
        if i.isdigit():
            i = int(i)
            numbers1.insert(0, i)
print(numbers1)

f = open('file1.txt', 'r')
numbers2 = []
for line in f:
    data = line.split()
    for i in data:
        if i.isdigit():
            i = int(i)
            numbers2.insert(0, i)
print(numbers2)

result = []
if len(numbers1) > len(numbers2):
    for i in range(1, len(numbers2)):
        if i % 2 == 0:
            result.insert(1, numbers1[i])
        else:
            result.insert(0, numbers1[i] + numbers2[i])
    for i in range(len(numbers2), len(numbers1)):
        result.insert(0, numbers1[i])
elif len(numbers1) < len(numbers2):
    for i in range(1, len(numbers1)):
        if i % 2 == 0:
            result.insert(0, numbers2[i])
        else:
            result.insert(0, numbers2[i] + numbers1[i])
    for i in range(len(numbers1), len(numbers2)):
        result.insert(0, numbers2[i])
else:
    for i in range(1, len(numbers2)):
        if i % 2 == 0:
            result.insert(0, numbers1[i])
        else:
            result.insert(0, numbers1[i] + numbers2[i])

print(result)

s = []
f = open('file2.txt', 'w')
for i in range(0, len(result)):
    if i % 2 == 0:
        s.append(f'{result[i]}')
    else:
        if result[i] == 1:
            s.append(f'*x+')
        else:
            s.append(f'*x^{result[i]}+')
s.append('=0')
f.writelines(s)
f.close()
