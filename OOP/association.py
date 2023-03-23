"========================Ассоциация======================="
# Ассоциация принцип ООП в котором два класса друг с другом связаны 
#
#
#
#

class Battery:
    power = 100

    def charge(self):
        if self.power < 100:
            self.power = 100

class Iphone:
    def __init__(self, color):
        self.color = color 
        self.battery = Battery()
        # когда мы создаем объект от другого класса прям внутри другого - композиция

iphone = Iphone('золотой')
del iphone
# объект батарейки удаляется вместе с объектом iphone



#battery = Battery()
#print(battery.power)
#iphone = Iphone('золотой')
#print(iphone.battery.power)

#del iphone

#print(iphone)

class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery
        # когда мы принимаем уже созданный вне класса объект - агрегация

battery = Battery()
nokia = Nokia('черный', battery)

# print(nokia.battery.power)

del nokia 
# удаляется только объект nokia
# объект батарейки сохраняется

print(nokia.battery)
print(battery.power)