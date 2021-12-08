# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# ```
#
# Подсказка: использовать возможности python, изученные на уроке.





src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 22, 2]
list = []
check = []

for ch in src:
    if ch in check:
        continue
    if ch in list:
        check.append(ch)
        list.remove(ch)
        continue
    list.append(ch)
print(src)
print(list)
