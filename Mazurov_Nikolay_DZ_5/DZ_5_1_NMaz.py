# Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
i= int(input("Ведите число до которого генерировать нечетные числа : \n      "))
def gen_nechet(nums):
    for ch in range(1, nums + 1, 2):
        yield ch
for n in gen_nechet(i):
    print(n)
x= input("Ведите символ для выхода.\n")
