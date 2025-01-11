#Задача 1

def task_1(a, b, c, d, e):
    return int, float, str, list, bool

a: int = 1
b: float = 0,1
c: str = 'homework'
d: list = [1, 2 , 3 , 4, 5]
e: bool = bool

print(int)
print(str)
print(float)
print(list)
print(bool)

#Задача 2

def task_2 (a):
    return a[0:3]

a: list = [1, 2, 3, 5, 8, 13, 21]

print('a[0:3] = ', a[0:3])

#Задача 3
def task_3(a:int) -> int:
    return a**2

print(task_3(a=4))

