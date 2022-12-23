# Эта программа применяет цикл for для чтения
# всех значений в файле sales.txt.

def main():
    # Открыть файд sales.txt для чтения.
    sales_file = open('sales.txt', 'r')

    # Прочитать все строки из файла.
    for line in sales_file:
        # Конвертировать строку в число с плавающей точкой.
        amount = float(line)
        # Отформатировать и показать сумму.
        print(format(amount, '.2f'))

    # Закрыть файл.
    sales_file.close()

# Вызвать главную функцию.
main()