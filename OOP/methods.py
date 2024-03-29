class A:
    def instance_method(self):
        print("Метод объекта")
        print("self", self)
obj = A()
obj.instance_method()
# метод объекта 
# self <__main__.A object at 0x7f22d
# когда мы вызываем метод у объекта, то нам не нужно передавать его в self, он передается автоматически

A.instance_method(obj)
# метод объекта
# self <__main__.A object at 0x7f85cc04faf0>
# когда мы вызываем метод у класса, то нам нужно передавать объект

class A:
    @classmethod
    def class_method(cls):
        print("метод класса")
        print("cls", cls)

A.class_method()
# метод класса
# cls <class '__main__.A'>

obj = A()
obj.class_method()
# метод класса
# cls <class '__main__.A'>

# все равно от куда вы будете вызывать classmethod (от объекта или класса), первым аргументо будет приходить class



# примеры
class C:
    counter = 0

    def __init__(self):
        # объект создается
        self._inc_counter()

    def __del__(self):
        # объект удаляется
        # C.counter -= 1
        self._dec_counter()

    @classmethod
    def _inc_counter(cls):
        # cls - class C
        # увеличиваем аттрибут класса counter на один
        cls.counter += 1
    
    @classmethod
    def _dec_counter(cls):
        cls.counter -= 1

obj1 = C()
obj2 = C()
obj3 = C()
obj4 = C()
print(C.counter) # 4
del obj1, obj2
print(C.counter) # 2


class Pizza:
    def __init__(self, radius, *ingredients):
        self.r = radius
        self.ingredients = ingredients

    def cook(self):
        print(f"Пицца размером {self.r*2}")
        print(f"Ингридиенты: {self.ingredients}")

    @classmethod
    def four_cheeze(cls, radius):
        pizza = cls(radius, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
        # pizza = Pizza(10, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
        return pizza

pizza1 = Pizza(15, "Сыр", "Колбаса", "Cherry")
pizza1.cook()

pizza2 = Pizza(10, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
pizza2.cook()
 

pizza3 = Pizza(15, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
pizza3.cook()

pizza4 = Pizza.four_cheeze(10)
pizza4.cook()

pizza5 = Pizza.four_cheeze(15)
pizza5.cook()


class A:
    @staticmethod
    def static_method():
        print("статик метод")

obj = A()
obj.static_method()


class Cylinder:
    def __init__(self, diametr, height):
        self.di = diametr
        self.h = height
        self.area = self.get_area(diametr, height)

    @staticmethod
    def get_area(di, h):
        from math import pi
        circle_area = pi * di**2 / 4
        side_area = pi * di * h             # Ингридиенты: ('1 сыр', '2 сыр', '3 сыр', '4 сыр')
        return circle_area*2 + side_area # статик метод
    
cylinder1 = Cylinder(4, 10)
print(cylinder1.area) # 150.79644737231007

print(Cylinder.get_area(4, 10))
# мы не создали объект. но получили нужные нам расчеты



def get_area_cylinder(di, h):
        from math import pi
        circle_area = pi * di**2 / 4
        side_area = pi * di * h             
        return circle_area*2 + side_area 

print(get_area_cylinder(4, 10))
