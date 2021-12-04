# Написать свой модуль utils и перенести в него функцию currency_rates()
# из предыдущего задания. Создать скрипт, в котором импортировать этот модуль
# и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.


# Импорт модулей
from requests import get, utils
from datetime import date


check = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rate(parcng):
    znachenie = check.split("<Valute ID=") # режим  и добываем значения
    d, m, y, = map(int, znachenie[0].split('"')[-4].split("."))# добываем даты
    for i in znachenie:
        if parcng.upper() in i:
            print(date(year=y, month=m, day=d), end=" ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))#берем нужное значение


# print(currency_rate("uSd"))#выводим и приводим к значению USD
# print(currency_rate("EUR"))#выводим
