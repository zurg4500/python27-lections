"================================Функции=============================="
# Функция - именованный блок кода, который принимает аргументы 
# и возвращает результат

# my_sum = lambda num1, num2: num1 + num2
# res = my_sum(5, 10)
# print(res) # 15
# lambda - ключевое слово, для создания анонимной функции

# def my_sum2(num1, num2):
#     return num1 + num2
# print(my_sum2) # <function my_sum2 at 0x7ff0f2c6b0d0>
# res = my_sum2(13, 45) # 58
# print(res) 

# def calc(num1, num2, oper):
#    """
#    oper - строка, с операцией для вычислений
#    "+" - сложение
#    "-" - вычитание
#    """
#    if oper == '+':
#        return num1 + num2
#    if oper == '-':
#        return num1 + num2
#    if oper == '*':
#        return num1 + num2
#    if oper == '/':
#        return num1 / num2
#print(calc(10, 7, '+')) # 17
#print(calc(10, 8, '-')) # 18
#print(calc(10, 15, '*')) # 25
#print(calc(10, 5, '/')) # 2.0
#print(calc(14, 12, '5')) # None


#def my_len(obj):
#    "Возвращает длину объекта"
#    count = 0
#    for i in obj:
#        count += 1
#        # count = count + 1
#    return count
#
#print(my_len([12, 14, 15, 16, 12])) # 5
#print(my_len('ajfjfjff')) # 8
#print(my_len({'a':1, 'b':2})) # 2

#def super_len(obj):
#    try:
#        return my_len(obj)
#    except:
        # если не можем, то будем итерировать его 
        # в виде строки
#        return my_len(str(obj))
    
#print(super_len([1,2,3,4])) # 4
#print(super_len(123344556)) # 9
#print(super_len(None)) # 4 - кол-во символов в ('None')=4 поэтому 4

"==================================DRY===================================="
# DRY - don't repeat yourself (не повторяйся)
# Функции позволяют не повторять один и тот же код

# представим, что у нас нет функции len

#str_ = "Hello world"
#count = 0
#for i in str_:
#    count += 1 # count - длина строки str_


#list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#count = 0
#for i in list1:
#    count += 1

#def len_(obj):
#    count = 0
#    for i in obj:
#        count += 1
#    return count

#str_ = 'Hello world'

"==================================Аргументы и параметры========================="
# параметры - локальные переменные, значение которым мы задаем при вызове функции
# аргументы - значения, которые мы задаем параметрам при вызове функции
# def func(parameter):
#     local_var = 5
#     print(locals())
    # {'parameter': 'Hello', 'local_var': 5}
    # {'parameter': 12, 'local_var': 5}
# func('Hello')
# func(12)
# print(local_var) NameError
# print(var) #NameError

"==============================Виды аргументов и параметров============================="
# 1. Обязательные
# 2. Необязательные
# 2.1 с дефолтным значением (по умолчанию)
# 2.2 args (arguments)
# 2.3 kwargs (key word arguments)

# def func(a, b='geforce'):
#    print(a, b)

# func()
# TypeError: func() missing 1 required positional argument: 'a'
# func('hello') # hello geforce
# func('hello', 100) # hello 100
 
# def func(a, b='geforce', *args):
#     print(a, b, args)

# func('hello', 112, 84, 23, 'world') # hello 112 (84, 23, 'world')

"============================Виды аргументов============================="
# позиционные (по порядку параметров)
# именованные (по имени параметров)

#def func(a, b):
#    print(f"a={a}, b={b}") 

#func(10, 20) # позиционно 
# a=10, b=20
#func(a=30, b=40) # именованно
# a=30, b=40
#func(a=112, b =213) # a=112, b=213

# def func(a, b='geforce', *args, **kwargs):
#     print(a, b, args, kwargs)

# func('hello', 100, 10, 20, key1='arguments', key2=500) # hello 100 (10, 20) {'key1': 'arguments', 'key2': 500}


"================================Звездочки=================================="
# args - tuple, куда попадут все позиционные аргументы, которые не попали по позиции
# kwargs - dict, куда попадут все именованные аргументы, которые не попали по имени
# list1 = [1,2,3,4]
# list2 = [*list1]
# print(list2) # [1, 2, 3, 4]

# list1 = [1,2,3,4]
# list2 = [*list1]

# dict1 = {'a':1, 'b':2}
# list3 = [*dict1]
# print(list3) # ['a', 'b']

# dict_ = {'a':1, 'b':2}
# list1 = [*dict_]
# def dictionary(list1):
#    for x in list1:
#         print(x)
# print(dictionary(list1))

# dict1 = {'a':1, 'b':2}
# list3 = {**dict1}
# print(list3) # {'a': 1, 'b': 2}

