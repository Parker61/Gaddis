##############  8
import tkinter
# Именованные константы
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
HOUSE_X = 50
HOUSE_Y = 400
HOUSE_WIDTH = 500
HOUSE_HEIGHT = 200
ROOF_X = HOUSE_X - 25
ROOF_Y = HOUSE_Y - HOUSE_HEIGHT
ROOF_WIDTH = HOUSE_WIDTH + 50
ROOF_HEIGHT = 150
ROOF_APEX_X = ROOF_X + int(ROOF_WIDTH / 2)
ROOF_APEX_Y = ROOF_Y - ROOF_HEIGHT
DOOR_WIDTH = 80
DOOR_HEIGHT = 150
DOOR_X = (HOUSE_X + int(HOUSE_WIDTH / 2)) - (int(DOOR_WIDTH / 2))
DOOR_Y = HOUSE_Y
WINDOW_WIDTH = 100
WINDOW_HEIGHT = 100
WINDOW1_X = (HOUSE_X + int(HOUSE_WIDTH / 4)) - (int(WINDOW_WIDTH / 2))
WINDOW1_Y = HOUSE_Y - 50
WINDOW2_X = (HOUSE_X + (int(HOUSE_WIDTH / 4) * 3)) - (int(WINDOW_WIDTH / 2))
WINDOW2_Y = WINDOW1_Y
SUN_WIDTH = 75
SUN_X = CANVAS_WIDTH - SUN_WIDTH - 20
SUN_Y = SUN_WIDTH + 20
class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать элемент интерфейса Canvas.
        self.canvas = tkinter.Canvas(self.main_window, width=CANVAS_WIDTH,
                                     height=CANVAS_HEIGHT)

        # Нарисовать корпус дома.
        self.canvas.create_rectangle(HOUSE_X, HOUSE_Y, HOUSE_X + HOUSE_WIDTH,
                                     HOUSE_Y - HOUSE_HEIGHT)

        # Нарисовать крышу.
        self.canvas.create_polygon(ROOF_X, ROOF_Y, ROOF_APEX_X, ROOF_APEX_Y,
                                   ROOF_X + ROOF_WIDTH, ROOF_Y,
                                   ROOF_X, ROOF_Y)

        # Нарисовать дверь.
        self.canvas.create_rectangle(DOOR_X, DOOR_Y,
                                     DOOR_X + DOOR_WIDTH, DOOR_Y - DOOR_HEIGHT)

        # Нарисовать окно 1.
        self.canvas.create_rectangle(WINDOW1_X, WINDOW1_Y,
                                     WINDOW1_X + WINDOW_WIDTH,
                                     WINDOW1_Y - WINDOW_HEIGHT)

        # Нарисовать окно 2.
        self.canvas.create_rectangle(WINDOW2_X, WINDOW2_Y,
                                     WINDOW2_X + WINDOW_WIDTH,
                                     WINDOW2_Y - WINDOW_HEIGHT)

        # Нарисовать осолнце.
        self.canvas.create_oval(SUN_X, SUN_Y,
                                SUN_X + SUN_WIDTH, SUN_Y - SUN_WIDTH,
                                fill='yellow')
        # Упаковать холст.
        self.canvas.pack()
        # Запустить главный цикл.
        tkinter.mainloop()
# Создать экземпляр класса MyGUI.
my_gui = MyGUI()
#####  7
import tkinter
import tkinter.messagebox
from tkinter.ttk import *
class PhoneGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        # Создать рамки
        self.button_frame=Frame(self.main_window)
        self.entry_frame=Frame(self.main_window)
        self.calc_frame=Frame(self.main_window)
        # Создать переменную для использования с радиокнопками
        self.radio_var=tkinter.IntVar()
        # Присвоить переменной 1
        self.radio_var.set(1)
        # Создать элементы Radiobutton в верхней рамке
        self.rb1=tkinter.Radiobutton(self.button_frame,text='Дневное время (6:00 - 17:59)',
                                     variable=self.radio_var,value=10)
        self.rb2=tkinter.Radiobutton(self.button_frame,text='Вечернее время (18:00 - 23:59)',
                                     variable=self.radio_var,value=20)
        self.rb3=tkinter.Radiobutton(self.button_frame,text='Непиковый период (00:00 - 5:59)',
                                     variable=self.radio_var,value=30)
        # Упаковать элементы  Radiobutton
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        # Создать элементы интерфейса для средней рамки
        self.text_label=tkinter.Label(self.entry_frame,text='Введите количество минут:')
        self.entry_label=tkinter.Entry(self.entry_frame,width=10)
        self.text_label.pack(side='left')
        self.entry_label.pack()
        # Создать две кнопки в нижней рамке
        self.calc_chb=tkinter.Button(self.calc_frame,text='Показать стоимость',command=self.calc)
        self.quit_chb=tkinter.Button(self.calc_frame,text='exit',command=self.main_window.destroy)
        self.calc_chb.pack(side='left')
        self.quit_chb.pack(side='left')
        # Упаковать рамки
        self.button_frame.pack()
        self.entry_frame.pack()
        self.calc_frame.pack()

        tkinter.mainloop()# Войти в главный цикл tkinter

    # Определить функцию calculate
    def calc(self):
        # Получить введенное значение
        self.hours=float(self.entry_label.get())
        self.price=self.hours * self.radio_var.get()

        # вариант 2:
        #if self.radio_var.get()==10:
            #self.rate=1
        #if self.radio_var.get()==20:
            #self.rate=2
        #if self.radio_var.get()==30:
            #self.rate=3
        #self.price=self.hours * self.rate

        tkinter.messagebox.showinfo('coust','price phone=$'+
                                        str(self.price))
# Создать экземпляр
my_phone=PhoneGUI()

###################################  6
import tkinter
import tkinter.messagebox
from tkinter.ttk import *
class CarGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        # Создать рамки
        self.button_frame=Frame(self.main_window)
        self.calc_frame=Frame(self.main_window)
        # Создать переменные для использования с элементами Checkbuttons
        self.oil=tkinter.IntVar ()
        self.work=tkinter.IntVar()
        self.tire=tkinter.IntVar()
        # Присвоить переменным значение 0
        self.oil.set(0)
        self.work.set(0)
        self.tire.set(0)
        # Создать флаговые кнопки Checkbutton в верхней рамке
        self.oil_chb=tkinter.Checkbutton(self.button_frame,text='oil-',variable=self.oil)
        self.work_chb = tkinter.Checkbutton(self.button_frame, text='work-', variable=self.work)
        self.tire_chb = tkinter.Checkbutton(self.button_frame, text='tire-', variable=self.tire)
        # Упаковать элементы Checkbutton
        self.oil_chb.pack()
        self.work_chb.pack()
        self.tire_chb.pack()
        # Создать две кнопки в нижней рамке
        self.calc_chb=tkinter.Button(self.calc_frame,text='calc',command=self.calc)
        self.quit_chb=tkinter.Button(self.calc_frame,text='exit',command=self.main_window.destroy)
        self.calc_chb.pack(side='left')
        self.quit_chb.pack(side='left')
        # Упаковать рамки
        self.button_frame.pack()
        self.calc_frame.pack()
        tkinter.mainloop()# Войти в главный цикл tkinter

    # Определить функцию show_info
    def calc(self):
        self.total=0
        if self.oil.get()==1:
            self.total+= 100  #self.total+int(100)
        if self.work.get()==1:
            self.total+= 200 #self.total+int(200)
        if self.tire.get()==1:
            self.total+= 300 #self.total+int(300)
        # Показать информационное окно
        tkinter.messagebox.showinfo('coust', 'Ваши затраты = $' + \
                                    format(self.total,'.2f'))
my_car=CarGUI()
###########  5
import tkinter
from tkinter.ttk import *
class TaxGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.Fact_frame = Frame(self.main_window) # Создать рамки
        self.RatingPrice_frame = Frame(self.main_window)
        self.Tax_frame = Frame(self.main_window)
        self.Button_frame = Frame(self.main_window)

        self.fact_cost=Label(self.Fact_frame,text='fact coust $:  ') # Создать элементы интерфейса для рамки
        self.fact_cost_entry=Entry(self.Fact_frame,width=20) #длина символов 10
        self.fact_cost.pack(side='left')
        self.fact_cost_entry.pack(side='left')

        self.price_label = Label(self.RatingPrice_frame, text='ratio price:')
        self.price_coust=tkinter.StringVar()
        self.price_in=Label(self.RatingPrice_frame,textvariable=self.price_coust)
        self.price_label.pack(side='left') # Упаковать элементы рамки value_frame
        self.price_in.pack(side='left')

        # Создать пустое поле для оценочной стоимости
        self.tax_coust=tkinter.StringVar()
        self.tax_in=Label(self.Tax_frame,textvariable=self.tax_coust)
        # Создать элементы интерфейса для рамки
        self.tax_label = Label(self.Tax_frame, text='tax price:')
        self.tax_label.pack(side='left')
        self.tax_in.pack(side='left')

        self.convert_button=Button(self.Button_frame,text='ratio price',
                                   command=self.calc)
        self.quit_button=Button(self.Button_frame,text='exit',command=self.main_window.destroy)
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.Fact_frame.pack()
        self.RatingPrice_frame.pack()
        self.Tax_frame.pack()
        self.Button_frame.pack()
        tkinter.mainloop()  # Войти в главный цикл tkinter

    def calc(self):
        self.price=float(self.fact_cost_entry.get())*0.6 # Вычислить оценочную стоимость
        self.price_coust.set('$'+str(self.price)) # Обновить поле с оценочной стоимостью
        self.tax=format(float(self.price)/100*0.75,'.3f') # Вычислить налог
        self.tax_coust.set('$'+self.tax)

tax = TaxGUI() # Создать экземпляр

############  4
import tkinter
from tkinter.ttk import *
class CelsiuGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.C_frame = Frame(self.main_window)
        self.F_frame = Frame(self.main_window)
        self.Button_frame = Frame(self.main_window)

        self.Celsiu_label=Label(self.C_frame,text='temperatura in oC: ')
        self.Celsiu_entry=Entry(self.C_frame,width=35)
        self.Celsiu_label.pack(side='left')
        self.Celsiu_entry.pack(side='left')

        self.farengate=tkinter.StringVar()
        self.F_label=Label(self.F_frame,text='temperatura in F: ')
        self.F_in=Label(self.F_frame,textvariable=self.farengate)
        self.F_label.pack(side='left')
        self.F_in.pack(side='left')

        self.convert_button=Button(self.Button_frame,text='convert Celsiu in Farengate',
                                   command=self.convert)
        self.quit_button=Button(self.Button_frame,text='exit',command=self.main_window.destroy)
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.C_frame.pack()
        self.F_frame.pack()
        self.Button_frame.pack()
        tkinter.mainloop()

    def convert(self):
        self.cels=float(self.Celsiu_entry.get())
        self.fareng=format(float(9*self.cels/5+32) ,'.2f')
        self.farengate.set(self.fareng)

fareng=CelsiuGUI()

######  3
import tkinter
from tkinter.ttk import *
class CalculationGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()  # Создать главное окно
        # Создать четыре рамки
        self.G_frame = Frame(self.main_window)
        self.M_frame = Frame(self.main_window)
        self.MPG_frame = Frame(self.main_window)
        self.Button_frame = Frame(self.main_window)

        self.G_label = Label(self.G_frame, text='gallons: ')  # Создать элементы интерфейса для рамки gallons_frame
        self.G_entry = Entry(self.G_frame, width=10)
        self.G_label.pack(side='left')  # Упаковать элементы рамки
        self.G_entry.pack(side='left')

        self.M_label = Label(self.M_frame, text='miles: ')
        self.M_entry = Entry(self.M_frame, width=10)
        self.M_label.pack(side='left')
        self.M_entry.pack(side='right')

        self.MPG_label = Label(self.MPG_frame, text='MPG result: ')  # Создать элементы интерфейса для поля MPG_label
        self.mpg = tkinter.StringVar()  # Создать пустое поле
        self.MPG_in = Label(self.MPG_frame, textvariable=self.mpg)  # привязка к mpg
        # Упаковать элементы интерфейса для рамки
        self.MPG_label.pack(side='left')
        self.MPG_in.pack(side='left')

        # Создать две кнопки в нижней рамке
        self.calc_button = Button(self.Button_frame, text='вычислить', command=self.calculate_mpg)
        self.quit_button = Button(self.Button_frame, text='exit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        # Упаковать рамки
        self.G_frame.pack()
        self.M_frame.pack()
        self.MPG_frame.pack()
        self.Button_frame.pack()
        tkinter.mainloop()

    def calculate_mpg(self):
        self.gallons = float(self.G_entry.get())
        self.miles = float(self.M_entry.get())
        self.calc_MPG = format(float(self.miles) / self.gallons, '.2f')
        self.mpg.set(self.calc_MPG)  # Обновить поле mpg


mpg = CalculationGUI()  # Создать экземпляр MilesGUI

#####  2
import tkinter
from tkinter.ttk import *
class LatinTranslatorGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)

        self.text=tkinter.StringVar()
        self.in_text=Label(self.top_frame,textvariable=self.text)

        self.sinister_button = tkinter.Button(self.bottom_frame,text='sinister',command=self.translate_1)
        self.dexter_button = tkinter.Button(self.bottom_frame, text='dexter', command=self.translate_2)
        self.medium_button = tkinter.Button(self.bottom_frame, text='medium', command=self.translate_3)

        self.in_text.pack()
        self.sinister_button.pack(side='left')
        self.dexter_button.pack(side='left')
        self.medium_button.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    # Определить функцию  для каждой кнопки соответсвенно
    def translate_1 (self):
        self.text.set('левый')
    def translate_2 (self):
        self.text.set('правый')
    def translate_3 (self):
        self.text.set('центральный')

latin_translator = LatinTranslatorGUI()

######### 1
import tkinter
from tkinter.ttk import * # без неё Label не работает
class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk() # Создать главное окно
        #создать 2 рамки
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #создать пустое поле и связать с функцией inf и при вызове этой функции это поле заполнялось текстом из функции
        self.text=tkinter.StringVar() #связывание text с StringVar
        self.in_text=Label(self.top_frame,
                           textvariable=self.text) #прописываем в Label ссылку на text

        #создать 2 кнопки в нижней рамке
        self.my_button=tkinter.Button(self.bottom_frame,text='info  ',command=self.inf) #кнопка ссылки на функцию inf
        self.quit_button=tkinter.Button(self.bottom_frame,text='exit  ',command=self.main_window.destroy) #кнопка выхода

        #упаковать
        self.in_text.pack()
        self.my_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        # Войти в главный цикл tkinter
        tkinter.mainloop()

    def inf (self):
        #передать аргумент в StringVar  а он связан text который приписывается в in_text=Label.... через метод set
        self.text.set('adress,name\n'\
                      'and other')
my_gui=MyGUI() #создать экземпляр класса