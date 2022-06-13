'''
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
'''

'''
"Мутная" формулировка: "подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?)" - сценарий
при котором в проекте была удалена папка. Поэтому проверка на наличие upper_folder (root_project), а затем восстановление
подкаталогов.
'''


print('----- Task_01 -----')


import os


sample_path = os.path.join('lesson_07')
sample = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
upper_folder = list(sample.keys())
subfolders = sample[upper_folder[0]]

try:
    os.mkdir(upper_folder[0])
except FileExistsError:
    print(f'Папка с именем {upper_folder[0]} уже существует.')
finally:
    for i in subfolders:
        sample_path = os.path.join(upper_folder[0], i)
        if not os.path.exists(sample_path):
            os.makedirs(sample_path)
