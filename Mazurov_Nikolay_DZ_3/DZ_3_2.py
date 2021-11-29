# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

number = {'one': 'один','two': 'два','three': 'три','four': 'четыре','five': 'пять','six': 'шесть','seven': 'семь',
            'eight': 'восемь','nine': 'девять','ten': 'десять'}  # создаем  словарь разделяя запятой ключ и значение.

def num_translate(volue):    #Создаем функцию num_translate

    for eng, rus in number.items():
        if eng == volue:
            return rus
        elif eng.title() == volue:  # С большой буквы
            return rus.title()

print(num_translate('one'))
print(num_translate('One'))
print(num_translate('four'))
print(num_translate('Four'))
print(num_translate('two'))
print(num_translate('Two'))
print(num_translate('33'))
print(num_translate('vosem'))
x=input("Для выхода нажмите любой символ")