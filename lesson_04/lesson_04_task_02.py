'''
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.
'''

print('----- Task_02 -----')


import requests
import re


'''
=======================================================================================
Первое решение методами класса str - выводит доли копеек. С ходу исправить не получилось.           - Работает.
Функция должна возвращать результат числового типа, например float.                                 - реализовано в _task_03.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?   - Вероятно, есть.
Сильно ли усложняется код функции при этом?                                                         - Не проверял.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.                 - Возвращает.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?        - Работает.
В качестве примера выведите курсы доллара и евро.                                                   - Работает.
=======================================================================================
'''


def currency_rates(money_code):
    answer_request = (requests.get('http://www.cbr.ru/scripts/XML_daily.asp')).text
    answer_request_list = []
    pattern_symbol = '<Valute ID="'
    answer_request_list = re.split(pattern_symbol, answer_request)[1:]
    for answer in answer_request_list:
        pattern_symbol = '</NumCode><CharCode>'
        answer = re.split(pattern_symbol, answer)
        answer = str(answer[1])
        money_code_from_massive = answer[:3]
        if str(money_code_from_massive) != str(money_code).upper():
            continue
        pattern_symbol = '</CharCode><Nominal>'
        answer = re.split(pattern_symbol, answer)
        amount_of_money = str(answer[1])
        amount = ''
        for i in amount_of_money:
            if i.isdigit():
                amount = str(amount) + str(i)
            else:
                break
        pattern_symbol = '</Name><Value>'
        exchange_rate = re.split(pattern_symbol, amount_of_money)
        pattern_symbol = '</Value></Valute>'
        exchange_rate = re.split(pattern_symbol, str(exchange_rate[1]))[0]
        return (f'Стоимость {amount} {money_code_from_massive} - {exchange_rate} рублей')


money_code_for_request = 'USD'
print(currency_rates(money_code_for_request))
money_code_for_request = 'EUR'
print(currency_rates(money_code_for_request))
money_code_for_request = 'ZBNG'
print(currency_rates(money_code_for_request))
