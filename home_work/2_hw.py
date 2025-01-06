#Задача 1
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

a: list = [1, 2, 3, 5, 8, 13, 21]

print('a[0:3] = ', a[0:3])

#Задача 3
def square_number(a:int) -> int:
    return a**2
print(square_number(a=4))

def pow(x: int, y: int) -> int:
    return x**y

print(pow(3,2))