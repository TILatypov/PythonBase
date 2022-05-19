'''
3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться.
'''

print('----- Task_03 -----')

origin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
mark_plus = None
mark_minus = None
for i in origin_list:
    if i.__contains__('+'):
        mark_plus = True
    if i.__contains__('-'):
        mark_minus = True
    try:                                                # Попытка преобразовать элементы массива в тип integer
        element = str(int(i))
        if len(element) < 2:
            element = '0' + element
        elif len(element) == 2 and mark_plus == True:
            element = element[0] + '0' + element[1]
            mark_plus = None
        elif len(element) == 2 and mark_minus == True:
            element = element[0] + '0' + element[1]
            mark_minus = None
        if mark_plus == True:
            origin_list[index] = '"+' + element + '"'
            mark_plus = None
        else:
            origin_list[index] = '"' + element + '"'
        index += 1
    except ValueError:                                  # Ловим ошибку, которая возникает в результате int(i)
        index += 1                                      # если ошибка, значит не наш клиент, берем следующего.
print(' '.join(map(str, origin_list)))                  # Нашел по запросу "python how to output str list format to string"
