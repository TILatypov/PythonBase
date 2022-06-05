'''
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке,
например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
'''

print('----- Task_05 -----')


import sys
from time import perf_counter


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

#'----- First step - filtaring of list and create "ignore list" -----'

start = perf_counter()
_result = []
_to_ignore = []
for i in src:
    if i not in _result:
        _result.append(i)
    else:
        _to_ignore.append(i)
_to_ignore = list(set(_to_ignore))

#'----- Second step - filtaring of list by using "ignore list" from previous step -----'

result = []
for i in _result:
    if i not in _to_ignore:
        result.append(i)
print(result)
print(f'size: {sys.getsizeof(result)}, time: {perf_counter() - start}')

print('\n----- My bad code got faster -----\n')

start = perf_counter()
_result = []
_to_ignore = []
result = []

for i in src:
    if i not in _result:
        _result.append(i)
    else:
        _to_ignore.append(i)
_to_ignore = list(set(_to_ignore))
result = [element for element in _result if element not in _to_ignore]
print(result)
print(f'size: {sys.getsizeof(result)}, time: {perf_counter() - start}')

print('\n----- My bad code got smaller -----\n')

start = perf_counter()
_to_ignore = []
result = []

_to_ignore = list(set([item for item in src if src.count(item) > 1]))
result = [item for item in src if item not in _to_ignore]
print(result)
print(f'size: {sys.getsizeof(result)}, time: {perf_counter() - start}')
