'''
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип:
одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл.
Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
'''

print('----- Task_03 -----')

file_users = open('users.csv', 'r', encoding='utf-8')
content_file_users = list(file_users.read().replace(',', ' ').split('\n'))
file_users.close()

file_hobby = open('hobby.csv', 'r', encoding='utf-8')
content_file_hobby = list(file_hobby.read().replace(',', ', ').split('\n'))
file_hobby.close()

while len(content_file_users) > len(content_file_hobby):
    content_file_hobby.append(None)

if len(content_file_users) < len(content_file_hobby):
    exit(1)

dict_result = {}

for user_names in content_file_users:
    key_user = user_names.split('\n')[0]
    dict_result.setdefault(key_user, None)

hobby_index = 0

for user_names, hobby in dict_result.items():
    if hobby == None:
        dict_result[user_names] = content_file_hobby[hobby_index]
        hobby_index += 1

file_result = open('result_3.csv', 'w+', encoding='utf-8')
for i in dict_result:
    to_write = str(i) + ': ' + str(dict_result[i]) + '\n'
    file_result.writelines(to_write)
file_result.seek(0)
print(file_result.read())
file_result.close()
