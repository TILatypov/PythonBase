'''
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
Известно, что имя сотрудника всегда в конце строки.
Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
Можно ли при этом не создавать новый список?
'''

print('----- Task_04 -----')

employee_base = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(employee_base)):
    employee_base[i] = employee_base[i].lower()

# ['инженер-конструктор игорь', 'главный бухгалтер марина', 'токарь высшего разряда николай', 'директор аэлита']

for i in employee_base:
    name = (i.split()[-1].title())
    print(f'Привет, {name}')