"=====================================Comprehensions======================="
# генератор, с помощью которого можно создавать последовательность используя цикл for

# list1 = []
# for i in range(1, 11):
#    list1.append(i)
# list1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1 = [i for i in range(1,11)]
# print(list1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# результат for элемент in последовательность
# результат for элемент in последовательность if фильтр

# comprehensions = (i for i in range(1, 4))
# print(comprehensions)
# <generator object <genexpr> at 0x7f6dfd94e490>
# генератор - итерируемый объект, который хранит в себе полностью все элементы последовательности, а генерирует их когда требуется

# print (next(comprehensions)) # 1
# print (next(comprehensions)) # 2
# print (next(comprehensions)) # 3
# print (next(comprehensions)) # StopIteration

# next - функция, которая принимает в себя генератор, запрашивает следующий элемент у генератора и возвращает его

# comprehensions = (i for i in range(1, 4))
# print(list(comprehensions)) # [1, 2, 3]
# print(list(comprehensions)) # []

"=========================Синтаксический сахар===================="
# list comprehension
# list_compr = [i for i in 'hello']
# print(list_compr)
# ['h', 'e', 'l', 'l', 'o']

# dict comprehension
# dict_compr = {i:str(i) for i in range(1, 11)}
# print(dict_compr)
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

# фильтр 
# string = 'Hello World'
# res = [i for i in string]
# print(res) # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
# string = 'Hello World'
# res = [i for i in string if i.islower()]
# print(res) # ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd'] - 1 вариант

# string = 'Hello World'
# res = []
# for i in string:
#     if i.islower():
#         res.append(i)
# print(res) # ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd'] - 2 вариант

# Создать список чисел от 1 до 10
# res = []
# for i in range(1, 11):
#     if i% 2 == 0:
#         res.append(i)
# print(res) # [2, 4, 6, 8, 10] - 1 вариант

# res = [i for i in range(1, 11) if i % 2 == 0]
# print(res) # [2, 4, 6, 8, 10] - 2 вариант

# res = [i for i in range (2, 11, 2)]
# print(res) # [2, 4, 6, 8, 10] - 3 вариант

# создать список из чисел от 1 до 100
# range(1, 11)
# res = [i*100 for i in range(1,11)]
# print(res) # [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# создать списко с именами ['Hello test1, 'Hello test2', 'Hello test3']

# users = ['test1', 'test2', 'test3']
# res = ['Hello '+name for name in users]
# res = [f'Hello {name}' for name in users]
# print(res)

# [
#    [1],
#    [1,2]
#    [1,2,3]
#    [1,2,3,4]
#    [1,2,3,4,5]
# ]

# res = [[x for x in range(1, i+1)] for i in range(1,6)] # [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
# print(res)


# res = []
# for i in range(1,6):
#     inner_list = []
#     for x in range(1, i+1):
#         inner_list.append(x)
#     res.append(inner_list)
# print(res) # [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

# list1 = [[1,2,3], [4,5,6], [7,8,9]]
# res = [1,2,3,4,5,6,7,8,9]
# res = [i for inner_list in list1 for i in inner_list]
# print(res) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# dict1 = {'a':1, 'b':2, 'c':3}
# {1:'a', 2:'b', 3:'c'}

# res = {v:k for k, v in dict1.items()}
# print(res) # {1: 'a', 2: 'b', 3: 'c'}

# res = {i:[x for x in range(1, i+1)] for i in range(1,6)}
# print(res) # {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

# set comprehension - удобно убирать дубликаты в последовательности
# set_comp = {x for x in range(10)}
# print({1, True, 'hello', 10, 1})  #  {1, 10, 'hello'} - все 1 ушли в первый по индексу 0 - 1

Таск 28 Типы данных. Словари
dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
dict2 = {}

for k, v in dict1.items():
    mul_ = 1
    for v2 in v.values():
        mul_ = mul_ *v2
        dict2[k] = mul_
print(dict2)

Таск 14 решение
Aidina, [14.02.2023 13:43]
my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
dict_ = {k : v2 for k,v in my_dict.items() for v2 in v.values()}
print(dict_)

Nurkamila, [14.02.2023 14:17]
"14"
dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
'Olga': {'history': 92, 'math': 96, 'literature': 81},
'Nik': {'history': 84, 'math': 85, 'literature': 87}}

new_dict = {}

for k1, v1 in dict_.items():
    for k2, v2 in v1.items():
        max_num = max(v1.values())
        if max_num == v2:
            new_dict[k1] = k2
print(new_dict)

# res = {k1: k2 for k1, v1 in dict_.items() for k2, v2 in v1.items() if max(v1.values()) == v2}



