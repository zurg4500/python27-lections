# from datetime import datetime

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         func(*args, **kwargs)
#         end = datetime.now()
#         print(f"Функция отработала за {end-start}")
#     return wrapper

# from functools import cache
# @timer
# @cache
# def func(count):
#     return sum(range(count))

# print(func(count=10000))

# <b>text</b> - жирный
# <i>text</i> - курсив

# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return f'<b>{res}</b>'
#     return wrapper

# def italic(func):
#    def wrapper(*args, **kwargs):
#        res = func(*args, **kwargs)
#        return f'<i>{res}</i>'
#    return wrapper

# @bold
# @italic
# def func(string):
#    return f'Hello {string}'
# func = bold(italic(func))

# print(func('Makers'))

# num1 = ['1', '3', '4', '7']
# num2 = list(map(int, num1))
# print(num2) # [1, 3, 4, 7] - преобразовала num1-строку в список с числами



# number1 = [1, 2, 3, 4, 6, 0]
# number2 = list(map(lambda x: x * 3, number1))
# print(number2) # [3, 6, 9, 12, 18, 0] - умножила на 3 числа в переменой number1


