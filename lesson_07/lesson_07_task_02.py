'''
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами,
его можно создать в любом текстовом редакторе «руками» (не программно);
предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
'''
'''
... pip install pyyaml
PS ...\Основы языка Python\PythonBase> pip freeze
certifi==2022.5.18.1
charset-normalizer==2.0.12
distlib==0.3.4
filelock==3.7.0
idna==3.3
Pillow==9.0.0
platformdirs==2.5.2
PyYAML==6.0
requests==2.27.1
six==1.16.0
urllib3==1.26.9
virtualenv==20.14.1
'''

print('----- Task_02 -----')


import os
import yaml


def structure_creator(structure):
    for folder, folders in structure.items():
        try:
            os.mkdir(folder)
            print(folder)
        except FileExistsError:
            print(f'Папка с именем {folder} уже существует.')
        finally:
            os.chdir(folder)
        for subfolder in folders:
            if type(subfolder) == dict:
                structure_creator(subfolder)
            else:
                if not os.path.exists(subfolder) and not os.path.isfile(subfolder):
                    with open(subfolder, 'w') as f:
                        f.write('It_is_a_file')
    else:
        os.chdir('../')





structure = {'my_project':
                        [{'settings': ['__init__.py', 'dev.py', 'prod.py'],
                         },
                        {'mainapp': ['__init__.py', 'models.py', 'views.py', {'templates': [
                                                                                            {'mainapp': [
                                                                                            'base.html', 'index.html']}]}]},
                        {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [
                                                                                             {'authapp': [
                                                                                             'base.html', 'index.html']}]}]}
                        ]
            }

with open('config.yaml', 'w', encoding='utf-8') as f:
    documents = yaml.dump(structure, f)

with open('config.yaml', encoding='utf-8') as f_config:
    structure = yaml.full_load(f_config)
    print(structure)

structure_creator(structure)
