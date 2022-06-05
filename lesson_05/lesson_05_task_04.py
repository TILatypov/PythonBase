'''
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке.
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
'''

print('----- Task_04 -----')


import sys
from time import perf_counter


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print('----- With using a loop "for" - it is a first variant of my bad code -----')
start = perf_counter()
result = []
i = 1
for i in range(0, len(src) - 1):
    if src[i] < src[i + 1]:
        result.append(src[i + 1])
    i += 1
print(result)
print(f'size: {sys.getsizeof(result)}, time: {perf_counter() - start}')

print(' ----- Start of optimization my bad code by "list comprehension" -----')

start = perf_counter()
result = []
index = [i for i in range(1, len(src) - 1) if src[i - 1] < src[i]]
for i in index:
    result.append(src[i])
print(result)
print(f'size: {sys.getsizeof(result)}, time: {perf_counter() - start}')

print(' ----- My bad code is finished -----')

#for i, num in enumerate(src):
#    print(f'{i} - {num}')
start = perf_counter()
result = [element for i, element in enumerate(src) if element > src[i - 1]]
del result[0]
print(result)
print(f'size: {sys.getsizeof(result)}, time: {perf_counter() - start}')
