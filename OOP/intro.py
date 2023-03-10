class Person:
    arms = 2
    legs = 2
    name = 'Nasyikat'

    def __init__(self, name):
        # __init__ - dunder метод, который добавляет в объект self 
        # аттрибуты, которые отличаются у разных объектов
        self.name = name

    def walk(self):
        # self - ссылка на объект, у которого мы вызываем данные метод
        print(self)
        print("я хожу")

# Person.walk(person1)
# person1.walk()

# p1 = Person()
# p2 = Person()
# p3 = Person()
# print(p1.name, p2.name, p3.name)
# print(dir(Person))
# print(dir)

person1 = Person('Nasyikat')
person2 = Person('Bekbol')
print(person1.name, person2.name)

# Аттрибуты класса и аттрибуты объекта класса

class A:
    var1 = 'переменная класса'

    def __init__(self):
        self.var2 = 'переменная объекта'

print(dir(A))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']

obj = A()
print(dir(obj))

# A.var2
# AttributeError: type object 'A' has no attribute 'var2'
print(A.var1) # 'переменная класса'

print(obj.var1) # 'переменная класса'
print(obj.var2) # 'переменная объекта'


