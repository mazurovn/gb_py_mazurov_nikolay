#  Найти IP адрес спамера и количество отправленных им запросов по данным файла
#  логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший
#  больше всех запросов; код должен работать даже с файлами,
#  размер которых превышает объем ОЗУ компьютера.
#
#
#


from collections import Counter

st = "!"*40

with open("nginx_logs.txt","r", encoding='utf-8') as find:
    list_of_spammer = Counter()

    for spamm in find:

        list_of_spammer[spamm.split()[0]] += 1

    ip, count = list_of_spammer.most_common(1)[0][0], list_of_spammer.most_common(1)[0][1]

    print(f' {st}\n   !!!  НАЙДЕН  SPAMMER  !!!\n  ЕГО IP - '
          f' {ip} \n КОЛЛИЧЕСТВО СПАММА -   {count} !!! \n {st}')

x= input("Ведите символ для выхода.\n")