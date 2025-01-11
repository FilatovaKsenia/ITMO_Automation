#Задача 2

def larger_number(a, b):
    if a > b:
        print(a)
    else:
        print(b)

larger_number(3, 6)


#Задача 3

def difference(a, b):
    if (a - b) ==135:
        print('YES')
    else:
        print('NO')

difference(100, 1)

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

def positive_number(a, b, c , d, e):

    print ((a > 0) + (b > 0) + (c > 0) + (d > 0) + (e > 0))

positive_number(-5, 2, 3, -4, 5)

#Задача 7

def count_days(age, month):

    print((age * 12 * 29) + (month * 29))

count_days(0, 10)


