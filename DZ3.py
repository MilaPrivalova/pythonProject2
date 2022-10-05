# 1.	Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


#lst = [2, 3, 5, 9, 3]
#print(lst)


#def rec_sum(lst):
#    Sum = 0
#    count = 1
#    for i in range(len(lst)):
#        if i%2 != 0:

#            Sum += lst[i]
#            count = count + 1
#    return Sum

#print('Сумма элементов на нечетных позициях:', rec_sum(lst)

#2.	Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list_numbers = [2, 3, 4, 5, 6]
list_multiplication = []
last_position = len(list_numbers) - 1

for index in range(len(list_numbers)):

    if index <= last_position:
        list_multiplication.append(list_numbers[index] * list_numbers[last_position])
        last_position -= 1

print (list_multiplication)