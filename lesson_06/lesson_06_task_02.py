'''
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов;
код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''

print('----- Task_02 -----')

with open('nginx_logs.txt', encoding='utf-8') as file:
    dict_to_detect_spammer = {}
    for line in file:
        ip_key = (line.split(' '))[0]
        if ip_key not in dict_to_detect_spammer:
            dict_to_detect_spammer.setdefault(ip_key, 1)
        else:
            dict_to_detect_spammer[ip_key] = dict_to_detect_spammer[ip_key] + 1
request_max = max(dict_to_detect_spammer.values())
for ip_key, value in dict_to_detect_spammer.items():
    if value == request_max:
        print(f'С IP {ip_key} отправлено наибольшее количество запросов - {request_max}.')
