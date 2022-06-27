"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random


''' ========== Card =========='''


class Card:
    cell = 9
    numbers_in_line = 5
    line = 3
    data = []
    empty = '  '


    def __init__(self):
        random_number_array = []
        counter_gen = self.line * self.numbers_in_line
        counter = 0
        while counter < counter_gen:
            random_number = random.randint(1, 90)
            if random_number not in random_number_array:
                random_number_array.append(random_number)
                counter += 1
            else:
                continue

        self.data = []
        for i in range(0, self.line):
            temp = sorted(random_number_array[self.numbers_in_line * i: self.numbers_in_line * (i + 1)])
            empty_nums_count = self.cell - self.numbers_in_line
            for j in range(0, empty_nums_count):
                index = random.randint(0, len(temp))
                temp.insert(index, self.empty)
            self.data += temp


    def __str__(self):
        delimiter = '=============================='
        random_number_array = delimiter + '\n'
        for index, num in enumerate(self.data):
            if num == self.empty:
                random_number_array += '  '
            else:
                random_number_array += str(num)

            if (index + 1) % self.cell == 0:
                random_number_array += '\n'
            else:
                random_number_array += ' '

        return random_number_array + delimiter


''' ========== LottoBarrel =========='''


class LottoBarrel:
    barrel_number = None


    def __init__(self):
        self.barrel_number = random.randint(1, 90)


    def number(self):
        return self.barrel_number


    def __str__(self):
        return str(self.barrel_number)


''' ========== First Step Test Output =========='''


player_card = Card()
computer_card = Card()
barrel = LottoBarrel()

print(f'======= Player Card =======\n{player_card}\n')
print(f'======= Computer Card =======\n{computer_card}')
print(f'Вытащили бочонок № {barrel}')
player_answer = input('Зачеркиваем? (y/n)').lower().strip()

