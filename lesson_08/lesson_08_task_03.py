'''
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую;
можете ли вы вывести тип значения функции?
Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''

print('----- Task_03 -----')


from functools import wraps


def type_logger(func):
    print(func)
    @wraps(func)

    def wrapper(arg):
        print('=========================')
        print(f'Function name: {func.__name__}; \nArgument type: {type(arg)};')
        return func(arg)
    return wrapper


@type_logger
def calc_cube(arg):
    result = arg ** 3
    return result


print(f'Result of calculation: {calc_cube(5)}; \nResult type: {type(calc_cube(5))}')
print(f"Don't wrapper, it's '{calc_cube.__name__}'")
