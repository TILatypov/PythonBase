'''
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
'''

print('----- Task_01 -----')


def odd_numbers_generator(max_number):
    for number in range(1, max_number + 1, 2):
        yield number


required_number = 15
odd_num_gen_to_n = odd_numbers_generator(required_number)

for i in odd_num_gen_to_n:
     print(i)

print('----- Next generation -----')

required_number = 7
odd_num_gen_to_n = odd_numbers_generator(required_number)

print(next(odd_num_gen_to_n))
print(next(odd_num_gen_to_n))
print(next(odd_num_gen_to_n))
print(next(odd_num_gen_to_n))
print(next(odd_num_gen_to_n))
