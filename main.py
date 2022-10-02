# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

 х = int(input("Введите число:"))
 sum = 0
 while х > 0:
 number = х % 10
 sum = sum + number
 х = х // 10
 print("Сумма цифр =", sum)

#2.Напишите программу, которая принимает на вход число N и выдает набор произведений
# чисел от 1 до N.

number = int(input('введите число N'))
count = 1
sum = 1
while count <= number:
   for i in range(1, number+1):
        sum = sum*i#       print(sum)
       count += 1

#3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def f(n):
    sum = 0
    list = {i:((1+1/i)**i)
    for i in range(1,n+1)}
   for i in list:
       sum += list.get(i)
    print('sum =',round(sum,2))
    return {i:((1+1/i)**i) for i in range(1,n+1)}
 n = int(input("Введите кол-во чисел в последовательности: "))
 print(f(n))


#4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.



from random import randint

n = int(input('Введите число: '))
listnum = []
for i in range(n):
   listnum.append(randint(-n, n))
print(listnum)
for i in range(-n, n+1):
    listnum.append(i)
res = listnum[n] * listnum[-n]
print(res)

# 5.Реализуйте алгоритм перемешивания списка.
import random
list = [0,1,2,3,4,5,6,7]
print ("Начальный список: " + str(list))
for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
print ("Перемешанный список: " +  str(list))