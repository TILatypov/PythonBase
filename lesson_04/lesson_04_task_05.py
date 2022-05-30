'''
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
Например:
> python task_4_5.py USD
75.18, 2020-09-05
'''

print('----- Task_05 -----')


import sys
import utils


value = sys.argv[1]
utils.currency_rates(value)
