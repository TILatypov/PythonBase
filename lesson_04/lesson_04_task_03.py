'''
3. * (вместо 2) Доработать функцию currency_rates():
теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
'''

print('----- Task_03 -----')


import requests
import re
from datetime import datetime


def currency_rates(money_code):
    answer_request = (requests.get('http://www.cbr.ru/scripts/XML_daily.asp')).text
    answer_request_list = []
    pattern_symbol = '<Valute ID="'
    answer_contained_date = re.split(pattern_symbol, answer_request)[0]
    date = re.findall(r'\d{2}.\d{2}.\d{4}', answer_contained_date)[0]
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
        exchange_rate = re.findall("\d+.\d+", amount_of_money)[0]
        exchange_rate = float(exchange_rate.replace(',', '.'))
        return (f'Дата: {date}. Стоимость {amount} {money_code_from_massive} = {exchange_rate:.2f} дробных рублей типа float')


money_code_for_request = 'USD'
print(currency_rates(money_code_for_request))
money_code_for_request = 'EUR'
print(currency_rates(money_code_for_request))
money_code_for_request = 'ZBNG'
print(currency_rates(money_code_for_request))
