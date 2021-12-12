#
#  Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется,
# не нужно реально создавать такие большие файлы,
# это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей и название каждого
#  хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться
#  данные, полученные в результате парсинга.

users = []
hobb = []

from itertools import zip_longest
with open("users.csv", "r",encoding="utf-8") as users:
    with open("hobby.csv","r", encoding='utf-8') as hobb:
        data = zip_longest(users,hobb,fillvalue=None)
        with open("hobbies_and_users_6_4.txt",'w',encoding="utf-8") as find:
            for add in data:
                print(f"{str(add[0]).strip()} : {str(add[1]).strip()}", file=find)
hobbies_and_users = open("hobbies_and_users_6_4.txt", "r",encoding="utf-8")
print(type(hobbies_and_users))
print(hobbies_and_users.read())
x = input("Ведите символ для выхода.\n")
