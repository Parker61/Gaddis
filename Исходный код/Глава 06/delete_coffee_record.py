# Эта программа позволяет пользователю удалить
# запись в файле coffee.txt.

import os # Этот модуль нужен для функций remove и rename

def main():
    # Создать булеву переменную для использования в качестве флага.
    found = False

    # Получить бренд кофе, которые нужно удалить.
    search = input('Какой бренд кофе Вы желаете удалить? ')

    # Открыть исходный файл coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Открыть временный файл.
    temp_file = open('temp.txt', 'w')

    # Прочитать поле с описанием первой записи.
    descr = coffee_file.readline()

    # Прочитать остаток файла.
    while descr != '':
        # Прочитать поле с количеством.
        qty = float(coffee_file.readline())

        # Удалить \n из описания.
        descr = descr.rstrip('\n')

        # Если эта запись не предназначена для удаления,
        # то записать ее во временный файл.
        if descr != search:
            # Записать исходную запись во временный файл.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        else:
            # Назначить флагу found значение True.
            found = True

        # Прочитать следующее описание.
        descr = coffee_file.readline()

    # Закрыть файл с данными о кофе и временный файл.
    coffee_file.close()
    temp_file.close()

    # Удалить исходный файл coffee.txt.
    os.remove('coffee.txt')

    # Переименовать временный файл.
    os.rename('temp.txt', 'coffee.txt')

    # Если искомое значение в файле не найдено,
    # то показать сообщение.
    if found:
        print('Файл обновлен.')
    else:
        print('Это значение в файле не найдено.')

# Вызвать главную функцию.
main()