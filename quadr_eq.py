from math import sqrt
a = int(input("Введите переменную a: "))
b = int(input("Введите переменную b: "))
c = int(input("Введите переменную c: "))
D = (b * b - (4 * a * c))
print("Дискриминант = ", D)
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print("Корни квадратного уравнения: ", x1, x2)
elif D == 0:
    x1 = -b / (2 * a)
    print("Корень квадратного уравнения: ", x1)
else:
    print("Корней нет!")