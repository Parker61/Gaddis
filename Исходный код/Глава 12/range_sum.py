# Эта программа демонстрирует функцию range_sum.

def main():
    # Создать список чисел.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Получить сумму значений в индексных
    # позициях, начиная с 2 вплоть до 5.
    my_sum = range_sum(numbers, 2, 5)

    # Показать сумму.
    print('Сумма значений со 2 по 5 позиции равняется', my_sum)

# Функция range_sum возвращает сумму заданного
# диапазона значений в списке num_list. Параметр start
# задает индексную позицию начального значения.
# Параметр end задает индексную позицию конечного значения.
def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

# Вызвать главную функцию.
main()