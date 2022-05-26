'''
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?
'''
import random

print('----- Task_05 -----')

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


''' =============== BEGINNING OF FUNCTIONS AREA =============== '''

def get_jokes(joke_amount):
    joke = []
    for i in range(joke_amount):
        nous_joke = random.choice(nouns)
        adverbs_joke = random.choice(adverbs)
        adjectives_joke = random.choice(adjectives)
        joke.append(f'{nous_joke} {adverbs_joke} {adjectives_joke}')
    return joke


# Согласен, удаление из списка - плохое решение, но предварительное перемешивание было рассмотрено
def get_jokes_advanced(joke_amount, without_repeat):
    joke_advanced = []
    if without_repeat == True:
        if min(len(nouns), len(adverbs), len(adjectives)) > joke_amount:
            for i in range(joke_amount):
                nous_joke = random.choice(nouns)
                nouns.remove(nous_joke)
                adverbs_joke = random.choice(adverbs)
                adverbs.remove(adverbs_joke)
                adjectives_joke = random.choice(adjectives)
                adjectives.remove(adjectives_joke)
                joke_advanced.append(f'{nous_joke} {adverbs_joke} {adjectives_joke}')
            return joke_advanced
        else:
            return 'Недостаточно шуток, чтобы развеселить вас - продолжайте страдать!'
    else:
        return get_jokes(joke_amount)

''' =============== END OF FUNCTIONS AREA =============== '''


print(get_jokes(7))
print(get_jokes_advanced(5, True))
