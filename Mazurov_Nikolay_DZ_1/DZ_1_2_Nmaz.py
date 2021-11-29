# Задание 1 пункт 2
# Nmaz
summa = 0
rsznachenie = 0
cubes = []
cube_to =[]


# Cоздать список, состоящий из кубов нечётных чисел от 1 до 1000.
for i in range(1, 1000, 2): # берем в списки четное число.
    cubes.append(i ** 3)# возведение в куб.

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

for index, zna, in enumerate(cubes):#перебор всех значений и проверяем кратность 7 и потом суммируем.
    rsznachenie = 0
    
    while zna > 0:
        rsznachenie += zna %10
        zna //=10
        
    if rsznachenie % 7 == 0:
        summa += cubes[index]
print(summa)

# К каждому элементу списка добавить 17  и заново вычислить сумму тех чисел из
# этого списка, сумма цифр которых делится нацело на 7.


for chislo in cubes:
    cube_to.append(chislo + 17)

# Повторное вычесление с новыми значениями + 17.
summa =0
for index, zna in  enumerate(cube_to):#перебор всех значений и проверяем кратность 7 и потом суммируем.
    rsznachenie = 0
    
    while zna > 0:
        rsznachenie += zna % 10
        zna //=10
        
    if rsznachenie %7 == 0:
        summa += cube_to[index]
print(summa)
x=input("Для выхода нажмите любой символ")
