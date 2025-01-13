#Задача 1

def task_1(a, b, c, d, e):
    a: int = 1
    b: float = 0,1
    c: str = 'homework'
    d: list = [1, 2 , 3 , 4, 5]
    e: bool = True

    print(type(a), type (b), type(c), type(d), type(e))

task_1(int, float, str, list, bool)


#Задача 2

def task_2 (a:list):
    return a[0:3]

a = [1, 2, 3, 5, 8, 13, 21]

print(a[0:3])

#Задача 3
def task_3(a:int) -> int:
    return a**2

print(task_3(4))

