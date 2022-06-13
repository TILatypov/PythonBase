'''
3. Создать структуру файлов и папок, как написано в задании 2
(при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание,
что html-файлы расположены в родительских папках (они играют роль пространств имён);
предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
'''

print('----- Task_03 -----')


import os
import yaml
import shutil


''' ========== Конструктор структуры =========='''

def structure():
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

#structure()

''' ======================================== '''

sources_folder = r'lesson_07'
dir_name = 'templates'
adress_files = []
for r, d, f in os.walk('my_project'):
    for file in f:
        if not os.path.isfile(file) and '.html' in file:
            adress_files.append(os.path.join(r, file))

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

for i in adress_files:
    new_adress = os.path.join(dir_name, os.path.basename(os.path.dirname(i)))
    print(new_adress)
    if not os.path.exists(new_adress):
         os.mkdir(new_adress)
    shutil.copy2(i, os.path.join(new_adress, os.path.basename(i)))
