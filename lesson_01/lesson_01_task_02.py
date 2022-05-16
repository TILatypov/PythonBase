'''
2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
'''

print('----- Task_02 -----')

numbers_list = []
number = 1

while(number <= 1000):
    if(number % 2 == 1):
        numbers_list.append(number ** 3)
        number += 1
    else:
        number += 1

summa = 0

for i in numbers_list:
    sum_of_digits = 0
    remainder = i
    while remainder > 0:
        sum_of_digits = sum_of_digits + remainder % 10
        remainder = remainder // 10
    if sum_of_digits % 7 == 0:
        summa += sum_of_digits
print('Сумма чисел списка, сумма цифр которых делится нацело на 7 равна:', summa)

summa = 0

for i in numbers_list:
    sum_of_digits = 0
    remainder = i + 17
    while remainder > 0:
        sum_of_digits = sum_of_digits + remainder % 10
        remainder = remainder // 10
    if sum_of_digits % 7 == 0:
        summa += sum_of_digits
print('Сумма чисел списка + 17, сумма цифр которых делится нацело на 7 равна:', summa)
