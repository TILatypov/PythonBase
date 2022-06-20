'''
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''

print('----- Task_02 -----')


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        DENSITY = 2.5 # т/м*3
        HIGHT = 0.15 # м
        mass = f'Требуемая масса асфальта: {self._length * self._width * HIGHT * DENSITY} тонн'
        return mass


mass_of_asphalt = Road(100, 10)
print(mass_of_asphalt.asphalt_mass())
