# Домашнее задание 1 задача 1 Nikolay Mazurov
# ver 2.0 alfa
sec = int(input('введите  duration')) # вводим значение в переменную
day = sec // (3600 * 24) # Дни
hour = sec // 3600 % 24 # часы
min = sec % 3600 // 60  # Минуты
sec = sec % 3600 % 60 # Секнды
# print(sec,'секунд')
# print(min,'минут',sec,'секунд')
# print(hour,'часов',min,'минут',sec,'секунд')
print (day,'дней',hour,'часов',min,'минут',sec,'секунд')