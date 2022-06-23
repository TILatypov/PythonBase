'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани.
Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
'''

print('----- Task_02 -----')


from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size_parameter):
        self.size_parameter = size_parameter

    @abstractmethod
    def fabric_consumption(self):
        print('Метод расчета расхода ткани')
        pass


class Coat(Clothes):

    @property
    def fabric_consumption(self):
        return f'Расход ткани на пашив пальто {self.size_parameter} размера: {round((self.size_parameter / 6.5) + 0.5, 2)} м кв.'


class Suit(Clothes):

    @property
    def fabric_consumption(self):
        return f'Расход ткани на пашив костюма для человека ростом {self.size_parameter}: {round((self.size_parameter / 100 * 2) + 0.3, 2)} м кв.'


coat = Coat(48)
suit = Suit(175)
print(coat.fabric_consumption)
print(suit.fabric_consumption)
