def task_func(a = (1, 2, 3, 4)):
    return a[1]

print(task_func())

r = (105)
pi = (3.14159)

def compute_surface(radius, pi=3.14159):
    return pi*radius*radius

print(compute_surface(3))