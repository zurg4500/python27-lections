"======================================Exceptions=================================="
# Исключения (ошибки) - объекты, которые обрывают работу кода, если не были обработаны
#'1' + 1          -          ошибка
#print 'hello'

# SyntaxError: '(' was never closed
# ОШибка выходит если допущена синтаксическая ошибка
# ОШибка выходит если используем ключевые слова не правильно

# TypeError
# исключение, которое выходит когда то что несвойсвенное для данного типа/типов данных
# также выходит когда передаем функции больше или меньше аргументов, чем она может обработать
# list1 = []
# list1.pop(1, 2 , 3) # TypeError: pop expected at most 1 argument, got 3
# Также выходит когда функции требует объект, но ему не передали объект
# list2 = []
# list2.append() # append() takes exactly one argument (0 given)

# KeyError
# Когда мы обращаемся к несуществующему ключу
# dict1 = {'a': 1, 'b':2}
# dict1.pop('c') # KeyError: 'c'
# if 'c' in dict - Проверка существования ключа

# NameError name 'fhhdjjdjjd' is not defined
# Выходит когда нет данной переменной

# a = 5
# id a ==6:
#     b = 7 # переменная создатся только если условие верное
# print(b) # NameError: name 'b' is not defined

# ValueError - ошибка выходит когда передаем в функцию то что она не может обработать
# int('10a') # invalid literal for int() with base 10: '10a'
# Когда мы пытаемся не такое кол-во элементов в нескольких переменных
# a, b = 1, 2 ,3
# a, b, c = 1, 2 # ValueError: too many values to unpack (expected 2)

# AttributeError - ошибка выходит когда к переменной применяют не свойсвенный ей метод 
# Когда пытаемся обратиться к несуществующему\несвойственному методу в каком-то типе данных
# list1 = []
# list1.lower() # AttributeError: 'list' object has no attribute 'lower'

# IndexError
# Ошибка выходит когда обращаемся по несуществующему индексу
# list1 = [1,2,3]
# list1[100] # IndexError: list index out of range
# Ошибка выходит когда пытаемся удалить элемент по несуществующему индексу
# list2 = []
# list2.pop() # IndexError: pop from empty list

# ModuleNotFoundError
# Ошибка выходит когда пытаемся обратится к несуществующей библиотеке
# import django # ModuleNotFoundError: No module named 'django'

# 10 / 0 # Ошибка выходит когда число делишь на 0, мат.формулы применимы и в языке програмирования python3
# ZeroDivisionError: division by zero

# IndentationError - ошибка выходит когда мы не соблюдаем отступы
# v = 10
# if True:
# print('hello') # IndentationError: expected an indented block

# Exception
# исключение, которое уже мы сами создали чтоб его вызвать

# raise SyntaxError # SyntaxError: None
# raise - метод когда сами вызываем ошибки
# чтоб вызвать исключения используем raise Exception('Hello')

"==========================Обработка исключений===================="
# Чтобы наш код не ломался, мы можем использовать конструкцию try-except 
# и обработать исключение

# try:
#    # код, который возможно вызовет ошибку
#    num = int(input("Введите число: "))
# except ValueError:
#     # код, кооторый отработает только если в блоке try вызвалась ошибка 
#    print("Вы ввели не число")
# else:
#      # код который отработает только если в блоке try ни одна ошибка не вызвалась
#       print("Введенное число")
# finally: 
#       # код который отработает в любом случае, хоть вызвалась ошибка, хоть и не вызвалась
#     print("До свидание!")

# минимальная конструкция состоит из try-except или try-finally
# можно использовать несколько except 
# try:
#     num1 = int(input("Введите 1 число "))
#     num2 = int(input("Введите 2 число "))
# except ValueError:
#     print('Вы ввели не число')
# except ZeroDivisionError:
#     print("Нельзя делить на 0")   
# try:
#    num1 = int(input("Введите 1 число "))
#    num2 = int(input("Введите 2 число "))
# except (ValueError, ZeroDivisionError):
#     print('Вы ввели не корректные данные')

# можно отловить любые исключения используя просто except
# try:
#     raise NameError
# except:
#     print("Любая ошибка")

# try:
#     print(1 + '1') # TypeError
# except TypeError:
#     try:
#       print(int('10a')) # ValueError
#       print("первый except")
#     except ValueError:
#      print("вложенный except")
# except ValueError:
#     print("второй except")
# finally:
#     print("все")

# Можно отловить любые ошибки, отлавливая Exception
# try:
#     raise SyntaxError # ValueError\NameError\SyntaxError - можно отловить любую ошибку
# except Exception as e:
#     print(type(e)

# TabError, IndentationError, SyntaxError - в питоне только 3 ошибки, остальные ValueError, KeyError и т.д.
# Ошибки не дадут читать код сразу изначально, а исключения будут читать код, пока не наткнется на ошибку

