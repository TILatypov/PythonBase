'''
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.

Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
'''

print('----- Task_01 -----')

duration = 8661

if (0 <= duration < 60):
    print(duration, 'сек')
elif (60 <= duration < 3600):
    minutes = duration // 60
    second = duration % 60
    print(minutes, 'мин', second, 'сек')
elif (3600 <= duration < 86400):
    hour = duration // 3600
    minutes = duration % 3600 // 60
    second = duration % 3600 % 60
    print(hour, 'час', minutes, 'мин', second, 'сек')
elif (duration >= 86400):
    day = duration // 86400
    hour = duration % 86400 // 3600
    minutes = duration % 86400 % 3600 // 60
    second = duration % 86400 % 3600 % 60
    print(day, 'дн', hour, 'час', minutes, 'мин', second, 'сек')
