# 1.	Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий
# делитель (НОД) двух чисел. Вычислите и напечатайте наибольший общий делитель
#  для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.

from math import gcd
from functools import reduce

lst = []

while True:
    num = input('Введите число: ')
    if num == '':
        break
    lst.append(int(num))

print('Общий делитель: ' + str(reduce(gcd, lst)))