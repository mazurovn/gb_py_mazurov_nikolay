# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы —
# результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


number = {'one': 'один','two': 'два','three': 'три','four': 'четыре','five': 'пять','six': 'шесть','seven': 'семь',
            'eight': 'восемь','nine': 'девять','ten': 'десять'}  # создаем  словарь разделяя запятой ключ и значение.

def num_translate(volue):    #Создаем функцию num_translate

    for eng, rus in number.items():
        if eng == volue:
            return rus

print(num_translate('one'))
print(num_translate('eight'))
print(num_translate('33'))
print(num_translate('vosem'))
x=input("Для выхода нажмите любой символ")