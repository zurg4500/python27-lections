# JavaScriptObjectNotification - единый формат, в котором могут храниться только те типы данных, которые есть
# во всех языках программирования поддерживающие json

# числа int, float
# строки string
# словари dict
# булевые значения True, False
# списки list
# пустое значение None

import json

# сериализация - перевод из python в json
# dump - для работы с файлами
# dumps - функция, которая переводит python obj\объект в json строку

# десериализация - перевод из json в python
# load - 
# loads - функция, которая переводит json строку в python obj\объект

python_list = [1,2,3]
json_list = json.dumps(python_list)
print(type(python_list)) # list - <class 'list'>
print(type(json_list)) # string - <class 'str'>

print(python_list) # [1,2,3] - list
print(json_list) # "[1,2,3]" - string

json_dict = '{"a":1, "b":2}'
python_dict = json.loads(json_dict)

print(type(json_dict)) # string - <class 'str'>
print(type(python_dict)) # dict - <class 'dict'>

list_ = [
    1,2,3,
    4.6,
    (1,2,3),
    {'A':1},
    'hello',
    True, False, None
]

with open("test.json", "w") as file:
    json.dump(list_, file)






with open("test.json", "r") as file:
    res = json.load(file)

print(res) # [1, 2, 3, 4.6, [1, 2, 3], {'A': 1}, 'hello', True, False, None]