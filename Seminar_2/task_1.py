## Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
## Функцию hex используйте для проверки своего результата.

num_dec = int(input("Введите число: "))
res = ''
DIVIDER = 16
print(hex(num_dec))
while num_dec > 0:
    res = str(num_dec % DIVIDER) + res
    num_dec //= DIVIDER
print(res)
