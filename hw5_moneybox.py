def moneybox():
    while True:
        try:
            n = int(input('''Сколько денег вы вносите? '''))
            r = int(input('''Под какой процент? '''))
            d = int(input('''На сколько месяцев? '''))
        except:
            print('Ошибка! Еще раз.')
            continue
        break 
    print(f'К {d} месяцу вы накопите {acc(n, r, d)}')
def acc(n, r, d):
    if d == 0:
        return n
    elif d > 0:
        n = n * (1 + r/100)**d
        a = float('{:.3f}'.format(n))
    return a

while True:
        try:
            n = int(input('''
    Выберете:
    1. Функция о вкладе.
    Выход. \n '''))
        except:
            print('Еще раз')
            continue
        if n == 1:
            moneybox()