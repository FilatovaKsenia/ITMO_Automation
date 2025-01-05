#Задача 2
from itertools import count

a = 1
b = 5

if a > b:
    print(a)

else:
    print(b)

#Задача 3
a = 130
b = 1

if (a - b) ==135:
    print('YES')

else:
    print('NO')


#Задача 4
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def month(a):
    if a == 1 or a == 2 or a == 12:
        print('ЗИМА')

    if a == 3 or a == 4 or a == 5:
        print('ВЕСНА')

    if a == 6 or a == 7 or a == 8:
        print('ЛЕТО')

    if a == 9 or a == 10 or a == 11:
        print('ОСЕНЬ')
month(4)

#Задача 5
def number(a, b, c):

    if a > 10 and b > 10 and c > 10:
        print('YES')

    else:
        print('NO')
number(11, 110, 12)

#Задача 6
a = -5
b = 2
c = 3
d = -4
e = 5
print((a > 0) + (b > 0) + (c > 0) + (d > 0) + (e > 0))

#Задача 7
age = 0
month = 10

print((age * 12 * 29) + (month * 29))


