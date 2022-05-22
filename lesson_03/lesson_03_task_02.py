'''
2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы
— результат тоже должен быть с заглавной. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
'''

print('----- Task_02 -----')

base_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
}

def num_translate_adv(word):
    word_from_dict = word.lower()
    russian_word = base_dict.get(word_from_dict)
    if ord(word[0]) == ord(word_from_dict[0]):
        return print(russian_word)
    else:
        russian_word = russian_word.capitalize()
        return print(russian_word)

num_translate_adv('One')
num_translate_adv('two')
