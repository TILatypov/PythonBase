'''
Написать регулярное выражение для парсинга файла логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
'''

print('----- Task_02 -----')


import re


def file_parse(file):
    with open(file, encoding='utf-8') as file:
        file_parse_array = []
        for line in file:
            _temp = []
            _temp.append(RE_PARSE_FILE_IP.findall(line)[0])
            _temp.append(RE_PARSE_FILE_TIME.findall(line)[0])
            _temp.append(RE_PARSE_FILE_GET.findall(line)[0])
            _temp.append(RE_PARSE_FILE_PATH.findall(line)[0])
            _temp.append(RE_PARSE_FILE_END.findall(line)[0][1])
            _temp.append(RE_PARSE_FILE_END.findall(line)[0][2])
            file_parse_array.append(_temp)
    return (file_parse_array)

# Слишком длинное выражение, пришлось разбить на части

pattern_ip = r'((?:[0-9]{,3}[.]){3}[0-9]{,3})'
pattern_time = r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}])'
pattern_get = r'[GET]{3}'
pattern_path = r'[/\[A-Za-z]+]{0,}[/\[A-Za-z]+]{0,}[_][0-9]+'
pattern_end = r'(([0-9]{3}) ([0-9]+))'

RE_PARSE_FILE_IP = re.compile(pattern_ip)
RE_PARSE_FILE_TIME = re.compile(pattern_time)
RE_PARSE_FILE_GET = re.compile(pattern_get)
RE_PARSE_FILE_PATH = re.compile(pattern_path)
RE_PARSE_FILE_END = re.compile(pattern_end)

file_for_parse = 'nginx_logs.txt'

print(file_parse(file_for_parse))
