'''
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
Также реализовать парсинг данных из файлов —
получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби:
преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
Обосновать выбор типа.
Подумать, какие могут возникнуть проблемы при парсинге.
В словаре должны храниться данные, полученные в результате парсинга.
'''

print('----- Task_04 -----')


from itertools import zip_longest


with open('result_4.csv', 'w', encoding='utf-8') as file_result:
    with open('users.csv', 'r', encoding='utf-8') as file_users:
        with open('hobby.csv', 'r', encoding='utf-8') as file_hobby:
            users_lines = sum(1 for line in file_users)
            hobby_lines = sum(1 for line in file_hobby)
            file_users.seek(0)
            file_hobby.seek(0)
            if users_lines < hobby_lines:
                exit(1)

# Вероятно, логично было бы преобразовать в отдельный список ФИО и хобби,
# такой подход позволит выдергивать элементы по индексу

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
