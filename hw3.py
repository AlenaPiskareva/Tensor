# Задача 1. Определить, является ли число простым

from math import sqrt
n = int(input())
i = 2
if n < 2:
    print('Это число не является ни простым ни составным')
    quit()
elif n == 2:
    print('Число является простым')
    quit()
lim = sqrt(n)
while i <= lim:
    if n % i == 0:
        print('Число не является простым')
        quit()
    i = i + 1
print('Число является простым')

# Задача 2, 3. Найти НОД и НОК.

a = int(input("Первое число: "))
b = int(input("Второе число: "))
a = abs(a)
b = abs(b)
c = a * b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
nod = a + b
nok = c / nod
print(f"НОД для чисел {nod}; НОК для чисел {nok}")