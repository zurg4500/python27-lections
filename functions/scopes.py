"================Области видимости / пространства имён============="
# LEGB - (local, enclosed, global, buid-in)

# build-in - встроенное пространство
# print, input, int, str, sum

# global - глобальное пространство (наш файл)
# чтобы посмотреть все глобальные переменные - globala  

# a = 5
# b = 7
# print(globals())

# enclosed - замкнутое пространство (находится между двумя пространствами)
# локальное пространство, внутри которого есть еще одно локальное пространство

# var = 'глобальная'
# def func():
#     var = 'замкнутая'
#    def inner_func():
#         var = 'локальная'
#         def inner_inner_func():
#             var = 'супер локальная переменная'
#             print(var)
#         inner_inner_func()
#         print(var)
#     inner_func()
#     print(var)
# func() # если поменять местами func() и print(var) то изменится порядок вызова функций
# print(var)

# local - локальное пространство (внутри функции)
# a = 'hello'

# def func(a, b):
#     print("GLOBAL", globals()) # {'a':'hello', 'func':<function ...>}
#     print("LOCAL", locals()) # {'a':10, 'b':50}

# func(10, 50)

#num1 = 10

#def func():
#    print(num1)

#func()

#counter = 0

#def increase_counter():
#    global counter
#    counter += 1
#    print(counter)

#increase_counter() # 1
#increase_counter() # 2
#increase_counter() # 3
#increase_counter() # 4


#def count(i):
#    counter = 0

#    def increase_counter():
#        nonlocal counter
#        counter += 1
#        print(counter)

#    for _ in range(i):
#        increase_counter()

#count(10)

def func():
    a = 10
    def inner_func():
        def inner_inner_func():
            nonlocal a # nonlocal ищет переменные только внутри функций в предыдущих функциях
            a += 1
        inner_inner_func()
        print(a)
    inner_func()
func()

