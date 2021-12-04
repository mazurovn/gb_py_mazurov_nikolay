# Написать функцию currency_rates(), принимающую
# в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в
# обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе,
# вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите
# курсы доллара и евро.


from requests import get, utils

from datetime import date

check = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rate(parcng):
    znachenie = check.split("<Valute ID=")  # режим  и добываем значения
    d, m, y, = map(int, znachenie[0].split('"')[-4].split("."))  # добываем даты
    for i in znachenie:
        if parcng.upper() in i:
            print(date(year=y, month=m, day=d), end=" ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))  # берем нужное значение



# print(currency_rate("uSd"))#выводим и приводим к значению USD
# print(currency_rate("EUR"))#выводим
