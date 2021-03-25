import math
import cmath
from functools import reduce

# Решение задач с ранних уроков под *

# Задача 1. XOR-шифрование. Выполнение представлено в файле hw6_xor.py

def xor_secret():
    print('Выполнение представлено в файле hw6_xor.py')

# Задача 2. Частота использования цифр в диапазоне чисел.

def freq_digits(first, last):
    '''
    Функция для определения частоты использования цифр в диапазоне чисел.
    Пользователь вводит два числа. Первое - начало промежутка, второе - конец
    промежутка. Далее происходит перебор чисел от 0 до 9 (включительно),
    и на экране происходит вывод каждого числа и частота его использования в
    промежутке.
    '''
    _str = ''
    for k in range(first, last+1):
        _str += str(k)
    print(f'Вы получили строку: {_str}')
    for i in range(0, 10):
        print(f'Число {i} встречается в строке {_str.count(str(i))} раз')

# Задача 3. Частота использования символов в тексте.

def freq_str(_str):
    '''
    Функция для определения частоты использования использования
    символов в тексте.
    Пользователь вводит строку, состоящую из любого набора букв/символов.
    Далее поэлементно пробегаем по каждому символу,и на экране происходит
    вывод каждого символа и частота его использования в введенной строке.
    '''
    print(f'Введенная строка: {_str}')
    while len(_str) != 0:
        print(f'Символ {_str[0]} используется {_str.count(_str[0])} раз(а)')
        _str = _str.replace(_str[0],'')
        print(_str)

# Задача 4. Удалить из списка элементы, значения которых уже встречались в этом же списке в предыдущих элементах.

def delete_elem(lst, item):
    '''
    Функция для удаления повторяющихся элементов массива. На вход: массив
    чисел и число, проверяющееся на повторение. На экран выводится список
    с удаленным элементом 
    '''
    if lst.count(item) > 1:
        return [i for i in lst if i != item]
    return list(lst)

# Задача 5. Вводится текст, содержащий различные скобки, необходимо определить, все ли с кобки расставлены корректно.
    
def check_correct(str):
    '''
    Функция, определящая верно ли расставлены скобки в строке. На вход: строка,
    содержащая скобки. Далее поиск открывающая-закрывающая скобка. На выходе
    сообщение: true - корректно, false - не корректно

    '''
    while True:
        if str[0] == '(':
            k = ')'
        elif str[0] == '[':
            k = ']'
        elif str[0] == '{':
            k = '}'
        else:
            return False
        if len(str) !=1 and str[1] == k:
            str = str[2:len(str)]
        elif k == str[len(str)-1]:
            str = str[1:len(str)-1]
        else:
            return False
        if len(str) == 0:
            return True

# Задача 6. Вычисление факториала числа с использованием lambda (не рекурсия).
def fact_lambda_notrec():
    print('Затрудняюсь решить задание')

# Задача 7. Подсчет частоты вхождений символов в текст с использованием lambda.
def count_text():
    print('Выполнение представлено в файле hw5_text.py')

# Задача 8. Создание калькулятора
def calc():
    print('Выполнение представлено в файле hw5_calc.py')



while True:
    try:
        n = int(input(
        '''
        Выберите задачу: 
        1. XOR-шифрование. Выполнение представлено в файле hw6_xor.py
        2. Частота использования цифр в диапазоне чисел.
        3. Частота использования символов в тексте.
        4. Удалить из списка элементы, значения которых уже встречались в этом же списке в предыдущих элементах.
        '''
    ))
    except:
        print('Ошибка! Выберите номер нужной задачи')
        continue
    if n == 1:
        xor_secret()
    
    if n == 2:
        try:
            first = int(input('Введите первое число списка: '))
            last = int(input('Введите последнее число списка: '))
        except:
            print('Вам нужно ввести целые числа, задающие список от 1-ого до n-ого')
            continue
        freq_digits(first, last)
    if n == 3:
        try:
            _str = str(input('Введите строку: '))
        except:
            print('Вам нужно ввести строку, состоящую из букв/символов')
            continue
    freq_str(_str)

    if n == 4:
        try:
            lst = input('Введите массив элементов в виде [n0,n1,n2,...]: ')
            item = input('Введите элемент, который хотите проверить на повторение: ')
        except:
            print('Ошибка! Следуйте правилам ввода.')
            continue
    delete_elem(lst, item)

    if n == 5:
        str = input('Введите строку со скобками:')
        for i in (range(len(str))):
            if str[i]!='(' or str[i]!=')' or str[i]!='[' or str[i]!=']' or str[i]!='{' or str[i]!='}':
                str.replace(str[i],'')
        print(f'Все ли скобки расставлены верно? - {check_correct(str)}')

    if n == 6:
        fact_lambda_notrec()
    
    if n == 7:
        count_text()
    
    if n == 8:
        calc()

        