#
#
# Есть два файла: в одном хранятся ФИО пользователей сайта,
# а в другом — данные об их хобби. Известно, что при хранении данных используется
# принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):



from itertools import zip_longest
import json

users = []
hobb = []
with open('users.csv', 'r', encoding='utf-8') as find:
    for line in find:
        users.append(line.strip())

with open('hobby.csv', 'r', encoding='utf-8') as find:
    for line in find:
        hobb.append(line.strip())

if len(users) < len(hobb):
    print("меньше пользователей")
    exit(1)

hobbies_and_users = {user: hobby for (user, hobby) in zip_longest(users, hobb)}

with open('hobbies_and_users_6_3.txt', 'w',encoding="utf-8") as find:
    json.dump(hobbies_and_users, find)

with open('hobbies_and_users_6_3.txt', 'r',encoding="utf-8") as find:
    hobbies_and_users = json.load(find)
print (f"Вывод класса:")
print(type(hobbies_and_users))
print (f"Вывод файла:")
for all_print in hobbies_and_users.items():
    print(all_print)

x= input("Ведите символ для выхода.\n")