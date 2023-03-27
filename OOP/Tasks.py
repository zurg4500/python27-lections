"=====================Введение в ООП=========================="

# Решение для 5 таска:
class Phone:
    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone

    def get_info(self):
        print(f"Контакт: {self.name} {self.last_name}, телефон:{self.phone}")

contact = Phone('John', 'Snow', +996707707707)
contact.get_info()     
# Вывод\результат: Контакт: John Snow, телефон:996707707707

# Решение 6 таска:
class Salary:
    percent = 8

    def __init__(self, salary, experience):
        self.salary = salary
        self.experience = experience

    def count_percent(self):
        return self.salary * self.percent/100 * self.experience
    
    
obj = Salary(10000, 10)    
print(obj.count_percent())

# Вывод\результат:
# 8000.0

# Решение 7 таска:
import datetime 
class Nobel:

    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

    def get_year(self):
        x = datetime.datetime.now()
        y = x.year - self.year
        return f'выиграл {y} лет назад'
    
winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year())

  
winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
print(winner2.category, winner2.year, winner2.winner) 
print(winner2.get_year())

# 7 Другой пример с классом Сатурн:
import datetime 
class Saturnfilms:

    def __init__(self, film, year, winner):
        self.film = film
        self.year = year
        self.winner = winner

    def get_year(self):
        x = datetime.datetime.now()
        y = x.year - self.year
        return f'выиграл {y} лет назад'
    
winner1 = Saturnfilms("Терминатор", 1985, "Джеймс Кэмерон") 
print(winner1.film, winner1.year, winner1.winner) 
print(winner1.get_year())

# Вывод\результат:
# Терминатор 1985 Джеймс Кэмерон
# выиграл 38 лет назад
  
winner2 = Saturnfilms("Аватар", 2010, "Джеймс Кэмерон") 
print(winner2.film, winner2.year, winner2.winner) 
print(winner2.get_year())

# Вывод\результат:
# Аватар 2010 Джеймс Кэмерон
# выиграл 13 лет назад
 
# Решение 8 таска:
class Password: 
    
    def __init__(self, password): 
        self.password = password 
        
    def __str__(self) -> str:
        return '*' * len(self.password) 
        
    def validate(self):
        if not len(self.password) == 8 and len(self.password) < 15: 
            return f'Password should be longer than 8, and less than 15' 
        if not any(map(lambda i: i.isdigit(), self.password)): 
            return f'Password should contain numbers too' 
        if not any(map(lambda i: i.isalpha(), self.password)): 
            return f'Password should contain letters as well' 
        if not any(map(lambda i: i in ['@', '#', '&', '$', '%', '!', '~', '*'], self.password)): 
            return f'Your password should have some symbols' 
        return f'Ваш пароль сохранен.' 
    
password = Password('zurg450@') 
print(password.validate()) 
print(password)

# Вывод\результат:
# Ваш пароль сохранен.
# ********

"==============ООП. множественные наследование и миксины===================="

# Решение 3 таска:
from datetime import datetime
class Clock:
    def current_time(self):
        print(datetime.now().strftime("%H:%M:%S"))
    
class Alarm:
    def on(self):
        print("Будильник включен")

    def off(self):
        print("Будильник выключен")

class AlarmClock(Clock, Alarm):
    def alarm_on(self):
        self.on()

clock = AlarmClock()
clock.current_time() 
clock.alarm_on()

# Вывод\результат:
# 11:45:32
# Будильник включен

# Решение 3 таска варианто решения с помощью @staticmethod :
from datetime import datetime
class Clock:
    @staticmethod
    def current_time():
        print(datetime.now().strftime("%H:%M:%S"))
    
class Alarm:
    @staticmethod
    def on():
        print("Будильник включен")

    @staticmethod
    def off():
        print("Будильник выключен")

class AlarmClock(Clock, Alarm):
    def alarm_on(self):
        self.on()

clock = AlarmClock()
clock.current_time() 
clock.alarm_on()

# Вывод\результат:
# 11:46:40
# Будильник включен

"==============ООП. Методы класса и статические методы=================="

# Решение 5 таска:
class MoneyFmt:
    def __init__(self, amount):
        self.amount = amount
    
    @staticmethod
    def dollarize(float_num):
        if float_num >= 0:
            return f"${float_num:,.2f}"
        float_num = abs(float_num)
        return f"-${float_num:,.2f}"

    def update(self, new_amount):
        self.amount = new_amount
    
    def __repr__(self):
        return str(self.amount)
    
    def __str__(self):
        return self.dollarize(self.amount)

cash = MoneyFmt(12345678.021) 
print(cash) 
cash.update(100000.4567) 
print(cash) 
cash.update(-0.3) 
print(cash) 
print(repr(cash))

# Вывод/результат:
# $12,345,678.02 
# $100,000.46 
# -$0.30 
# -0.3 

# Решение 6 таска:
from datetime import datetime 

class CreateMixin: 
    def create(self, todo, key): 
        if key in self.todos: 
            return 'Задача под таким ключом уже существует' 
        self.todos[key] = todo 
        return self.todos 

class DeleteMixin: 
    def delete(self, key): 
        delete_ = self.todos.pop(key, None) 
        if not delete_:
            return 'нет такого ключа'
        return delete_

class UpdateMixin: 
    def update(self, key, new_value): 
        self.todos[key] = new_value 
        return self.todos 

class ReadMixin: 
    def read(self): 
        return sorted(self.todos.items())

class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin): 
    todos = {} 

    def set_deadline(self, deadline): 
        day, month, year = deadline.split("/")
        datetime_deadline = datetime(int(year), int(month), int(day))
        datetime_now = datetime.now()
        return (datetime_deadline - datetime_now).days + 1

task = ToDo() 
print(task.set_deadline('31/12/2022')) 

# Вывод\результат: -81
