'''
4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи,
в которых фамилия начинается с соответствующей буквы.
Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?
'''

print('----- Task_04 -----')


def thesaurus_adv(*names_surnames):

    result_dict = {}
    for name_surname in names_surnames:
        first_level_key_index = name_surname.find(' ') + 1
        first_level_key = name_surname[first_level_key_index]
        second_level_key = name_surname[0]

        result_dict.setdefault(first_level_key, {})
        result_dict[first_level_key].setdefault(second_level_key, [])
        result_dict[first_level_key][second_level_key].append(name_surname)

#        print(name_surname, first_level_key, second_level_key)              #шпаргалка

    print(f'Without sorting:\n{result_dict}\n')

# ---------- Нашел по запросу: "Python how to sort dictionary by key?" ----------
    sorted_result_dict = dict(sorted(result_dict.items(), key=lambda item: item[0]))

    print(f'Sorted result_dict:\n{sorted_result_dict}\n')

    return sorted_result_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Вахтанг Мюллер"))
