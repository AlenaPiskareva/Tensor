# Факториал через функцию

def fact(n):
    factorial = 1
    if n == 0:
        return 1
    while n > 1:
        factorial *= n
        n = n - 1
    return factorial

# Факториал через лямбда рекурсией.
#factor = lambda x: x and x * factor(x - 1) or 1

# Факториал через лямбда без рекурсии

while True:
    try:
        n = int(input('''
    Выберете:
    1.Факториал через функцию.
    2.Факториал через lambda (рекурсия). 
    3.Факториал через lambda (не рекурсия) - не сделала.
    Выход.\n'''))
    except:
        print('Еще раз')
        continue
    if n == 1:
        while True:
            try:
                a = int(input('Введите число для которого посчитать факториал: '))
            except:
                print('Еще раз!')
                continue
            if a < 0:
                print('Еще раз!')
                continue
            break
        print(f'Факториал {a} = {fact(a)}')

    if n == 2:
        while True:
            try:
                a = int(input('Введите число для которого посчитать факториал: '))
            except:
                print('Еще раз!')
                continue
            if a < 0:
                print('Еще раз!')
                continue
            break
        print(f'Факториал {a} равен {fact(a)}')
    
            