# Эта программа вызывает метод split, используя
# символ '/' в качестве разделителя.

def main():
   # Создать строковое значение с датой.
   date_string = '01/12/2018'

   # Разбить дату.
   date_list = date_string.split('/')

   # Показать все части даты.
   print('День:', date_list[0])
   print('Месяц:', date_list[1])
   print('Год:', date_list[2])

# Вызвать главную функцию.
main()