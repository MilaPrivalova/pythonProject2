# 1.	Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий
# делитель (НОД) двух чисел. Вычислите и напечатайте наибольший общий делитель
#  для списка натуральных чисел. Ввод чисел продолжается до ввода пустой строки.

# from math import gcd
# from functools import reduce

# lst = []
# while True:
#    num = input('Введите число: ')
#    if num == '':
#        break
#    lst.append(int(num))
# print('Общий делитель: ' + str(reduce(gcd, lst)))

# 2. Орел и решка

text = 'ООООРРРРРРРРРРРООООО'
char_to_find = 'Р'
max_count = 0
tmp = 0
for b in text:
    if char_to_find == b:
        tmp += 1
    else:
        if tmp > max_count:
            max_count = tmp
        tmp = 0
if tmp > max_count:
    max_count = tmp
print(f'Последовательность: {text}')
print(f'Максимальная последовательность решки: {max_count}')