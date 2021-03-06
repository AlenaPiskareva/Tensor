#Задание ОШИБКИ

# Установлен Python3
# Ошибку вида "SyntaxError: unexpected EOF while parsing" не продемонстрирую

# Ошибка: SyntaxError: invalid syntax
#def f():
#    if a = 10:
#        s = a + 2
#        print(s)  #Приводит к ошибке из-за того, что переменная не сравнивается со значением, а происходит операция присваивания
# Исправим: 
a = 10
if a == 10:
    s = a + 2
    print(s)

# Ошибка: TypeError: Can’t convert ‘int’ object to str implicitly.
# n = input()
# k = n + 10
# print(k)
# Исправим: 
n = int(input())
k = n + 10
print(k)

# Ошибка: NameError: name1 ‘c’ is not defined
# a = 5
# b = 10
# s = a + b - c 
# print(s)
# Исправим: 
a = 5
b = 10
c = a + 1
m = a + b - c 
print(m)

# Ошибка: TabError: inconsistent use of tabs and spaces in indentation.
# x = 1
# y = -5 
# if x > 0:
#    if y < 0:
#     print(y)
# Исправим:
x = 1
y = -5
if x > 0:
    if y < 0:
        print(y)

# Ошибка: UnboundLocalError: local variable ‘a’ referenced before assignment.
# if a == 0:
#    a = a + 1
# Исправим: 
a = 0
if a == 0: 
    a = a + 1

# Ошибка: IndentationError: expected an indented block.
#def f(x):
#
#f(x)
# Исправим:
def f(x):
    x = 1
f(x)