'''
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''

print('----- Task_03 -----')

class Worker:

    def __init__(self, name, surname, position, income, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': None, 'bonus': None}
        self._income['wage'] = income
        self._income['bonus'] = bonus

class Position(Worker):

    def get_full_name(self):
        return (f'Полное имя сотрудника: {self.name} {self.surname}, должность - {self.position}.')

    def get_total_income(self):
        return f"Доход сотрудника: {(self._income['wage'] + self._income['bonus'])}"
#        print(f'Доход сотрудника: {self._income}')


_test = Position('John', 'Smith', 'Slave', 100, 50)
print(_test.get_full_name())
print(_test.get_total_income())
