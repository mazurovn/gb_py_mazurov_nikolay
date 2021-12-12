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



from itertools import zip_longest
import sys
import argparse

bake = []
price = []
x = 1000000
y = 10
print(f"число {x}\n\n")
print(f"число {y}\n\n")

with open("bakery.csv","r+", encoding="utf-8") as count:
    num, price = sys.argv[1:]
    price= round(float(price.replace(".","")), 3)

    for sale in range(int(num)):
        number = count.tell()
        stroka = count.readline().strip()
        if stroka == "":
            exit("Такой строки в документе нет.  \n ! Ошибка ввода!")
    if "," in str(price) or "." in str(price):
        if price <= x:
            count.seek(number)
            count.write(f"{price:>{y}}")

        else:
            print(f"Укажите значени меньше{x}")



file = "bakery.csv"
price_bake = open(file, "r",encoding="utf-8")
print(type(price_bake))
print(price_bake.read())
x = input("\n\nВедите символ для выхода.\n")
