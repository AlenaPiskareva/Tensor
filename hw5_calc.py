import os

def add(x, y):
    '''
    Функция сложения чисел
    '''
    return x + y
def minus(x, y):
    '''
    Функция вычитания чисел
    '''
    return x - y
def div(x, y): #   Функция деления чисел
  if y == 0:
    print('На ноль делить нельзя!')
  else:
    return x / y
def multiply(x, y):
    '''
    Функция умножения чисел
    '''
    return x * y
def power(x, y):
    '''
    Функция возведения числа в степень
    '''
    return x ** y


os.system("cls")
while True:
    operation = input('''
    Выберете операцию:
    '+' - сложение
    '-' - вычитание 
    '*' - умножение
    '/' - деление
    '**' - возведение в степень
    Пустой ввод - выход
    ''')
    if (operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '**' and operation != ''):
        print ('Вы ввели неверное действие, попробуйте еще раз.')
    if operation == '+':
        x = float(input('Введите первое число: '))
        y = float(input('Введите второе число: '))
        print(add(x, y))
    elif (operation == '-'):
        x = float(input('Введите первое число: '))
        y = float(input('Введите второе число: '))
        print(minus(x, y))
    elif (operation == '*'):
        x = float(input('Введите первое число: '))
        y = float(input('Введите второе число: '))
        print(multiply(x, y))
    elif (operation == '/'):
        x = float(input('Введите первое число: '))
        y = float(input('Введите второе число: '))
        print(div(x, y))
    elif (operation == '**'):
        x = float(input('Введите первое число: '))
        y = float(input('Введите степень, в которую возведем первое число: '))
        print(power(x, y))
    elif (operation == ''):
        print('Вы вышли из калькулятора!')
        break
    os.system("cls")