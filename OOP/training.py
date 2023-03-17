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

class Phone:
    
    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone
    
    def get_info(self):
        return (f'Контакт: {self.name} {self.last_name}, телефон:{self.phone}')
    
    