'''
Есть два списка:
tutors = [
'Иван', 'Анастасия', 'Петр', 'Сергей',
'Дмитрий', 'Борис', 'Елена'
]
klasses = [
'9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>),
например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors.
Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
кортежи в виде: (<tutor>, None),
например:
('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
'''

print('----- Task_03 -----')


from itertools import zip_longest


tutors = [
'Иван', 'Анастасия', 'Петр', 'Сергей',
'Дмитрий', 'Борис', 'Елена'
]
klasses = [
'9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tutors_klasses = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
# print(type(tutors_klasses))                 # <class 'generator'>
# print(tutors_klasses)                       # <generator object <genexpr> at 0x000002270852C6D0>
group = tuple(tutors_klasses)
# print(type(group))                          # <class 'tuple'>
print(group)
