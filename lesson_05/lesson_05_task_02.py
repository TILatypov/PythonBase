'''
2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
не используя ключевое слово yield.
'''

print('----- Task_02 -----')

n = 15
generated_number = (number for number in range(1, n + 1, 2))

print(type(generated_number))
print(*generated_number)
