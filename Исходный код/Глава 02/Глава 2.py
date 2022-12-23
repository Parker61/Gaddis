
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-


# # Глава 2. Ввод, обработка и вывод

# ## 2.3	Вывод выходных данных при помощи функции print

# ### Программа 2-1 (output.py)

# In[34]:


print('Дед Мороз')   
print('162390, Россия, Вологодская область, г. Великий Устюг')
print('ул. Снежная, 20-18')


# ### Программа 2-2 (double_quotes.py)

# In[35]:


print("Дед Мороз")
print("162390, Россия, Вологодская область, г. Великий Устюг")
print("ул. Снежная, 20-18")


# ### Программа 2-3 (apostrophe.py)

# In[4]:


print("Из всех рассказов О'Генри")
print("мне больше нравится 'Вождь краснокожих'.")


# ### Программа 2-4 (display_quote.py)

# In[5]:


print('Домашнее задание на завтра – прочитать "Гамлет".')


# ## 2.4 Комментарии

# ### Программа 2-5 (comment1.py)

# In[36]:


# Эта программа показывает
# фио и адрес человека.
print('Дед Мороз')
print('162390, Россия, Вологодская область, г. Великий Устюг')
print('ул. Снежная, 20-18')


# ### Программа 2-6 (comment2. py)

# In[37]:


print('Дед Мороз') # Показать фио.
print('162390, Россия, Вологодская область, г. Великий Устюг') # Показать индекс, город.
print('ул. Снежная, 20-18') # Показать адрес проживания.


# ## 2.5 Переменные

# ### Программа 2-7 (variable_demo.py)

# In[8]:


# Эта программа демонстрирует переменную.
room = 503
print('Я нахожусь в комнате номер')
print(room)


# ### Программа 2-8 (variable_demo2.py)

# In[9]:


# Создать две переменные: top_speed и distance.
top_speed = 160
distance = 300

# Показать значения, на которые ссылаются переменные.
print('Предельная скорость составляет')
print(top_speed)
print('Пройденное расстояние составляет')
print(distance)  


# ### Программа 2-9 (variable_demo3.py)

# In[10]:


# Эта программа демонстрирует переменную.
room = 503
print('Я нахожусь в комнате номер', room)


# ### Программа 2-10 (variable_demo4.py)

# In[2]:


# Эта программа показывает повторное присвоение значения переменной.
# Присвоить значение переменной roubles.
roubles = 12.75
print('У меня счете', roubles, 'рублей.')
 
# Повторно присвоить значение переменной roubles, 
# чтобы оно ссылалось на другое значение.
roubles = 990.95
print('А теперь там', roubles, 'рублей!')


# ### Программа 2-11 (string_variable.py)

# In[17]:


# Создать переменные, которые ссылаются на два строковых значения.
first_name = 'Кэтрин'
last_name = 'Марино'
 
# Показать значения, на которые эти переменные ссылаются.
print(first_name, last_name)


# ## 2.6 Чтение входных данных с клавиатуры

# ### Программа 2-12 (string_input.py)

# In[19]:


# Получить имя пользователя.
first_name = input('Введите свое имя: ')
 
# Получить фамилию пользователя.
last_name = input('Введите свою фамилию: ')
 
# Напечатать пользователю приветствие.
print('Привет,', first_name, last_name)


# ### Программа 2-13 (input.py)

# In[20]:


# Получить имя, возраст и доход пользователя.
name = input('Как Вас зовут? ')
age = int(input('Сколько Вам лет? '))
income = float(input('Какой у Вас доход? '))
 
# Вывод данных на экран.
print('Вот данные, которые Вы ввели:')
print('Имя:', name)
print('Возраст:', age)
print('Доход:', income)


# ## 2.7 Выполнение расчетов

# ### Программа 2-14 (simple_math.py)

# In[21]:


# Присвоить значение переменной salary.
salary = 25000.0

# Присвоить значение переменной bonus.
bonus = 12000.0

# Рассчитать заработную плату до удержаний, сложив salary
# и bonus. Присвоить результат переменной pay.
pay = salary + bonus

# Вывести переменную pay.
print('Ваша заработная плата составляет', pay)


# ### Программа 2-15 (sale_price.py)

# In[23]:


# Эта программа получает исходную цену товара и
# вычисляет его отпускную цену с 20%-й скидкой.

# Получить исходную цена товара.
original_price = float(input("Введите исходную цену товара: "))

# Вычислить сумму скидки.
discount = original_price * 0.2

# Вычислить отпускную цену.
sale_price = original_price - discount

# Показать отпускную цену.
print('Отпускная цена составляет', sale_price)


# ### Программа 2-16 (test_score_average.py)

# In[1]:


# Получить три оценки и присвоить их переменным
# test1, test2 и test3.
test1 = float(input('Введите первую оценку: '))
test2 = float(input('Введите вторую оценку: '))
test3 = float(input('Введите третью оценку: '))

# Вычислить средний балл из трех оценок
# и присвоить результат переменной average.
average = (test1 + test2 + test3) / 3.0

# Показать переменную average.
print('Средний балл составляет', average)


# ### Программа 2-17 (time_converter.py)

# In[25]:


# Получить от пользователя количество секунд.
total_seconds = float(input('Введите количество секунд: '))
 
# Получить количество часов.
hours = total_seconds // 3600
 
# Получить количество оставшихся минут.
minutes = (total_seconds // 60) % 60

# Получить количество оставшихся секунд.
seconds = total_seconds % 60

# Показать результаты.
print('Вот время в часах, минутах и секундах:')
print('Часы:', hours)
print('Минуты:', minutes)
print('Секунды:', seconds)


# ### Программа 2-18 (future_value.py)

# In[38]:


# Получить требуемое будущее значение.
future_value = float(input('Введите требуемое будущее значение: '))

# Получить годовую процентную ставку.
rate = float(input('Введите годовую процентную ставку: '))

# Получить количество лет роста стоимости денег.
years = int(input('Введите количество лет роста стоимости денег: '))

# Рассчитать сумму, необходимую для внесения на счет.
present_value = future_value / (1.0 + rate)**years

# Показать сумму, необходимую для внесения на счет.
print('Вам потребуется внести сумму:', present_value)


# ## 2.8 Подробнее о выводе данных

# ### Программа 2-19 (no_formatting.py)

# In[28]:


# Эта программа демонстрирует как число 
# с плавающей точкой выводится без форматирования.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print('Ежемесячный платеж составляет', monthly_payment)


# ### Программа 2-20 (formatting.py)

# In[29]:


# Эта программа демонстрирует, как может быть 
# отформатировано число с плавающей точкой.
amount_due = 5000.0
monthly_payment = amount_due / 12
print('Ежемесячный платеж составляет',
      format(monthly_payment, '.2f'))


# ### Программа 2-21 (dollar_display.py)

# In[31]:


# Эта программа демонстрирует, как число с плавающей точкой 
# может быть отформатировано в качестве валюты.
monthly_pay = 30000.0
annual_pay = monthly_pay * 12
print('Ваша годовая заработная плата составляет $',
      format(annual_pay, ',.2f'),
      sep='')


# ### Программа 2-22 (columns.py)

# In[32]:


# Эта программа выводит приведенные ниже
# числа с плавающей точкой в столбце,
# в котором десятичные знаки выровнены.
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Вывести каждое число в поле шириной 7 пробелов
# с 2 десятичными знаками.
print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))


# ## 2.10	Введение в черепашью графику

# ### Программа 2-23 (orion.py)

# In[33]:


# Эта программа наносит звезды созвездия Ориона,
# названия звезд и линии созвездия.
import turtle

# Задать размер окна.
turtle.setup(500, 600)

# Установить черепаху.
turtle.penup()
turtle.hideturtle()

# Создать именованные константы для звездных координат.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Нанести звезды.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # Левое плечо 
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) # Правое плечо 
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) # Левая звезда в поясе 
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) # Средняя звезда в поясе
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) # Правая звезда в поясе 
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) # Левое колено 
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) # Правое колено 
turtle.dot()

# Вывести названия звезд.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # Левое плечо 
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) # Правое плечо 
turtle.write('Хатиса')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) # Левая звезда в поясе
turtle.write('Альнитак')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) # Средняя звезда в поясе
turtle.write('Альнилам')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) # Правая звезда в поясе
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) # Левое колено
turtle.write('Саиф')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) # Правое колено
turtle.write('Ригель')

# Нанести линию из левого плеча в левую звезду пояса
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из правого плеча в правую звезду пояса
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из левой звезды пояса в среднюю звезду пояса
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

# Нанести линию из средней звезды пояса в правую звезду пояса
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из левой звезды пояса в левое колено
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# Нанести линию из правой звезды пояса в правое колено
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

# Оставить окно открытым. (В среде IDLE не требуется.)
turtle.done()

