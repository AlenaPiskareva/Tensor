def count_txt():
    while True:
        try:
            n = int(input('''
    Выберите задачу:
    1.Подсчет частоты вхождений символов в текст.
    2.Подсчета количества слов в тексте. 
    3.Посчета количества предложений в тексте.
    4.Выход.\n'''))
        except:
            print('Еще раз')
            continue
        if n == 1:
            s = str(input('Введите строку: '))
            while len(s) != 0:
                print(f'Символ {s[0]} встречается {s.count(s[0])} раз(а)')
                s = s.replace(s[0],'')
        if n == 2:
            s = str(input('Введите текст: '))
            words = s.split(' ' or '\n')
            print(f'Количество слов в тексте:{len(words)}')
        if n == 3:
            s = str(input('Введите текст: '))
            sentence = s.count('.')+s.count('!')+s.count('?')
            print(f'Количество предложений в тексте: {sentence}')
        if n == 4:
            break
    
while True:
        try:
            n = int(input('''
    Выберете:
    1.Функция для подсчета символов, слов, предложений.
    2.Выход.\n'''))
        except:
          print('Еще раз')
          continue
        if n == 1:
            count_txt()
            break
        if n == 2:
            break