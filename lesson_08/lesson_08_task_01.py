'''
1. Написать функцию email_parse(<email_address>),
которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError.
Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
'''

print('----- Task_01 -----')


import re


def email_parse(email_address):
    email_parse_dict = {}
    validate = RE_EMAIL.match(email_address)
    if validate:
        email_parse_dict['username'] = RE_USERNAME.findall(email_address)[0]
        email_parse_dict['domain'] = RE_DOMAIN.findall(email_address)[0]
    else:
        raise ValueError(f'wrong email: {email_address}')
    return email_parse_dict


pattern_email = r'([A-Za-z0-9_]+)+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+'
pattern_username = r'([A-Za-z0-9_]+)+@'
pattern_domain = r'@([A-Za-z0-9]+\.[A-Z|a-z]{2,})+'

RE_EMAIL = re.compile(pattern_email)
RE_USERNAME = re.compile(pattern_username)
RE_DOMAIN =re.compile(pattern_domain)

print(email_parse('someone@geekbrains.ru'))
print(email_parse('s_Ome_oNe@geekBrains2022.ru'))
print(email_parse('s_Ome_oNe!@geekBrains2022.ru'))
