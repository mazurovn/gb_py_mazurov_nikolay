#  Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
#  web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
#  олучить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами,
#  размер которых превышает объем ОЗУ компьютера.

file = "nginx_logs_to_new_dic.txt"

with open (file,"w", encoding= "utf-8") as new:  #создаем новый лог файл
    with open("nginx_logs.txt", "r", encoding="utf-8") as find_v: #открываем и обрезаем из лога
        write_to_new = ("{line.split()[0]}{line.split()[5][1:]} {line.split([6]}" for line in find_v)
        for list in write_to_new:
            print(list, file=new)  #сохраняем в новый файл

print(f"был создан файл: \n {file}" )
x= input("Ведите символ для выхода.\n")