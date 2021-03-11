#Даны два списка. Определите, совпадают ли множества их элементов.

import random
a_list = []
for i in range(3):
    a_list.append(random.randint(0, 3))
a_set = set(a_list)
b_list = []
for j in range(3):
    b_list.append(random.randint(0, 3))
b_set = set(b_list)
print(f"Первое множество: {a_set}")
print(f"Второе множество: {b_set}")
if a_set == b_set:
    print(True)
else:
    print(False)
