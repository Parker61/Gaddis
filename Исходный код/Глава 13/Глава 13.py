
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-


# # Глава 13. Программирование графического пользовательского интерфейса 

# ## 13.2	Использование модуля tkinter

# ### Программа 13-1 (empty_window1.py)

# In[1]:


# Эта программа показывает пустое окно.

import tkinter

def main():
    # Создать элемент интерфейса главного окна.
    main_window = tkinter.Tk()

    # Войти в главный цикл tkinter.
    tkinter.mainloop()

# Вызвать главную программу.
main()


# ### Программа 13-2 (empty_window2.py)

# In[2]:


# Эта программа показывает пустое окно.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ## 13.3 Вывод текста при помощи элемента интерфейса Label

# ### Программа 13-3 (hello_world.py)

# In[5]:


# Эта программа показывает надпись с текстом.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Label, содержащий
        # надпись 'Привет, Мир!'
        self.label = tkinter.Label(self.main_window,
                                   text='Привет, мир!')

        # Вызвать метод pack  элемента интерфейса Label.
        self.label.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI() 


# ### Программа 13-4 (hello_world2.py)

# In[6]:


# Эта программа показывает два элемента Label с текстом.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать два элемента интерфейса Label.
        self.label1 = tkinter.Label(self.main_window,
                                    text='Привет, мир!')
        self.label2 = tkinter.Label(self.main_window,
                        text='Это моя программа с ГИП.')

        # Вызвать метод pack обоих элементов интерфейса Label.
        self.label1.pack()
        self.label2.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-5 (hello_world3.py)

# In[7]:


# Эта программа изпользует аргумент side='left' в
# методе pack для изменения размещения элементов интерфейса.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать два элемента интерфейса Label.
        self.label1 = tkinter.Label(self.main_window,
                                    text='Привет, мир!')
        self.label2 = tkinter.Label(self.main_window,
                        text='Это моя программа с ГИП.')

        # Вызвать метод pack обоих элементов интерфейса Label.
        self.label1.pack(side='left')
        self.label2.pack(side='left')

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ## 13.4 Упорядочение элементов интерфейса при помощи рамок Frame

# ### Программа 13-6 (frame_demo.py)

# In[8]:


# Эта программа создает надписи в двух разных рамках.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать две рамки, одну для верхней части 
        # окна, и другую для нижней части.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать три элемента интерфейса Label
        # для верхней рамки.
        self.label1 = tkinter.Label(self.top_frame,
                                    text='Мигнуть')
        self.label2 = tkinter.Label(self.top_frame,
                                    text='Моргнуть')
        self.label3 = tkinter.Label(self.top_frame,
                                    text='Кивнуть')

        # Упаковать надписи, расположенные в верхней рамке.
        # Применить аргумент side='top', чтобы их
        # расположить один под другим.
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # Создать три элемента интерфейса Label
        # для нижней рамки.
        self.label4 = tkinter.Label(self.bottom_frame,
                                    text='Мигнуть')
        self.label5 = tkinter.Label(self.bottom_frame,
                                    text='Моргнуть')
        self.label6 = tkinter.Label(self.bottom_frame,
                                    text='Кивнуть')

        # Упаковать надписи, расположенные в нижней рамке.
        # Применить аргумент side='left', чтобы их
        # расположить горизонтально слева рамки.
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # Да, и мы также должны упаковать рамки!
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ## 13.5 Элементы интерфейса Button и информационные диалоговые окна

# ### Программа 13-7 (button_demo.py)

# In[4]:


# Эта программа демонстрирует элемент интерфейса Button.
# Когда пользователь нажимает кнопку Button, 
# на экран выводится информационное диалоговое окно.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Button widget.  
        # На кнопке должен появиться текст 'Нажми меня!'. 
        # Когда пользователь нажимает кнопку, 
        # должен быть исполнен метод do_something.
        self.my_button = tkinter.Button(self.main_window,
                                        text='Нажми меня!',
                                        command=self.do_something)

        # Упаковать элемент интерфейса Button.
        self.my_button.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Метод do_something является функцией обратного 
    # вызова для элемента интерфейса Button.

    def do_something(self):
        # Показать информационное диалоговое окно.
        tkinter.messagebox.showinfo('Реакция',
                                    'Благодарю, что нажали кнопку.')

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-8 (quit_button.py)

# In[5]:


# Эта программа содержит кнопку 'Выйти', которая
# при ее нажатии вызывает метод destroy класса Tk .

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Button widget.
        # На кнопке должен появиться текст 'Нажми меня!'.
        # Когда пользователь нажимает кнопку,
        # должен быть исполнен метод do_something.
        self.my_button = tkinter.Button(self.main_window,
                                        text='Нажми меня!',
                                command=self.do_something)

        # Создать кнопку 'Выйти'. При нажатии этой кнопки вызыва-ется
        # метод destroy корневого элемента интерфейса (переменная
        # main_window ссылается на корневой элемент, поэтому функцией
        # обратного вызова является self.main_window.destroy.)
        self.quit_button = tkinter.Button(self.main_window,
                                          text='Выйти',
                                command=self.main_window.destroy)


        # Упаковать элементы интерфейса Button.
        self.my_button.pack()
        self.quit_button.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Метод do_something является функцией обратного
    # вызова для элемента интерфейса Button.

    def do_something(self):
        # Показать информационное диалоговое окно.
        tkinter.messagebox.showinfo('Реакция',
                                     'Благодарю, что нажали кнопку.')

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ## 13.6 Получение входных данных при помощи элемента интерфейса Entry

# ### Программа 13-9 (kilo_converter.py)

# In[7]:


# Эта программа конвертирует расстояния в километрах
# в мили. Полученный результат выводится в
# информационном диалоговом окне.

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):

        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать две рамки, чтобы сгруппировать элементы интер-фейса.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать элементы интерфейса для верхней рамки.
        self.prompt_label = tkinter.Label(self.top_frame,
                             text='Введите расстояние в километрах:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Упаковать элементы верхней рамки.
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Создать элементы интерфейса Button для нижней рамки.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                    text='Преобразовать',
                                    command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                    text='Выйти',
                                    command=self.main_window.destroy)
        # Упаковать кнопки.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковать рамки.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Метод convert является функцией обратного вызова
    # для кнопки 'Преобразовать'.

    def convert(self):
        # Получить значение, введенное пользователем
        # в элемент интерфейса kilo_entry.
        kilo = float(self.kilo_entry.get())

        # Конвертировать километры в мили.
        miles = kilo * 0.6214

        # Показать результаты в информационном диалоговом окне.
        tkinter.messagebox.showinfo('Результаты',
                                    str(kilo) +
                                    ' километров эквивалентно ' +
                                    str(miles) + ' милям.')

# Создать экземпляр класса KiloConverterGUI.
kilo_conv = KiloConverterGUI()


# ## 13.7 Применение элементов Label в качестве полей вывода

# ### Программа 13-10 (kilo_converter2.py)

# In[8]:


# Эта программа конвертирует расстояния в километрах
# в мили. Полученный результат выводится 
# в элемент Label в главном окне.

import tkinter

class KiloConverterGUI:
    def __init__(self):

        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать три рамки, чтобы сгруппировать элементы интерфейса.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Создать элементы интерфейса для верхней рамки.
        self.prompt_label = tkinter.Label(self.top_frame,
                    text='Введите расстояние в километрах:')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Упаковать элементы верхней рамки.
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        # Создать элементы интерфейса для средней рамки.
        self.descr_label = tkinter.Label(self.mid_frame,
                   text='Преобразовано в мили:')

        # Объект StringVar нужен для того, чтобы его связать
        # с выходной надписью. Для сохранения последовательности 
        # пробелов используется метод set данного объекта.
        self.value = tkinter.StringVar()

        # Создать надпись Label и связать ее с объектом
        # StringVar. Любые значения, хранящиеся в 
        # объекте StringVar будут автоматически 
        # выводиться в надписи Label.
        self.miles_label = tkinter.Label(self.mid_frame,
                   textvariable=self.value)

        # Создать элементы интерфейса для средней рамки.
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')

        # Создать элементы интерфейса Button для нижней рамки.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Преобразовать',
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                   command=self.main_window.destroy)

        # Упаковать кнопки.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковать рамки.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    # Метод convert является функцией обратного вызова
    # для кнопки 'Преобразовать'.

    def convert(self):
        # Получить значение, введенное пользователем
        # в элемент интерфейса kilo_entry.
        kilo = float(self.kilo_entry.get())

        # Конвертировать километры в мили.
        miles = kilo * 0.6214

        # Конвертировать мили в символьную последовательность и 
        # сохранить ее в объекте StringVar. В результате элемент 
        # интерфейса miles_label будет автоматически обновлен.
        self.value.set(miles)

# Создать экземпляр класса KiloConverterGUI.
kilo_conv = KiloConverterGUI()


# ### Программа 13-11 (test_averages.py)

# In[1]:


# Эта программа применяет ГИП для получения трех
# оценок и вывода среднего балла.

import tkinter

class TestAvg:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать пять рамок.
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Создать и упаковать элементы интерфейса для оценки 1.
        self.test1_label = tkinter.Label(self.test1_frame,
                   text='Введите оценку 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame,
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Создать и упаковать элементы интерфейса для оценки 2.
        self.test2_label = tkinter.Label(self.test2_frame,
                   text='Введите оценку 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame,
                                         width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        # Создать и упаковать элементы интерфейса для оценки 3.
        self.test3_label = tkinter.Label(self.test3_frame,
                   text='Введите оценку 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame,
                                         width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # Создать и упаковать элементы интерфейса для среднего балла.
        self.result_label = tkinter.Label(self.avg_frame,
                                          text='Средний балл:')
        self.avg = tkinter.StringVar() # Для обновления avg_label
        self.avg_label = tkinter.Label(self.avg_frame,
                                       textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # Создать и упаковать элементы интерфейса Button.
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Усреднить',
                                          command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Выйти',
                               command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковать рамки.
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # Запустить главный цикл.
        tkinter.mainloop()

    # Метод calc_avg является функцией обратного вызова
    # для элемента интерфейса calc_button.

    def calc_avg(self):
        # Получить три экзаменационных оценки и
        # сохранить их в переменных.
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        # Вычислить средний балл.
        self.average = (self.test1 + self.test2 +
        self.test3) / 3.0

        # Обновить элемент интерфейса avg_label widget,
        # сохранив значение self.average в объекте 
        # StringVar, на который ссылается avg.
        self.avg.set(self.average)

# Создать экземпляр класса TestAvg.
test_avg = TestAvg()


# ## 13.8 Радиокнопки и флаговые кнопки

# ### Программа 13-12 (radiobutton_demo.py)

# In[10]:


# Эта программа демонстрирует группу элементов Radiobutton.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать две рамки. Одну для элементов Radiobutton
        # и еще одну для обычных элементов Button.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
 
        # Создать объект IntVar для использования с
        # элементами Radiobutton.
        self.radio_var = tkinter.IntVar()
 
        # Назначить объекту IntVar значение 1.
        self.radio_var.set(1)

        # Создать элементы Radiobutton в рамке top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Вариант 1',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Вариант 2',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Вариант 3',
                                       variable=self.radio_var,
                                       value=3)

        # Упаковать элементы Radiobutton.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Создать кнопку 'OK' и кнопку 'Выйти'.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                command=self.main_window.destroy)

        # Упаковать элементы Button.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковать рамки.
        self.top_frame.pack()
        self.bottom_frame.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

    # Метод show_choice является функцией обратного вызова
    # для кнопки OK.
    def show_choice(self):
        tkinter.messagebox.showinfo('Выбор', 'Выбран вариант ' +
                                    str(self.radio_var.get()))

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-13 (checkbutton_demo.py)

# In[12]:


# Эта программа демонстрирует группу элементов Checkbutton.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать две рамки. Одну для элементов Checkbutton
        # и еще одну для обычных элементов Button.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
 
        # Создать три объекта IntVar для использования с
        # элементами Checkbutton.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
 
        # Назвначить объектам IntVar значения 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
 
        # Создать элементы Checkbutton в рамке top_frame.
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Вариант 1',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Вариант 2',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Вариант 3',
                                       variable=self.cb_var3)

        # Упаковать элементы Checkbutton.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # Создать кнопку 'OK' и кнопку 'Выйти'.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                 command=self.main_window.destroy)

        # Упаковать элементы Button.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковать рамки.
        self.top_frame.pack()
        self.bottom_frame.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

    # Метод show_choice является функцией обратного вызова
    # для кнопки 'OK'.

    def show_choice(self):
        # Создать символьную последовательность с сообщением.
        self.message = 'Вы выбрали:\n'

        # Определить, какие элементы Checkbuttons были выбраны и
        # составить соответствующее сообщение.
        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'

        # Вывести сообщение в информационном диалоговом окне.
        tkinter.messagebox.showinfo('Выбор', self.message)

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ## 13.9 Рисование фигур при помощи элемента интерфейса Canvas

# ### Программа 13-14 (draw_line.py)

# In[13]:


# Эта программа демонстрирует элемент интерфейса Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
                                     width=200, height=200)
        # Нарисовать две прямых.
        self.canvas.create_line(0, 0, 199, 199)
        self.canvas.create_line(199, 0, 0, 199)

        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-15 (draw_multi_lines.py) 

# In[14]:


# Эта программа соединяет несколько точек отрезками прямой.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемента Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
                                     width=200, height=200)
        # Начертить отрезки прямой, соединяющей несколько точек.
        self.canvas.create_line(10, 10, 189, 10, 100, 189, 10, 10)

        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-16 (draw_square.py)

# In[16]:


# Эта программа чертит прямоугольник на элементе Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
                                     width=200, height=200)
        # Нарисовать прямоугольник.
        self.canvas.create_rectangle(20, 20, 180, 180)
        
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-17 (draw_ovals.py)

# In[18]:


# Эта программа чертит два овала на элементе Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
                                     width=200, height=200)
        # Нарисовать два овала.
        self.canvas.create_oval(20, 20, 70, 70)
        self.canvas.create_oval(100, 100, 180, 130)
 
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-18 (draw_arc.py)

# In[21]:


# Эта программа чертит дугу на элементе Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
                                     width=200, height=200)
        # Нарисовать дугу.
        self.canvas.create_arc(10, 10, 190, 190, start=45, extent=30)
 
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-19 (draw_piechart.py)

# In[22]:


# Эта программа чертит круговую диаграмму на элементе Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        self.__CANVAS_WIDTH = 320    # Ширина холста
        self.__CANVAS_HEIGHT = 240   # Высота холста
        self.__X1 = 60     # Левая верхняя координата X ограничивающего прямоугольника 
        self.__Y1 = 20     # Левая верхняя координата Y ограничивающего прямоугольника
        self.__X2 = 260    # Нижняя правая координата X ограничивающего прямоугольника
        self.__Y2 = 220    # Нижняя правая координата Y ограничивающего прямоугольника
        self.__PIE1_START = 0     # Исходный угол сектора 1
        self.__PIE1_WIDTH = 45    # Протяженность сектора 1
        self.__PIE2_START = 45    # Исходный угол сектора 2
        self.__PIE2_WIDTH = 90    # Протяженность сектора 2
        self.__PIE3_START = 135   # Исходный угол сектора 3
        self.__PIE3_WIDTH = 120   # Протяженность сектора 3
        self.__PIE4_START = 255   # Исходный угол сектора 4
        self.__PIE4_WIDTH = 105   # Протяженность сектора 4
 
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=self.__CANVAS_WIDTH,
                                     height=self.__CANVAS_HEIGHT)

        # Начертить сектор 1.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, 
                               self.__Y2, start=self.__PIE1_START,
                               extent=self.__PIE1_WIDTH,
                               fill='red')

        # Начертить сектор 2.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, 
                               self.__Y2, start=self.__PIE2_START,
                               extent=self.__PIE2_WIDTH,
                               fill='green')

        # Начертить сектор 3.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, 
                               self.__Y2, start=self.__PIE3_START,
                               extent=self.__PIE3_WIDTH,
                               fill='black')

        # Начертить сектор 4.
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, 
                               self.__Y2, start=self.__PIE4_START,
                               extent=self.__PIE4_WIDTH,
                               fill='yellow')
 
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-20 (draw_polygon.py)

# In[23]:


# Эта программа чертит многоугольник на элементе Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
                                     width=160, height=160)
        # Нарисовать многоугольник.
        self.canvas.create_polygon(60, 20, 100, 20, 140, 60, 140, 
                                   100, 100, 140, 60, 140, 20, 100, 
                                   20, 60)
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-21 (draw_text.py)

# In[24]:


# Эта программа наносит текст на элемент Canvas.
import tkinter

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент Canvas.
        self.canvas = tkinter.Canvas(self.main_window, 
                                     width=200, height=200)
        # Показать текст в центре окна.
        self.canvas.create_text(100, 100, text='Привет, мир!')
 
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()


# ### Программа 13-22 (font_demo.py)

# In[25]:


# Эта программа наносит текст на элемент Canvas.
import tkinter
import tkinter.font

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=200, 
                                     height=200)
        # Создать объект Font.
        myfont = tkinter.font.Font(family='Helvetica', size=18, 
                                   weight='bold')
        # Показать немного текста.
        self.canvas.create_text(100, 100, text='Привет, мир!', 
                                font=myfont)
        # Упаковать холст.
        self.canvas.pack()
 
        # Запустить главный цикл.
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()

