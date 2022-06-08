'''
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида:
(<remote_addr>, <request_type>, <requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
'''

print('----- Task_01 -----')

with open('nginx_logs.txt', encoding='utf-8') as file:
    result_data = []
    for line in file:
        temp_data = []
        line = (line.replace('\n', ' ').replace('"', '')).split(' ')
        temp_data = [line[0], line[5], line[6]]
        result_data.append(tuple(temp_data))

for i in result_data:
    print(i)
