#  Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из
#  этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.


src = [1000, 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 30, 20]
export_v = (src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1])
print('Результат:', *export_v)


from time import perf_counter
from sys import getsizeof




# ____________PERFOMANCE______________

count = perf_counter()
src = [1000, 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 30, 20]
export_v = [src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1]]
print('ВЫВОД:', export_v)
print('ЗАТРАЧЕНО :', perf_counter() - count)
print('ПОТРАЧНЕНО :', getsizeof(export_v))

#_______________Экономия ресурсов _________

count = perf_counter()
src = [1000, 300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 30, 20]
export_v = (src[idx] for idx in range(1, len(src)) if src[idx] > src[idx - 1])
print('ВЫВОД:', *export_v)
print('ЗАТРАЧЕНО :', perf_counter() - count)
print('ПОТРАЧНЕНО :', getsizeof(export_v))

x= input("Ведите символ для выхода.\n")
