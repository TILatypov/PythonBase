'''
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде
<r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
(должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
'''

print('----- Task_05 -----')

prices = [57.8, 46.51, 97, 35.7, 102.23, 10.3, 55.65, 50, 81.94, 26.13, 50, 68.02]

original_id_of_prices = id(prices)

'---------- Functions ----------'

def units_of_cost(prices_list):
    for i in range(len(prices_list)):
        ruble = str(int(prices_list[i]) // 1)
        kopeck = str(int(prices_list[i] * 100 % 100))
        if len(kopeck) == 1:
            kopeck = '0' + kopeck
        prices_list[i] = (f'{ruble} руб {kopeck} коп')
    return prices_list

def remove_units_of_cost(prices_list):
    for i in range(len(prices_list)):
        prices_list[i] = prices_list[i].replace(' руб ', '.')
        prices_list[i] = prices_list[i].replace(' коп', '')
    return prices_list

def add_units_of_cost(prices_list):
    for i in range(len(prices_list)):
        prices_list[i] = prices_list[i].replace('.', ' руб ')
        prices_list[i] = prices_list[i] + ' коп'
    return prices_list

print('---------- Adding units of cost and id verify ----------')

print(', '.join(units_of_cost(prices)))

after_add_units_of_cost_id = id(prices)

if original_id_of_prices == after_add_units_of_cost_id:
    print('Объект списка после добавления единиц измерения стоимости - прежний')
else:
    print('Объект списка после добавления единиц измерения стоимости - изменился')

print('---------- Sorting prices array and id verify ----------')

sorted_prices = (sorted(remove_units_of_cost(prices), key=float))

before_sorted_id = id(sorted_prices)

print(add_units_of_cost(sorted_prices))

after_sorted_id = id(sorted_prices)

if before_sorted_id == after_sorted_id:
    print('Объект списка после после сортировки, удаления единиц стоимости и последующего добавления - прежний')
else:
    print('Объект списка после сортировки, удаления единиц стоимости и последующего добавления - изменился')

print('---------- Create new list and elements sorting ----------')

new_prices = [57.8, 46.51, 97, 35.7, 102.23, 10.3, 55.65, 50, 81.94, 26.13, 50, 68.02]

new_prices = sorted(new_prices)
new_prices.reverse()
print(', '.join(units_of_cost(new_prices)))

for i in range(0, 4):
    print(new_prices[i])
