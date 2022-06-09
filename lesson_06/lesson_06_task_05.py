'''
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
'''

print('----- Task_05 -----')

from itertools import zip_longest
import sys


# users, hobby, result_5 = sys.argv[1:]
# "\lesson_06> python .\lesson_06_task_05.py ".\users.csv" ".\hobby.csv" ".\result_5.csv" - вызов из PyCharm Terminal
# Если в разных папках - дописываем путь в терминале относительно каталога в котором запускаем Python (предположение)

with open('result_5.csv', 'w', encoding='utf-8') as file_result:
    with open('users.csv', 'r', encoding='utf-8') as file_users:
        with open('hobby.csv', 'r', encoding='utf-8') as file_hobby:
            users_lines = sum(1 for line in file_users)
            hobby_lines = sum(1 for line in file_hobby)
            file_users.seek(0)
            file_hobby.seek(0)
            if users_lines < hobby_lines:
                exit(1)

            for user_line, hobby_line in zip_longest(file_users, file_hobby):
                if hobby_line != None:
                    key_user_line = user_line.replace(',', ', ').replace('\n', ':')
                    print(key_user_line)
                    dict_hobby_line = hobby_line.replace(',', ', ').replace('\n', '')
                    print(dict_hobby_line)
                else:
                    key_user_line = user_line.replace(',', ', ')
                    key_user_line = key_user_line + ':'
                    print(key_user_line)
                    dict_hobby_line = None
                    print(dict_hobby_line)
                file_result.write(f'{key_user_line} {dict_hobby_line}\n')

#"\lesson_06> python .\lesson_06_task_05.py ".\users.csv" ".\hobby.csv" ".\result_5.csv" - вызов из PyCharm Terminal
