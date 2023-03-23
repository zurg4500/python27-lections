#class Circle:
#    color = "Синий"
#    pi = 3.14
#    def __init__(self,radius):
#        self.radius = radius
#    def get_area(self):
#        return self.pi*(self.radius**2)
#circle = Circle(2)
#circle.color = 'жёлтый'
#print(circle.color)
#print(circle.get_area())


#class Circle:
#    color = "Синий"
#    pi = 3.14
#    def __init__(self,radius):
#        self.radius = radius
#    def get_area(self):
#        return self.pi*(self.radius**2)
#circle = Circle(2)
#circle.color = 'жёлтый'
#print(circle.color)
#print(circle.get_area())

#class BankAccount:
#    def withdraw(self, amount):
#        self.balance -= amount
#        print(f'Ваш баланс: {self.balance} сом')
#    
#    def deposit(self, amount):
#        self.balance += amount
#        print(f'Ваш баланс: {self.balance} сом')
#
#account = BankAccount()
#print(account.deposit(1000))
#print(account.withdraw(500))

#class Taxi:
#    def __init__(self, name, cost, cost_km):
#        self.name = name
#        self.cost = cost
#        self.cost_km = cost_km

#    def get_total_cost(self, km):
#        self.cost = self.cost_km * km + self.cost
#        return f'Такси {self.name}, стоимость поездки: {self.cost} сом'

#taxi1 = Taxi(name='Namba', cost=179, cost_km=1)
#taxi2 = Taxi(name='Yandex', cost=127, cost_km=1)
#taxi3 = Taxi(name='Jorgo', cost=238, cost_km=1)
#print(taxi1.get_total_cost(10))
#print(taxi2.get_total_cost(6))
#print(taxi3.get_total_cost(14))



#class Phone:
#    
#    def __init__(self, name, last_name, phone):
#        self.name = name
#        self.last_name = last_name
#        self.phone = phone
#    
#    def get_info(self):
#        print(f"Контакт: {self.name} {self.last_name} телефон: {self.phone}")

#contact = Phone('John', 'Snow', 996707707707)
#contact.get_info()

"""
1) Создайте класс Auto в нем реализуйте метод ride который выводит сообщение 'Riding on a ground'.

Создайте класс Boat реализуйте метод swim, который выводит 'Floating on water'.

Создайте класс Amphibian который наследуется от класса Auto и Boat.

Создайте от него объект obj и вызовите все методы.

Ввод:

obj = Amphibian() 
obj.ride() 
obj.swim() 
Вывод:

Riding on a ground 
Floating on water 
"""
#class Auto:
#    def ride(self):
#        print("Riding on a ground")

#class Boat:
#    def swim(self):
#        print("Floating on water")

#class Amphibian(Auto, Boat):
#    def __init__(self):
#        pass

#obj = Amphibian()
#obj.ride()
#obj.swim()

"""
2)Создайте класс ContactList, который должен наследоваться от встроенного класса list.

В вашем классе должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений.

Создайте экземпляр класса в переменной all_contacts и передайте список ваших контактов.

Примерный ввод:

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
print(all_contacts.search_by_name('Olya')) 
Метод search_by_name возвращает все строки содержащие подстроку "Olya":

['Ivan Olya', 'Olya Ivan'] 
"""
#class ContactList(list):
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#    def search_by_name(self):
#        for self.x in list:
#            if self.x == self.y:
#                return self.x

#all_contacts = ContactList(['Ivan', 'Maris', 'Olga', #'Ivan Olya', 'Olya Ivan', 'ivan']) 
#print(all_contacts.search_by_name('Olya')) 



"""

3) Напишите класс Person, который будет хранить информацию о пользователе. У объекта будут следующие атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email).
При инициализации объекта, передавать аргументы классу не нужно, все его атрибуты по умолчанию будут равны None и также все они будут приватными.
Поэтому реализуйте для каждого атрибута методы доступа get и set не используя декораторы property и setter. У вас будут такие методы: get_name, set_name, get_last_name, set_last_name, get_age, set_age, get_email, set_email.
Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран.
Пример:

john = Person()
print(john.get_name()) # None
print(john.get_last_name()) # None
print(john.get_age()) # None
print(john.get_email()) # None
john.set_name('John')
john.set_last_name('Snow')
john.set_age(30)
john.set_email('johnsnow@gmail.com')
print(john.get_name()) # John
print(john.get_last_name()) # Snow
print(john.get_age()) # 30
print(john.get_email()) # johnsnow@gmail.com
"""

#class Person:
#    __name = 'John'
#    __last_name = 'Snow'
#    __age = 30
#    __email = 'johnsnow@gmail.com'
#    def __init__(self, name, last_name, age, email):
#        self.name = name
#        self.last_name = last_name
#        self.age = age
#        self.email = email
#
#    def get_name(self):
#        return None
#
#    def set_name(self):
#        print(self.name)
#
#    def get_last_name(self):
#        return None
#
#    def set_last_name(self):
#        print(self.last_name)
#
#    def get_age(self):
#        return None
#      
#    def set_age(self):
#        print(self.age)
#
#    def get_email(self):
#        return None

#    def set_email(self):
#        print(self.email)

#john = Person()
#print(john.get_name()) # None
#print(john.get_last_name()) # None
#print(john.get_age()) # None
#print(john.get_email()) # None
#john.set_name('John')
#john.set_last_name('Snow')
#john.set_age(30)
#john.set_email('johnsnow@gmail.com')
#print(john.get_name()) # John
#print(john.get_last_name()) # Snow
#print(john.get_age()) # 30
#print(john.get_email()) # johnsnow@gmail.com


#class Plant: 
#     oxygen = 900 

#     def __init__(self, height): 
#        self.height = height 

#     def grow(self, cm): 
#        self.height += cm 
#        self.oxygen += 35 
#        return self.height 
     
#kaktus = Plant(10) 
#print(kaktus.grow(2)) 
#print(kaktus.oxygen) 

#class Plant: 
#     season = 'зима' 

#     @classmethod 
#     def change_season(cls, value): 
#        cls.season = value 

#Plant.change_season('зима') 
#kaktus = Plant() 
#ficus = Plant() 
#print(kaktus.season, ficus.season) 

#class Plant:

#     @staticmethod 
#     def is_blooming(season): 
#        if season == 'весна': 
#            print('Да') 
#        else:  
#           print('Нет') 

#Plant.is_blooming('зима') 

class Product:
    base_price = 20000

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    @staticmethod
    def has_garantiya(year):
        for i in year:
            if i + 3 in year:
                print("Ваша гарантия истекла")
            else:
                print("Гарантия действительна")
    
    @classmethod
    def change_price(cls, rate):
        cls.base_price = rate * 20000
        return cls.base_price

obj = Product('A218', 2009, 'red') 
obj.change_price(3) 
print(obj.has_garantiya(2010)) 
print(obj.base_price)   