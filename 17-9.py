
def findPosition(num_list, number, first, last):
    try:
        if first > last:
            return False
        middle = (first + last) // 2
        if num_list[middle] == number:
            return middle
        elif number < num_list[middle]:
            return findPosition(num_list, number, first, middle-1)
        else:
            return findPosition(num_list, number, middle + 1, last)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'

s = input("Ведите последовательность целых чисел через пробел: ")
number = int(input("Ведите любое целое число: "))
num_list = [int(x) for x in s.split()]
num_list = sorted(num_list)

print(f'Список элементов по возрастанию: {num_list}')


if not findPosition(num_list, number, 0, len(num_list)):
    rI = min(num_list, key=lambda x: (abs(x - number), x))
    ind = num_list.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < number:
        print(f'''Введенного элемента нет в списке
Ближайший больший элемент: {num_list[max_ind]} индекс: {max_ind}
Ближайший меньший элемент: {rI}, индекс: {ind}''')
    elif min_ind < 0:
        print(f'''Введенного элемента нет в списке
Ближайший больший элемент: {rI}, индекс: {num_list.index(rI)}
В списке нет меньшего элемента''')
    elif rI > number:
        print(f'''Введенного элемента нет в списке
Ближайший больший элемент: {rI}, индекс: {num_list.index(rI)}
Ближайший меньший элемент: {num_list[min_ind]} индекс: {min_ind}''')
    elif num_list.index(rI) == 0:
        print(f'Индекс введенного элемента: {num_list.index(rI)}')
else:
    print(f'Индекс введенного элемента: {findPosition(num_list, number, 0, len(num_list))}')
