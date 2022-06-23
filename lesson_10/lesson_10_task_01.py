'''
Урок 10. Объектно-ориентированное программирование. Продвинутый уровень
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
'''

print('----- Task_01 -----')


class Matrix:
    def __init__(self, matrix_input):
        self.matrix = matrix_input

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.matrix])

    def __add__(self, other):
        result = ''
        if len(self.matrix) == len(other.matrix):
            for line_1, line_2 in zip(self.matrix, other.matrix):
                if len(line_1) == len(line_2):
                    summed_line = [x + y for x, y in zip(line_1, line_2)]
                    result += ' '.join(map(str, summed_line)) + '\n'
                else:
                    return 'Мтарицы разного размера складывать нельзя.'
        else:
            return 'Мтарицы разного размера складывать нельзя.'
        return result


first_matrix = Matrix([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
second_matrix = Matrix([[3, 2, 1], [4, 3, 2], [5, 4, 3], [-4, -5, -6]])
print(f'Матрица №1:\n{first_matrix}\n')
print(f'Матрица №2:\n{second_matrix}\n')
print(f'Результат сложения матриц:\n{first_matrix + second_matrix}')

first_matrix = Matrix([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6, 8]])
print(f'Матрица №1:\n{first_matrix}\n')
print(f'Матрица №2:\n{second_matrix}\n')
print(f'Результат сложения матриц:\n{first_matrix + second_matrix}')
