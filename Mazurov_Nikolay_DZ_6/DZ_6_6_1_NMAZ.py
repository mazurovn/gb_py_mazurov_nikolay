# Реализовать простую систему хранения данных о
# суммах продаж булочной. Должно быть два скрипта с интерфейсом
# командной строки: для записи данных и для вывода на экран
# записанных данных. При записи передавать из командной строки
# значение суммы продаж. Для чтения данных реализовать
# в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом —
# выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить
# записи, начиная с номера, равного первому числу,
# по номер, равный второму числу, включительно.


########################  ОТОБРОЖЕНИЕ  ################
from itertools import zip_longest
import sys
import argparse

bake=[]
price = []

with open("bakery.csv","r",encoding="utf-8") as add_item:

    if 1< len(sys.argv) < 4 and [ch for ch in sys.argv[1:] if ch.isdigit()]:
        if len(sys.argv) == 3:

            first, last = map(int, sys.argv[1:])


            print(*(price for ch, price in enumerate(add_item) if first - 1 <= ch < last), sep="")
        else:

                print(add_item.read())
file = "bakery.csv"
price_bake = open(file, "r",encoding="utf-8")

print(type(price_bake))
print(price_bake.read())

x = input("Ведите символ для выхода.\n")
