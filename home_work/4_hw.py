#Задача 1
class Rectangle:

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def square(self):
        return (self.weight * self.height)

    def perimeter(self):
        return (self.weight + self.height)

r1 = Rectangle(10, 5)
r2 = Rectangle(1, 2)
r3 = Rectangle(5, 3)
r4 = Rectangle(7, 14)
print(r1.square())
print(r1.perimeter())
print(r2.square())
print(r2.perimeter())
print(r3.square())
print(r3.perimeter())
print(r4.square())
print(r4.perimeter())


#Задача 2

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return (self.a + self.b)

    def multiplication(self):
        return (self.a * self.b)

    def division(self):
        return (self.a / self.b)

    def subtraction(self):
        return (self.a - self.b)

m = Math(10, 20)
print(m.addition())
print(m.multiplication())
print(m.division())
print(m.subtraction())

#Задача 3

class ButtonTwo:

    type: str = 'Кнопка'

    def __init__(self, text, loc=None):
        self.text = text
        self.loc = loc

    def click(self):
        return ('Клик по кнопке - {}'.format(self.text))


text_field = ButtonTwo('Текстовое поле')
flag = ButtonTwo('Установите флажок')
switch_button = ButtonTwo('Кнопка переключения')
web_tables = ButtonTwo('Вев-таблицы')
buttons = ButtonTwo('Кнопки')
links = ButtonTwo('Ссылки')
images = ButtonTwo('Неработающие ссылки - Изображения')
upload_and_download = ButtonTwo('Загружать и скачивать')
dynamic_properties = ButtonTwo('Динамические изменения')

print(text_field.click())
print(flag.click())
print(switch_button.click())
print(web_tables.click())
print(buttons.click())
print(links.click())
print(images.click())
print(upload_and_download.click())
print(dynamic_properties.click())