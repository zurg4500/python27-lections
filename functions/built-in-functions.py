# enumerate

#string = 'hello'
#enum = enumerate(string)
#print(enum) # <enumerate object at 0x7f3cb8bfdb00>
#print(list(enum)) # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

#string = 'world'
#enum = enumerate(string, 5)
#print(list(enum)) # [(5, 'w'), (6, 'o'), (7, 'r'), (8, 'l'), (9, 'd')]

# дан список с числами, умножьте на 2 все числа под нечетным индексом, 
# умножьте на 3 все числа под индексом, кратным 3
#list1 = [1,2,3,4,2,3,4,1,4,9]

#for ind in range(len(list1)):
#    x1 = list1[ind]
#    if ind % 2: # ind % 2 !=0 - нечетное число, один из вариантов нахождения нечетного числа
#        list1[ind] = x1 * 2
#    if ind % 3 == 0: # not ind % 3
#        list1[ind] = x1 * 3

#print(list1) # [3, 4, 3, 12, 2, 6, 12, 2, 4, 27]


#list1 = [1,2,3,4,2,3,4,1,4,9]
#for ind, x1 in enumerate(list1):
#    if ind % 2:
#        list1[ind] = x1 * 2
#    if ind % 3 == 0:
#        list1[ind] = x1 * 3
# print(list1)

# string1 = 'abc'
# print(dict(enumerate(string1,1))) # {1: 'a', 2: 'b', 3: 'c'}

# zip
# list1 = [1,2,3,4,50]
# list2 = 'asgfggddg'
# list3 = [0.5,0.4,0.6]
# print(list(zip(list1, list2, list3))) # [(1, 'a', 0.5), (2, 's', 0.4), (3, 'g', 0.6)]


"================================Функция высшего порядка====================================="

# это функция, которая:
# принимает в аргументы другую функцию
# возвращает функцию
# создает внутри функцию
# вызывает внутри функцию

# map - принимает в аргументы функцию и итерируемый объект
# но также возвращает генератор, в котором все элементы - 
# результат принимаемой функции, в которую передали элементы последовательности

# x1 = map(int, ['1', '2', '3'])
# print(x1) # <map object at 0x7f8319273c40>
# print(list(x1)) # [1, 2, 3]

# list1 = [1,2,3,4]
# def res1(i):
#    return i+1
# print(list(map(res1, list1))) # [2, 3, 4, 5]

# y1 = [1,2,3,4]
# print(list(map(lambda x:x+1, y1))) # [2, 3, 4, 5]

# filter - принимает в аргументы функцию и итерируемый объект.
# возвращает генератор, в котором все элементы из последовательности
# прошедшие фильтр (функция вернула True)

# list1 = [-2,2,0,25,6,12,1244,10]
# def is_positive(x):
#    return x > 0 # Пример лаконичного возврата положительных чисел

# print(list(filter(is_positive, list1))) # [2, 25, 6, 12, 1244, 10]

# print(list(filter(lambda x: x>0, list1))) # [2, 25, 6, 12, 1244, 10]

# list1 = ['av', 'Cc', 'Fd', 'DEAD']

# print(list(filter(lambda i: i.istitle(), list1))) # ['Cc', 'Fd']
# print(list(filter(lambda i: i[0].isupper(), list1))) # ['Cc', 'Fd', 'DEAD']

# reduce - функция, которая импортируется из модуля functools.
# тоже принимает функцию и итерирумемый объект.
# возвращает один результат

from functools import reduce

# list1 = [2,3,4,5,67,123,8]

# def mul(x, y):
#     return x*y

# res = reduce(mul, list1) # функция reduce перемножила все числа в list1
# print(res) # 7911360 = 2*3*4*5*67*123*8

# string1 = 'hello world'
# print(reduce(lambda x,y: x + '$' + y, string1)) # h$e$l$l$o$ $w$o$r$l$d
# x='h', y='e' -> 'h$e'
# x='h$e', y='l' -> 'h$e$l'
# x='h$e$l', y='l' -> 'h$e$l$l'
# x='h$e$l$l', y='o' -> 'h$e$l$l$o'

# list1 = ['hello', 'bot', 'president']
# president
# print(reduce(lambda x, y: x if len(x)> len(y) else y, list1)) # president

