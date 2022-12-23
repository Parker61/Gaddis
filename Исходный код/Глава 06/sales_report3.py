# Эта программа показывает итоговую сумму
# продаж в файле sales_data.txt.

def main():
    # Инициализировать накопитель.
    total = 0.0

    try:
        # Открыть файл sales_data.txt.
        infile = open('sales_data.txt', 'r')

        # Прочитать значения из файла и 
        # накопить их в переменной.
        for line in infile:
            amount = float(line)
            total += amount

        # Закрыть файл.
        infile.close()

        # Напечатать итоговую сумму.
        print(format(total, ',.2f'))
    except Exception as err:
        print(err)

# Вызвать главную функцию.
main()