# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.
# n = int(input('введите число'))
# s = ''
# h = '0123456789ABCDEF'
# while n > 0:
#     s = h[n % 16] + s
#     n = n // 16
# print(s)
# решение нашел в интернете

# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом
# number = float(input('Введите число: '))

# if number%1 == 0:
#   print(f'{number} не является дробным числом')
# else:
#   print(f'{number} является дробным числом')



# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между первой и последней буквой "о" из исходной строки. Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.