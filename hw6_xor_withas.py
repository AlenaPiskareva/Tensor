def xor_encryption(data, key):
    crypt = ""
    for i in data:
      crypt += chr(ord(i)^ord(key))
    with open("crypt.txt", "w") as file:
        file.write(crypt)

    print(f'Зашифрованное сообщение: {crypt}')


def xor_decryption(data, key):
  decrypt = ""
  with open("crypt.txt", "r") as file:
    for j in file.read():
      decrypt += chr(ord(j)^ord(key))

  print(f'Расшифрованное сообщение: {decrypt}')

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
    xor_encryption(data,key)
  if n == 2:
    data = input("Введите текст: ")
    key = input("Введите ключ: ")
    xor_decryption(data, key)
  if n == 3:
    break
  