# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
# Проверить работу скрипта для случая, когда все файлы находятся в разных папках.



import DZ_6_4_NMAZ
from itertools import zip_longest
import sys
import argparse
users = []
hobb = []

user, hob,file = sys.argv[1:]

with open(user, "r",encoding="utf-8") as users:
    with open(hob,"r", encoding='utf-8') as hobb:
        data = zip_longest(users,hobb,fillvalue=None)
        with open(file,'w',encoding="utf-8") as find:
            for add in data:
                print(f"{str(add[0]).strip()} : {str(add[1]).strip()}", file=find)
hobbies_and_users = open(file, "r",encoding="utf-8")
print(type(hobbies_and_users))
print(hobbies_and_users.read())
x = input("Ведите символ для выхода.\n")
