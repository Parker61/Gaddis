
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-


# # Глава 5. Функции

# ## 5.2	Определение и вызов пустой функции

# ### Программа 5-1 (function_demo.py)

# In[1]:


# Эта программа демонстрирует функцию.
# Сначала мы определяем функцию с именем message.
def message():
    print('Я - Артур,')
    print('король британцев.')

# Вызвать функцию message.
message()


# ### Программа 5-2 (two_functions.py)

# In[4]:


# Эта программа имеет две функции. Сначала мы
# определяем главную функцию. 
def main():
    print('У меня для вас известие.')
    message()
    print('До свидания!')

# Затем мы определяем функцию message. 
def message():
    print('Я – Артур,') 
    print('король британцев.')

# Вызвать функцию
main() 


# ## 5.3 Разработка программы с использованием функций

# ### Программа 5-3 (acme_dryer.py)

# In[1]:


# Эта программа показывает пошаговые инструкции
# для разборке бельевой сушилки фирмы Acme.
# Главная функция выполняет основную логику программы.
def main():
    # Показать стартовое сообщение.
    startup_message()
    input('Нажмите Enter, чтобы увидеть Шаг 1.')
    # Показать шаг 1.
    step1()
    input('Нажмите Enter, чтобы увидеть Шаг 2.')
    # Показать шаг 2.
    step2()
    input('Нажмите Enter, чтобы увидеть Шаг 3.')
    # Показать шаг 3.
    step3()
    input('Нажмите Enter, чтобы увидеть Шаг 4.')
    # Показать шаг 4.
    step4()

# Функция startup_message показывает
# первоначальное сообщение программы на экране.
def startup_message():
    print('Эта программа дает рекомендации по')
    print('разборке бельевой сушилки фирмы ACME.')
    print('Данный процесс состоит из 4 шагов.')
    print()

# Функция step1 показывает инструкции
# для шага 1.
def step1():
    print('Шаг 1: Отключить сушилку и')
    print('отодвинуть ее от стены.')
    print()

# Функция step2 показывает инструкции
# для шага 2.
def step2():
    print('Шаг 2: Удалить шесть винтов')
    print('с задней стороны сушилки.')
    print()

# Функция step3 показывает инструкции
# для шага 3.
def step3():
    print('Шаг 3: Удалить заднюю панель')
    print('сушилки.')
    print()

# Функция step4 показывает инструкции
# для шага 4.
def step4():
    print('Шаг 4: Вынуть верхний блок')
    print('сушилки.')

# Вызвать функцию main, чтобы начать программу.
main()


# ## 5.4 Локальные переменные

# ### Программа 5-4 (bad_local.py)

# In[11]:


# Определение главной функции.
def main():
    get_name()
    print('Привет,', name) # Это вызовет ошибку!

# Определение функции get_name.
def get_name():
    name = input('Введите свое имя: ')

# Вызвать функцию main.
main()


# ### Программа 5-5 (birds.py)

# In[13]:


# Эта программ демонстрирует две функции, которые
# имеют локальные переменные с одинаковыми именами.

def main():
    # Вызвать функцию texas.
    texas()
    # Вызвать функцию california.
    california()

# Определение функции texas. Она создает
# локальную переменную с именем birds.
def texas():
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')

# Определение функции california. Она тоже
# создает локальную переменную с именем birds.
def california():
    birds = 8000
    print('В Калифорнии обитает', birds, 'птиц.')

# Вызвать функцию main.
main()


# ## 5.5 Передача аргументов в функцию 

# ### Программа 5-6 (pass_arg.py)

# In[14]:


# Это программа демонстрирует аргумент,
# передаваемый в функцию.

def main():
    value = 5
    show_double(value)

# Функция show_double принимает аргумент
# и показывает его удвоенное значение.
def show_double(number):
    result = number * 2
    print(result)

# Вызвать функцию main.
main()


# ### Программа 5-7 (cups_to_ounces.py)

# In[3]:


# Эта программа конвертирует чашки в жидкие унции.

def main():
    # Показать вводное окно.  
    intro()
    # Получить количество чашек.
    cups_needed = int(input('Введите количество чашек: '))
    # Конвертировать чашки в унции.
    cups_to_ounces(cups_needed)

# Функци intro показывает вводное окно.
def intro():
    print('Эта программа конвертирует замеры')
    print('в чашках в жидкие унции. Для')
    print('справки приводим формулу:')
    print(' 1 чашка = 8 жидких унций')
    print()

# Функция cups_to_ounces принимает количество чашек
# и показывает эквивалентное количество унций.
def cups_to_ounces(cups):
    ounces = cups * 8
    print('Это конвертируется в', ounces, 'унции(й).')

# Вызвать функцию main.
main()


# ### Программа 5-8 (multiple_args.py)

# In[5]:


# Эта программа демонстрирует функцию, которая принимает
# два аргумента.

def main():
    print('Сумма чисел 12 и 45 равняется')
    show_sum(12, 45)

# Функция show_sum принимает два аргумента
# и показывает их сумму.
def show_sum(num1, num2):
    result = num1 + num2
    print(result)

# Вызвать функцию main.
main()


# ### Программа 5-9 (string_args.py)

# In[6]:


# Эта программа демонстрирует передачу в функцию двух 
# строковых аргумента.

def main():
    first_name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    print('Ваше имя в обратном порядке')
    reverse_name(first_name, last_name)

def reverse_name(first, last):
    print(last, first)

# Вызвать функцию main.
main()


# ### Программа 5-10 (change_me.py)

# In[8]:


# Эта программа демонстрирует, что происходит, когда вы
# изменяете значение параметра.

def main():
    value = 99
    print('Значение равняется', value)
    change_me(value)
    print('Вернувшись в функцию main, значение равняется', value)

def change_me(arg):
    print('Я изменяю значение.')
    arg = 0
    print('Теперь значение равняется', arg)

# Вызвать функцию main.
main()


# ### Программа 5-11 (keyword_args.py)

# In[1]:


# Эта программа демонстрирует именованные аргументы.

def main():
    # Показать сумму простого процентного дохода, используя 
    # 0.01 как процентной ставки за период, 10 как количество
    # периодов и $10,000 в как основную сумму на счету.
    show_interest(rate=0.01, periods=10, principal=10000.0)

# Функция show_interest показывает сумму простого процентного
# дохода для заданной основной суммы, процентной ставки
# за период и количество периодов.

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print('Простой процентный доход составит $',
          format(interest, ',.2f'),
          sep='')

# Вызвать функцию main.
main()


# ### Программа 5-12 (keyword_string_args.py)

# In[11]:


# Эта программа демонстрирует передачу в функцию двух 
# строковых значений в качестве именованных аргументов.

def main():
    first_name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    print('Ваше имя в обратном порядке')
    reverse_name(last=last_name, first=first_name)

def reverse_name(first, last):
    print(last, first)

# Вызвать функцию main.
main()


# ## 5.6 Глобальные переменные и глобальные константы

# ### Программа 5-13 (global1.py)

# In[12]:


# Создать глобальную переменную.
my_value = 10

# Функция show_value печатает
# значение глобальной переменной.
def show_value():
    print(my_value)

# Вызвать функцию show_value.
show_value()


# ### Программа 5-14 (global2.py)

# In[13]:


# Создать глобальную переменную.
number = 0

def main():
    global number
    number = int(input('Введите число: '))
    show_number()

def show_number():
    print('Вы ввели число', number)

# Вызвать функцию main.
main()


# ### Программа 5-15 (retirement.py)

# In[6]:


# Следующее используется в качестве глобальной константы
# Ставка взноса компании.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Введите заработную плату: '))
    bonus = float(input('Введите сумму премий: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# Функция show_pay_contrib принимает заработную
# плату в качестве аргумента и показывает взнос
# в пенсионные накопления исходя из этого размера оплаты.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Взнос исходя из заработной платы: $',
          format(contrib, ',.2f'),
          sep='')

# Функция show_bonus_contrib принимает сумму премий
# в качестве аргумента и показывает взнос в
# пенсионное накопление исходя из этой суммы оплаты.
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print('Взнос исходя из суммы премий: $',
          format(contrib, ',.2f'),
          sep='')

# Вызвать функцию main.
main()


# ## 5.7 Введение в функции с возвратом значения: генерирование случайных чисел

# ### Программа 5-16 (random_numbers.py)

# In[15]:


# Эта программа показывает случайное число
# в диапазоне от 1 до 10.
import random

def main():
    # Получить случайное число.
    number = random.randint(1, 10)
    # Показать число.
    print('Число равняется', number)

# Вызвать функцию main.
main()


# ### Программа 5-17 (random_numbers2.py)

# In[16]:


# Эта программа показывает пять случайных
# чисел в диапазоне от 1 до 100.
import random

def main():
    for count in range(5):
        # Получить случайное число.
        number = random.randint(1, 100)
        # Показать число.
        print(number)

# Вызвать функцию main.
main()


# ### Программа 5-18 (random_numbers3.py)

# In[17]:


# Эта программа показывает пять случайных
# чисел в диапазоне от 1 до 100.
import random

def main():
    for count in range(5):
        print(random.randint(1, 100))

# Вызвать функцию main.
main() 


# ### Программа 5-19 (dice.py)

# In[7]:


# Эта программа бросает кубики.
import random

# Константы для минимального и максимального случайных чисел
MIN = 1
MAX = 6

def main():
    # Создать переменную, которая управляет циклом.
    again = 'д'

    # Имитировать бросание кубиков.
    while again == 'д' or again == 'Д':
        print('Бросаем кубики...')
        print('Значения граней:')
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))

        # Сделать еще один бросок кубиков?
        again = input('Бросить кубики еще раз? (д = да): ')

# Вызвать функцию main.
main()


# ### Программа 5-20 (coin_toss.py)

# In[20]:


# Эта программа имитирует 10 бросков монеты.
import random

# Константы
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        # Имитировать бросание монеты.
        if random.randint(HEADS, TAILS) == HEADS:
            print('Орел')
        else:
            print('Решка')

# Вызвать функцию main.
main()


# ## 5.8 Написание своих собственных функций с возвратом значения

# ### Программа 5-21 (total_ages.py)

# In[2]:


# Эта программа использует возвращаемое значение функции.

def main():
    # Получить возраст пользователя.
    first_age = int(input('Введите свой возвраст: '))

    # Получить возраст лучшего друга пользователя.
    second_age = int(input("Введите возраст своего лучшего друга: "))

    # Получить сумму обоих возрастов.
    total = sum(first_age, second_age)

    # Показать общий возраст.
    print('Вместе вам', total, 'лет.')

# Функция sum принимает два числовых аргумента и
# возвращает сумму этих аргументов.
def sum(num1, num2):
    result = num1 + num2
    return result

# Вызвать функцию main.
main()


# ### Программа 5-22 (sale_price.py)

# In[22]:


# Эта программа вычисляет отпускную цену 
# розничого товара.

# DISCOUNT_PERCENTAGE используется в качестве
# глобальной константы для процента скидки.
DISCOUNT_PERCENTAGE = 0.20

# Главная функция.
def main():
    # Получить регулярную цену товара.
    reg_price = get_regular_price()

    # Рассчитать отпускную цену.
    sale_price = reg_price - discount(reg_price)

    # Показать отпускную цену.
    print('Отпускная цена составляет $', 
          format(sale_price, ',.2f'), sep='')

# Функция get_regular_price предлагает пользователю
# ввести регулярную цену товара, и она возвращает
# это значение.
def get_regular_price():
    price = float(input("Введите регулярную цену товара: "))
    return price

# Функция discount принимает цену товара в качестве
# аргумента и возвращает сумму скидки
# указанной в DISCOUNT_PERCENTAGE.
def discount(price):
    return price * DISCOUNT_PERCENTAGE

# Вызвать главную функцию.
main()


# ### Программа 5-23 (commission_rate.py)

# In[28]:


# Эта программа вычисляет выплату продавцу
# в компании 'Делай свою музыку'.
def main():
    # Получить сумму продаж.
    sales = get_sales()

    # Получить сумму авансовой оплаты.
    advanced_pay = get_advanced_pay()

    # Определить ставку комиссионных.
    comm_rate = determine_comm_rate(sales)

    # Рассчитать оплату.
    pay = sales * comm_rate - advanced_pay

    # Показать сумму выплаты.
    print('Выплата составляет $', format(pay, ',.2f'), sep='')

    # Определить, является ли выплата отрицательной.
    if pay < 0:
        print('Продавец должен возместить разницу')
        print('компании.')

# Функция get_sales получает от пользователя 
# месячные продажи продавца и возвращает это значение.
def get_sales():
    # Получить сумму месячных продаж.
    monthly_sales = float(input('Введите сумму месячных продаж: '))

    # Вернуть введенную сумму.
    return monthly_sales

# Функция get_advanced_pay получает сумму 
# авансовой выплаты конкретному продавцу и 
# возвращает эту сумму.
def get_advanced_pay():
    # Получить сумму авансовой выплаты.
    print('Введите сумму авансовой выплаты либо')
    print('введите 0, если такой выплаты не было.')
    advanced = float(input('Авансовая выплата: '))

    # Вернуть введенную сумму.
    return advanced

# Функция determine_comm_rate принимает сумму продаж
# в качестве аргумента и возвращает подходящую
# ставку комиссионных.
def determine_comm_rate(sales):
    # Определить ставку комиссионных.
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18

    # Вернуть ставку комиссионных.
    return rate

# Вызвать главную функцию.
main()


# ## 5.9 Математический модуль math 

# ### Программа 5-24 (square_root.py)

# In[31]:


# Эта программа демонстрирует функцию sqrt.
import math

def main():
   # Получить число.
   number = float(input('Введите число: '))

   # Получить квадратный корень числа.
   square_root = math.sqrt(number)

   # Показать квадратный корень.
   print('Квадратный корень из', number, 'составляет', square_root)

# Вызвать главную функцию.
main()


# ### Программа 5-25 (hypotenuse.py)

# In[33]:


# Эта программа вычисляет длину равнобедренного
# прямоугольного треугольника.
import math

def main():
    # Получить длину двух сторон треугольника.
    a = float(input('Введите длину стороны A: '))
    b = float(input('Введите длину стороны B: '))

    # Вычислить длину гипотенузы.
    c = math.hypot(a, b)

    # Показать длину гипотенузы.
    print('Длина гипотенузы составляет', c)

# Вызвать главную функцию.
main()


# ## 5.10 Хранение функций в модулях

# ### Программа 5-26 (circle.py)

# In[38]:


# Модуль circle содержит функции, которые выполняют
# вычисления, связанные с кругами.
import math

# Функция area принимает радиус круга в качестве
# аргумента и возвращает площадь круга.
def area(radius):
    return math.pi * radius**2

# Функция circumference принимает радиус круга
# и возвращает окружность круга.
def circumference(radius):
    return 2 * math.pi * radius


# ### Программа 5-27 (rectangle.py)

# In[39]:


# Модуль rectangle содержит функции, которые выполняют
# вычисления, связанные с прямоугольниками.

# Функция area принимает ширину и длину прямоугольника
# в качестве аргументов и возвращает площадь прямоугольника.
def area(width, length):
    return width * length

# Функция perimeter принимает ширину и длину прямоугольника
# в качестве аргументов и возвращает периметр 
# прямоугольника.
def perimeter(width, length):
    return 2 * (width + length)


# ### Программа 5-28 (geometry.py)

# In[1]:


# Эта программа позволяет пользователю выбирать различные
# геометрические вычисления из меню. Эта программа
# Импортирует моудли circle и rectangle.
import circle
import rectangle

# Константы для элементов меню
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

# Главная функция.
def main():
    # Переменная choice управляет циклом
    # и содержит вариант выбора пользователя.
    choice = 0

    while choice != QUIT_CHOICE:
        # Показать меню.
        display_menu()

        # Получить вариант выбора пользователя.
        choice = int(input('Введите ваш выбор: '))

        # Выполнить выбранное действие.
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("Введите радиус круга: "))
            print('Площадь равна', circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Введите радиус круга: "))
            print('Окружность равна',
                  circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("Введите ширину прямоугольника: "))
            length = float(input("Введите длину прямоугольника: "))
            print('Площадь равна', rectangle.area(width, length))
        elif choice == PERIMETER_RECTANGLE_CHOICE:
            width = float(input("Введите ширину прямоугольника: "))
            length = float(input("Введите длину прямоугольника: "))
            print('Периметр равен',
                  rectangle.perimeter(width, length))
        elif choice == QUIT_CHOICE:
            print('Выходим из программы...')
        else:
            print('Ошибка: недопустимый выбор.')

# Функция display_menu показывает меню.
def display_menu():
    print(' МЕНЮ')
    print('1) Площадь круга')
    print('2) Окружность круга')
    print('3) Площадь прямоугольника')
    print('4) Периметр прямоугольника')
    print('5) Выход')

# Вызвать главную функцию.
main()


# ## 5.11 Черепашья графика: модуляризация кода при помощи функций

# ### Программа 5-29 (draw_squares.py)

# In[1]:


import turtle

def main():
    turtle.hideturtle()
    square(100, 0, 50, 'red')
    square(-150, -100, 200, 'blue')
    square(-200, 150, 75, 'green')

# Функция square рисует квадрат. 
# Параметры x и y - это координаты левого нижнего угла. 
# Параметр width - это ширина стороны квадрата. 
# Параметр color - это цвет заливки в видек строки.

def square(x, y, width, color):
    turtle.penup()             # Поднять перо
    turtle.goto(x, y)          # Переместить в указанное место
    turtle.fillcolor(color)    # Задать цвет заливки
    turtle.pendown()           # Опустить перо
    turtle.begin_fill()        # Начать заливку
    for count in range(4):     # Нарисовать квадрат
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()          # Завершить заливку

# Вызвать главную функцию.
main()


# ### Программа 5-30 (draw_circles.py)

# In[2]:


import turtle

def main():
    turtle.hideturtle()
    circle(0, 0, 100, 'red')
    circle(-150, -75, 50, 'blue')
    circle(-200, 150, 75, 'green')

# Функция circle рисует круг. 
# Параметры x и y - это координаты центральной точки.
# Параметр radius - это радиус круга. 
# Параметр color - это цвет заливки в виде строки.

def circle(x, y, radius, color):
    turtle.penup()              # Поднять перо
    turtle.goto(x, y - radius)  # Спозиционировать черепаху
    turtle.fillcolor(color)     # Задать цвет заливки
    turtle.pendown()            # Опустить перо
    turtle.begin_fill()         # Начать заливку
    turtle.circle(radius)       # Нарисовать круг
    turtle.end_fill()           # Завершить заливку

# Вызвать главную функцию.
main()


# ### Программа 5-31 (draw_lines.py) 

# In[2]:


import turtle

# Именованные константы для точек треугольника
TOP_X = 0
TOP_Y = 100
BASE_LEFT_X  = -100
BASE_LEFT_Y  = -100
BASE_RIGHT_X =  100
BASE_RIGHT_Y = -100

def main():
    turtle.hideturtle()
    line(TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y, 'red')
    line(TOP_X, TOP_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'blue')
    line(BASE_LEFT_X, BASE_LEFT_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'green')

# Функция line рисует отрезок от (startX, startY) до (endX, endY).
# Параметр color – это цвет отрезка.
def line(startX, startY, endX, endY, color):
    turtle.penup()               # Поднять перо
    turtle.goto(startX, startY)  # Переместить в начальную точку
    turtle.pendown()             # Опустить перо
    turtle.pencolor(color)       # Задать цвет заливки
    turtle.goto(endX, endY)      # Нарисовать треугольник

# Вызвать главную функцию.
main()


# ### Программа 5-32 (my_graphics.py)

# In[ ]:


# Функции черепашьей графики
import turtle

# Функция square рисует квадрат. 
# Параметры x и y - это координаты левого нижнего угла. 
# Параметр width - это ширина стороны квадрата. 
# Параметр color - это цвет заливки в виде строки.

def square(x, y, width, color):
    turtle.penup()             # Поднять перо
    turtle.goto(x, y)          # Переместить в указанное место
    turtle.fillcolor(color)    # Задать цвет заливки
    turtle.pendown()           # Опустить перо
    turtle.begin_fill()        # Начать заливку
    for count in range(4):     # Нарисовать квадрат
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()          # Завершить заливку

# Функция circle рисует круг. 
# Параметры x и y - это координаты центральной точки.
# Параметр radius - это радиус круга. 
# Параметр color - это цвет заливки в виде строки.

def circle(x, y, radius, color):
    turtle.penup()              # Поднять перо
    turtle.goto(x, y - radius)  # Спозиционировать черепаху
    turtle.fillcolor(color)     # Задать цвет заливки
    turtle.pendown()            # Опустить перо
    turtle.begin_fill()         # Начать заливку
    turtle.circle(radius)       # Нарисовать круг
    turtle.end_fill()           # Завершить заливку

# Функция line рисует линию от (startX, startY) до (endX, endY).
# Параметр color – это цвет линии.

def line(startX, startY, endX, endY, color):
    turtle.penup()               # Поднять перо
    turtle.goto(startX, startY)  # Переместить в начальную точку
    turtle.pendown()             # Опустить перо
    turtle.pencolor(color)       # Задать цвет заливки
    turtle.goto(endX, endY)      # Нарисовать треугольник


# ### Программа 5-33 (graphics_mod_demo.py)

# In[2]:


import turtle
import my_graphics

# Именованные константы
X1 = 0
Y1 = 100
X2 = -100
Y2 = -100
X3 = 100
Y3 = -100
RADIUS = 50

def main():
    turtle.hideturtle()

    # Нарисовать квадрат.
    my_graphics.square(X2, Y2, (X3 - X2), 'gray')

    # Нарисовать несколько кругов.
    my_graphics.circle(X1, Y1, RADIUS, 'blue')
    my_graphics.circle(X2, Y2, RADIUS, 'red')
    my_graphics.circle(X3, Y3, RADIUS, 'green')

    # Нарисовать несколько линий.
    my_graphics.line(X1, Y1, X2, Y2, 'black')
    my_graphics.line(X1, Y1, X3, Y3, 'black')
    my_graphics.line(X2, Y2, X3, Y3, 'black')

main()

