"======================================Решения тасков: Введение в ООП============================="
# Решение 1 таска
#class Song:
#    def __init__(self, title, author, year):
#        self.title = title
#        self.author = author
#        self.year = year
#    
#    def show_title(self):
#        return f"Название этой песни {self.title}"
#
#    def show_author(self):
#        return f"Автор этой песни {self.author}"      
#
#    def show_year(self):
#        return f"Эта песня вышла в {self.year} году"
#
#song = Song("Happy", "Pharrell Williams", 2013)
#
#print(song.show_title())
#print(song.show_author())
#print(song.show_year())

# Решение 2 таска
#class SolarSystem: 
#    star = 'Sun'
#    def __init__(self, planet): 
#        self.planet = planet 

#first = SolarSystem('Mercury') 
#print(first.star) 
#second = SolarSystem('Venus') 
#print(second.star) 


class Circle:
    color = "Синий"
   
    def __init__(self, radius=int, pi=3.14):
        self.radius = radius
        self.pi = pi

    def get_area(self):
        res = (self.pi * self.radius)*2
        return res 

circle = Circle(2)
circle.get_area()

