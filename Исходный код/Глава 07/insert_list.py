# Это программа демонстрирует метод insert.

def main():
    # Создать список с несколькими именами.
    names = ['Джеймс', 'Кэтрин', 'Билл']

    # Показать список.
    print('Список перед ставкой:')
    print(names)

    # Вставить новое имя в элемент 0.
    names.insert(0, 'Джо')

    # Показать список еще раз.
    print('Список после вставки:')
    print(names)

# Вызвать главную функцию.
main()