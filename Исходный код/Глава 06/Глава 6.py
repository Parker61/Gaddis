
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-


# # Глава 6. Файлы и исключения

# ## 6.1 Введение в файловый ввод и вывод

# ### Программа 6-1 (file_write.py)

# In[1]:


# Эта программа пишет три строки данных
# в файл.
def main():
    # Открыть файл с именем philosophers.txt.
    outfile = open('philosophers.txt', 'w')

    # Записать имена трех философов
    # в файл.
    outfile.write('Джон Локк\n')
    outfile.write('Дэвид Хьюм\n')
    outfile.write('Эдмунд Берк\n')

    # Закрыть файл.
    outfile.close()

# Вызвать главную функцию.
main() 


# ### Программа 6-2 (file_read.py)

# In[3]:


# Эта программа читает и показывает содержимое
# файла philosophers.txt.
def main():
    # Открыть файл с именем philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Прочитать содержимое файла.
    file_contents = infile.read()

    # Закрыть файл.
    infile.close()

    # Напечатать данные, прочитанные 
    # в оперативную память.
    print(file_contents)

# Вызвать главную функцию.
main()


# ### Программа 6-3 (line_read.py)

# In[4]:


# Эта программа построчно читает 
# содержимое файла philosophers.txt.
def main():
    # Открыть файл с именем philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Прочитать три строки файла.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Закрыть файл.
    infile.close()

    # Напечатать данные, считанные 
    # в оперативную память.
    print(line1)
    print(line2)
    print(line3)

# Вызвать главную функцию.
main() 


# ### Программа 6-4 (write_names.py)

# In[7]:


# Эта программа получает от пользователя три имени
# и пишет их в файл.

def main():
    # Получить три имени.
    print('Введите имена трех друзей.')
    name1 = input('Друг #1: ')
    name2 = input('Друг #2: ')
    name3 = input('Друг #3: ')

    # Открыть файл с именем friends.txt.
    myfile = open('friends.txt', 'w')

    # Записать имена в файл.
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    # Закрыть файл.
    myfile.close()
    print('Имена были записаны в friends.txt.')

# Вызвать главную функцию.
main()


# ### Program 6-5 (strip_newline.py)

# In[8]:


# Эта программа читает содержимое файла
# philosophers.txt построчно.
def main():
    # Открыть файл с именем philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Прочитать три строки из файла.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Удалить \n из каждого строкового значения.
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    # Закрыть файл.
    infile.close()

    # Напечатать данные, прочитанные в 
    # оперативную память.
    print(line1)
    print(line2)
    print(line3)

# Вызвать главный метод.
main()


# ### Программа 6-6 (write_numbers.py)

# In[9]:


# Эта программа демонстрирует конвертацию 
# числовых значений в строковые перед их
# записью в текстовый файл.

def main():
    # Открыть файл для записи.
    outfile = open('numbers.txt', 'w')

    # Получить от пользователя три числа.
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите еще одно число: '))
    num3 = int(input('Введите еще одно число: '))

    # Записать эти числа в файл.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    # Закрыть файл.
    outfile.close()
    print('Данные записаны в numbers.txt')

# Вызвать главную функцию.
main()


# ### Программа 6-7 (read_numbers.py)

# In[10]:


# Эта программа демонстрирует, как прочитанные из файла 
# числа конвертируются из строкового представления
# перед тем, как они используются в математической операции.

def main():
    # Открыть файл для чтения.
    infile = open('numbers.txt', 'r')

    # Прочитать три числа из файла.
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Закрыть файл.
    infile.close()

    # Сложить три числа.
    total = num1 + num2 + num3

    # Показать числа и их сумму.
    print('Числа:', num1, num2, num3)
    print('Их сумма:', total)

# Вызвать главную функцию.
main()


# ## 6.2 Применение циклов для обработки файлов

# ### Программа 6-8 (write_sales.py)

# In[12]:


# Эта программа предлагает пользователю ввести суммы 
# продаж и записывает эти суммы в файл sales.txt.

def main():
    # Получить количество дней.
    num_days = int(input('За какое количество дней ' +
                         'Вы располагаете продажами? '))

    # Открыть новый файл с именем sales.txt.
    sales_file = open('sales.txt', 'w')

    # Получить суммы продаж за каждый день и
    # записать их в файл.
    for count in range(1, num_days + 1):
        # Получить продажи за день.
        sales = float(input('Введите продажи за день №' +
                            str(count) + ': '))

        # Записать сумму продаж в файл.
        sales_file.write(str(sales) + '\n')

    # Закрыть файл.
    sales_file.close()
    print('Данные записаны в sales.txt.')

# Вызвать главную функцию.
main()


# ### Программа 6-9 (read_sales.py)

# In[13]:


# Эта программа читает все значения из
# файла sales.txt.

def main():
    # Открыть файл sales.txt для чтения.
    sales_file = open('sales.txt', 'r')

    # Прочитать первую строку из файла, но
    # пока не конвертировать в число. С начала нужно
    # выполнить проверку на пустое строковое значение.
    line = sales_file.readline()

    # Продолжать обработку до тех пор, пока из readline
    # не будет возвращена пустая строка.
    while line != '':
        # Конвертировать строку в число с плавающей точкой.
        amount = float(line)

        # Отформатировать и показать сумму.
        print(format(amount, '.2f'))

        # Прочитать следующую строку.
        line = sales_file.readline()

    # Закрыть файл.
    sales_file.close()

# Вызвать главную функцию.
main()


# ### Программа 6-10 (read_sales2.py)

# In[15]:


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


# ### Программа 6-11 (save_running_times.py)

# In[2]:


# Эта программа сохраняет последовательность, состоящую из
# длительностей видеоклипов, в файле video_times.txt.

def main():
    # Получить количество видеоклипов в проекте.
    num_videos = int(input('Сколько видеоклипов в проекте? '))

    # Открыть файл для записи длительностей видеоклипов.
    video_file = open('video_times.txt', 'w')

    # Получить длительность каждого видеоклипа
    # и записать его в файл.
    print('Введите длительность каждого видеоклипа.')
    for count in range(1, num_videos + 1):
        run_time = float(input('Видеоклип №' + str(count) + ': '))
        video_file.write(str(run_time) + '\n')

    # Закрыть файл.
    video_file.close()
    print('Времена сохранены в video_times.txt.')

# Вызвать главную функцию.
main()


# ### Программа 6-12 (read_running_times.py)

# In[3]:


# Эта программа читает значения в файле 
# video_times.txt и вычисляет их сумму.

def main():
    # Открыть файл video_times.txt для чтения.
    video_file = open('video_times.txt', 'r')

    # Инициализировать накопитель значением 0.0.
    total = 0.0

    # Инициализировать переменную для подсчета видеоклипов.
    count = 0

    print('Длительности всех видеоклипов:')

    # Получить значения из файла и их просуммировать.
    for line in video_file:
        # Преобразовать строку в число с плавающей точкой.
        run_time = float(line)

        # Прибавить 1 к переменной count.
        count += 1

        # Показать длительность.
        print('Видеоклип №', count, ': ', run_time, sep='')

        # Прибавить длительность к total.
        total += run_time

    # Закрыть файл.
    video_file.close()

    # Показать итоговую длительность.
    print('Общая длительность составляет', total, 'секунд.')

# Вызвать главную функцию.
main()


# ## 6.3 Обработка записей

# ### Программа 6-13 (save_emp_records.py)

# In[1]:


# Эта программа получает от пользователя данные о сотрудниках
# и их сохраняет в виде записей в файле employee.txt.

def main():
    # Получить количество записей о сотрудниках для создания.
    num_emps = int(input('Сколько записей о сотрудниках ' +
                         'Вы хотите создать? '))

    # Открыть файл для записи.
    emp_file = open('employees.txt', 'w')

    # Получить данные каждого сотрудника и
    # записать их в файл.
    for count in range(1, num_emps + 1):
        # Получить данные о сотруднике.
        print('Введите данные о сотруднике №', count, sep='')
        name = input('Имя: ')
        id_num = input('Идентификационный номер: ')
        dept = input('Отдел: ')

        # Записать в файл данные как запись.
        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        # Показать пустую строку.
        print()

    # Закрыть файл.
    emp_file.close()
    print('Записи о сотрудниках записаны в employees.txt.')

# Вызвать главную функцию.
main()


# ### Программа 6-14 (read_emp_records.py)

# In[4]:


# Эта программа показывает записи, которые
# находятся в файле employees.txt.

def main():
    # Открыть файл employees.txt.
    emp_file = open('employees.txt', 'r')

    # Прочитать первую строку в файле, т.е.
    # поле с именем сотрудника первой записи.
    name = emp_file.readline()

    # Если поле прочитано, то продолжить обработку.
    while name != '':
        # Прочитать поле с идентификационным номером.
        id_num = emp_file.readline()

        # Прочитать поле с названием отдела.
        dept = emp_file.readline()

        # Удалить символы новой строки из полей.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Показать запись.
        print('Имя:', name)
        print('ИД:', id_num)
        print('Отдел:', dept)
        print()

        # Прочитать поле с именем следующей записи.
        name = emp_file.readline()

    # Закрыть файл.
    emp_file.close()

# Вызвать главную функцию.
main()


# ### Программа 6-15 (add_coffee_record.py)

# In[6]:


# Эта программа добавляет записии о запасах кофе
# в файл coffee.txt.

def main():
    # Создать переменную для управления циклом.
    another = 'д'

    # Открыть файл coffee.txt file в режиме дозаписи.
    coffee_file = open('coffee.txt', 'a')

    # Добавить записи в файл.
    while another == 'д' or another == 'Д':
        # Получить данные с записью о кофе.
        print('Введите следующие данные о кофе:')
        descr = input('Описание: ')
        qty = int(input('Количество (в фунтах): '))

        # Добавить данные в файл.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Определить, желает ли пользователь добавить 
        # в файл еще одну запись.
        print('Желаете ли Вы добавить еще одну запись?')
        another = input('Д = да, все остальное = нет: ')

    # Закрыть файл.
    coffee_file.close()
    print('Данные добавлены в coffee.txt.')

# Вызвать главную функцию.
main()


# ### Программа 6-16 (show_coffee_records.py)

# In[7]:


# Эта программа показывает записи в 
# файле coffee.txt. 

def main():
    # Открыть файл coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Прочитать поле с описанием первой записи.
    descr = coffee_file.readline()

    # Прочитать остаток файла.
    while descr != '':
        # Прочитать поле с количеством.
        qty = float(coffee_file.readline())

        # Удалить \n из описания.
        descr = descr.rstrip('\n')

        # Показать запись.
        print('Описание:', descr)
        print('Количество:', qty)

        # Прочитать следующее описание.
        descr = coffee_file.readline()

    # Закрыть файл.
    coffee_file.close()

# Вызвать главную функцию.
main()


# ### Программа 6-17 (search_coffee_records.py)

# In[1]:


# Эта программа позволяет пользователю производить поиск
# в файле coffee.txt file записей, которые соответствуют
# описанию.

def main():
    # Создать булеву переменную для использования в качестве фла-га.
    found = False

    # Получить искомое значение.
    search = input('Введите искомое описание: ')

    # Открыть файл coffee.txt.
    coffee_file = open('coffee.txt', 'r')

    # Прочитать поле с описанием кофе первой записи.
    descr = coffee_file.readline()

    # Прочитать остаток файла.
    while descr != '':
        # Прочитать поле с количеством.
        qty = float(coffee_file.readline())

        # Удалить \n из описания.
        descr = descr.rstrip('\n')

        # Определить, соответствует ли эта запись
        # поисковому значению.
        if descr == search:
            # Показать запись.
            print('Описание:', descr)
            print('Количество:', qty)
            print()
            # Назначить флагу found значение True.
            found = True

        # Прочитать следующее описание.
        descr = coffee_file.readline()

    # Закрыть файл.
    coffee_file.close()

    # Если поисковое значение в файле не найдено,
    # то показать сообщение.
    if not found:
        print('Это значение в файле не найдено.')

# Вызвать главную функцию.
main()


# ### Программа 6-18 (modify_coffee_records.py)

# In[1]:


# Эта программа позволяет пользователю изменять количество
# в записи в файле coffee.txt.

import os # Это модуль нужен для функций remove и rename

def main():
    # Создать булеву переменную для использования в качестве фла-га.
    found = False

    # Получить искомое значение и новое количество.
    search = input('Введите искомое описание: ')
    new_qty = int(input('Введите новое количество: '))

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

        # Записать во временный файл либо эту запись,
        # либо новую запись, если эта запись 
        # подлежит изменению.
        if descr == search:
            # Записать измененную запись во временный файл.
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')

            # Назначить флагу found значение True.
            found = True
        else:
            # Записать исходную запись во временный файл.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')

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


# ### Программа 6-19 (delete_coffee_record.py)

# In[2]:


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


# ## 6.4 Исключения

# ### Программа 6-20 (division.py)

# In[3]:


# Эта программа делит одно число на другое.

def main():
    # Получить два числа.
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите еще одно число: '))

    # Разделить num1 на num2 и показать результат.
    result = num1 / num2
    print(num1, 'деленое на', num2, 'равняется', result)

# Вызвать главную функцию.
main()


# ### Программа 6-21 (division2.py)

# In[4]:


# Эта программа делит одно число на другое.

def main():
    # Получить два числа.
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите еще одно число: '))

    # Если переменная num2 не равна 0, то разделить 
    # num1 на num2 и показать результат.
    if num2 != 0:
        result = num1 / num2
        print(num1, 'деленое', num2, 'равняется', result)
    else:
        print('Нельзя делить на ноль.')

# Вызвать главную функцию.
main()


# ### Программа 6-22 (gross_pay1.py)

# In[5]:


# Эта программа вычисляет заработную плату до удержаний.

def main():
    # Получить количество отработанных часов.
    hours = int(input('Сколько часов вы отработали? '))

    # Получить почасовую ставку оплаты труда.
    pay_rate = float(input('Введите свою почасовую ставку: '))

    # Вычислить заработную плату до удержаний.
    gross_pay = hours * pay_rate

    # Показать заработную плату.
    print('Заработная плата: $', format(gross_pay, ',.2f'), sep='')

# Вызвать главную функцию.
main()


# ### Программа 6-23 (gross_pay2.py)

# In[6]:


# Эта программа вычисляет заработную плату до удержаний.

def main():
    try:
        # Получить количество отработанных часов.
        hours = int(input('Сколько часов вы отработали? '))

        # Получить почасовую ставку оплаты труда.
        pay_rate = float(input('Введите свою почасовую ставку: '))

        # Вычислить заработную плату до удержаний.
        gross_pay = hours * pay_rate

        # Показать заработную плату.
        print('Зарплата: $', format(gross_pay, ',.2f'), sep='')
    except ValueError:
        print('ОШИБКА: Отработанные часы и почасовая ставка оплаты')
        print('должны быть допустимыми числами.')

# Вызвать главную функцию.
main()


# ### Программа 6-24 (display_file.py)

# In[9]:


# Эта программа показывает содержимое
# файла.

def main():
    # Получить имя файла.
    filename = input('Введите имя файла: ')

    # Открыть файл.
    infile = open(filename, 'r')

    # Прочитать содержимое файла.
    contents = infile.read()

    # Показать содержимое файла.
    print(contents)

    # Закрыть файл.
    infile.close()

# Вызвать главную функцию.
main()


# ### Программа 6-25 (display_file2.py)

# In[10]:


# Эта программа показывает содержимое
# файла.

def main():
    # Получить имя файла.
    filename = input('Введите имя файла: ')
 
    try:
        # Открыть файл.
        infile = open(filename, 'r')

        # Прочитать содержимое файла.
        contents = infile.read()

        # Показать содержимое файла.
        print(contents)

        # Закрыть файл.
        infile.close()
    except IOError:
        print('Произошла ошибка при попытке прочитать')
        print('файл', filename)

# Вызвать главную функцию.
main()  


# ### Программа 6-26 (sales_report1.py)

# In[14]:


# Эта программа показывает итоговый объем
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

        # Распечатать итог.
        print(format(total, ',.2f'))

    except IOError:
        print('Произошла ошибка при попытке прочитать файл.')

    except ValueError:
        print('В файле найдены нечисловые данные.')

    except:
        print('Произошла ошибка.')

# Вызвать главную функцию.
main()


# ### Программа 6-27 (sales_report2.py)

# In[13]:


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

        # Напечатать итооговую сумму.
        print(format(total, ',.2f'))
    except:
        print('Произошла ошибка.')

# Вызвать главную функцию.
main()


# ### Программа 6-28 (gross_pay3.py)

# In[11]:


# Эта программа вычисляет заработную плату до удержаний.

def main():
    try:
        # Получить количество отработанных часов.
        hours = int(input('Сколько часов вы отработали? '))

        # Получить почасовую ставку оплаты труда.
        pay_rate = float(input('Введите почасовую ставку: '))

        # Вычислить заработную плату.
        gross_pay = hours * pay_rate

        # Показать заработную плату.
        print('Зарплата: $', format(gross_pay, ',.2f'), sep='')
    except ValueError as err:
        print(err)

# Вызвать главную функцию.
main()


# ### Программа 6-29 (sales_report3.py)

# In[12]:


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


# ### Программа 6-30 (sales_report4.py)

# In[15]:


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
    except Exception as err:
        print(err)
    else:
        # Напечатать итоговую сумму.
        print(format(total, ',.2f'))

# Вызвать главную функцию.
main()

