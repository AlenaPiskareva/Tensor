from itertools import cycle
#Скрипт
def xor_secret(data, key):
    """
    Алгоритм шифрования XOR
    """
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(data, cycle(key)))

while True:
  try:
    n = int(input('''
      Выберете:
      1. Зашифровать.
      2. Расшифровать
      3. Выход. \n '''))
  except:
    print('Еще раз')
    continue
  if n == 1:
    data = input("Введите текст: ")
    key = input("Введите ключ: ")
    txt_encr = xor_secret(data, key)
    print(f'Зашифрованный текст: {txt_encr}')
  if n == 2:
    data = input("Введите текст: ")
    key = input("Введите ключ: ")
    txt_decr = xor_secret(data, key)
    print(f'Расшифрованный текст: {txt_decr}')
  if n == 3:
    break
  