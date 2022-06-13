'''
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
'''

print('----- Task_04 -----')


import os


size_dict = {10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0}
files_size = []
for r, d, f in os.walk('./my_project'):
    for file in f:
        file_path = os.path.join(r, file)
        files_size.append(os.stat(file_path).st_size)
max_size = max(files_size)

previous_key = 0

for key in size_dict.keys():
    for i in files_size:
        if previous_key <= i < key:
            size_dict[key] += 1
    previous_key = key

print(size_dict)
