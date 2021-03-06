while(1):
    n = input("Укажите сигнал светофора (Red, Green, Green-Yellow, Red-Yellow) или exit: ")
    if n == 'Red':
        print('Стойте')
    elif n == 'Red-Yellow':
        print('Стойте, скоро будет зеленый')
    elif n == 'Green':
        print('Можно двигаться')
    elif n == 'Green-Yellow':
        print('Стойте, скоро будет красный')
    elif n == 'exit':
        print('До свидания!')
        break