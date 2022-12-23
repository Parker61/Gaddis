
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-


# # Глава 11. Наследование

# ## 11.1	Введение в наследование

# ### Программа 11-1 (vehicles.py)

# In[6]:


# Класс Automobile содержит общие данные
# об автомобиле в на складе.

class Automobile:
    # Метод __init__method принимает аргументы для
    # фирмы-изготовителя, модели, пробега и цены. 
    # Он инициализирует атрибуты данных этими значениями.
 
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # Следующие ниже методы являются методами-модификаторами 
    # атрибутов данных этого класса.

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    # Следующие ниже методы являются методами-получателями
    # атрибутов данных этого класса.

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price
    
# Класс Car представляет легковой автомобиль.
# Он является подклассом класса Automobile.

class Car(Automobile):
    # Метод __init__method принимает аргументы для
    # фирмы-изготовителя, модели, пробега, цены и количества дверей.

    def __init__(self, make, model, mileage, price, doors):
        # Вызвать метод __init__ надкласса и передать
        # требуемые аргументы. Обратите внимание, что мы также
        # передаем self в качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)

        # Инициализировать атрибут __doors.
        self.__doors = doors

    # Метод set_doors является методом-модификатором 
    # атрибута __doors.

    def set_doors(self, doors):
        self.__doors = doors

    # Метод get_doors является методом-получателем
    # атрибута __doors.

    def get_doors(self):
        return self.__doors

# Класс Truck представляет пикап. 
# Он является подклассом класса Automobile.

class Truck(Automobile):
    # Метод __init__ принимает аргументы для
    # изготовителя, модели, пробега, цены и типа привода пикапа.

    def __init__(self, make, model, mileage, price, drive_type):
        # Вызвать метод __init__ надкласса и передать
        # требуемые аргументы. Обратите внимание, что мы также
        # передаем self в качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)

        # Инициализировать атрибут __drive_type.
        self.__drive_type = drive_type

    # Метод set_drive_type является методом-модификатором
    # атрибута __drive_type.

    def set_drive_type(self, drive_type):
        self.__drive = drive_type

    # Метод get_drive_type является методом-получателем
    # атрибута __drive_type.

    def get_drive_type(self):
        return self.__drive_type

# Класс SUV представляет джип. 
# Он является подклассом класса Automobile.

class SUV(Automobile):
    # Метод __init__ принимает аргументы для
    # изготовителя, модели, пробега, цены и
    # пассажирской вместимости.

    def __init__(self, make, model, mileage, price, pass_cap):
        # Вызвать метод __init__ надкласса и передать
        # требуемые аргументы. Обратите внимание, что мы также
        # передаем self в качестве аргумента.
        Automobile.__init__(self, make, model, mileage, price)

        # Инициализировать атрибут __pass_cap.
        self.__pass_cap = pass_cap

    # Метод set_pass_cap является методом-модификатором
    # атрибутом __pass_cap.

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    # Метод get_pass_cap является методом-получателем
    # атрибутом __pass_cap.

    def get_pass_cap(self):
        return self.__pass_cap


# ### Программа 11-3 (car_demo.py)

# In[3]:


# Эта программа демонстрирует класс Car.

import vehicles

def main():
    # Создать объект на основе класса Car. 
    # Легковое авто: 2007 Audi с 12,500 миль пробега, 
    # ценой $21,500.00 и с 4 дверьми.
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)

    # Показать данные легкового авто.
    print('Изготовитель:', used_car.get_make())
    print('Модель:', used_car.get_model())
    print('Пробег:', used_car.get_mileage())
    print('Цена:', used_car.get_price())
    print('Количество дверей:', used_car.get_doors())

# Вызвать главную функцию.
main()


# ### Программа 11-6 (car_truck_suv_demo.py)

# In[1]:


# Эта программа создает объект Car, объект Truck
# и объект SUV.

import vehicles

def main():
    # Создать объект Car для подержанного авто 2001 BMW
    # с 70,000 милями пробега, ценой $15,000, с
    # 4 дверьми.
    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)

    # Создать объект Truck для подержанного пикапа 2002
    # Toyota с 40,000 милями пробега, ценой
    # $12,000, с 4-колесным приводом.
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    # Создать объект SUV для подержанного 2000
    # Volvo с 30,000 милями пробега, ценой
    # $18,500, с вместимостью 5 человек.
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('ПОДЕРЖАННЫЕ АВТО НА СКЛАДЕ')
    print('==========================')

    # Показать данные легкового авто.
    print('Данный легковой автомобиль имеется на складе:')
    print('Изготовитель:', car.get_make())
    print('Модель:', car.get_model())
    print('Пробег:', car.get_mileage())
    print('Цена:', car.get_price())
    print('Количество дверей:', car.get_doors())
    print()

    # Показать данные пикапа.
    print('Данный пикап имеется на складе.')
    print('Изготовитель:', truck.get_make())
    print('Модель:', truck.get_model())
    print('Пробег:', truck.get_mileage())
    print('Цена:', truck.get_price())
    print('Тип привода:', truck.get_drive_type())
    print()

    # Показать данные джипа.
    print('Данный джип имеется на складе.')
    print('Изготовитель:', suv.get_make())
    print('Модель:', suv.get_model())
    print('Пробег:', suv.get_mileage())
    print('Цена:', suv.get_price())
    print('Пассажирская вместимость:', suv.get_pass_cap())

# Вызвать главную функцию.
main()


# ### Программа 11-7 (accounts.py)

# In[2]:


# Класс SavingsAccount представляет
# сберегательный счет.

class SavingsAccount:

    # Метод __init__ принимает аргументы для 
    # номера счета, процентной ставки и остатка.

    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    # Следующие ниже методы являются методами-модификаторами
    # атрибутов данных.

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal

    # Следующие ниже методы являются методами-получателями
    # атрибутов данных.

    def get_account_num(self):
        return self.__account_num

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance

# Класс CD представляет счет 
# депозитного сертификата (CD). 
# Это подкласс класса SavingsAccount.

class CD(SavingsAccount):

    # Метод __init__ принимает аргументы для
    # номера счета, процентной ставки, остатка и
    # даты погашения.

    def __init__(self, account_num, int_rate, bal, mat_date):
        # Вызвать метод __init__ надкласса.
        SavingsAccount.__init__(self, account_num, int_rate, bal)

        # Инициализировать атрибут __maturity_date.
        self.__maturity_date = mat_date

    # Метод set_maturity_date является методом-модификатором
    # атрибута __maturity_date.

    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    # Метод get_maturity_date является методом-получателем
    # атрибута __maturity_date.

    def get_maturity_date(self):
        return self.__maturity_date


# ### Программа 11-8 (account_demo.py)

# In[2]:


# Эта программа создает экземпляр класса SavingsAccount
# и экземпляр класса CD.

import accounts

def main():
    # Получить номер счета, процентную ставку,
    # и остаток сберегательного счета.
    print('Введите данные о сберегательном счете.')
    acct_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))

    # Создать объект SavingsAccount.
    savings = accounts.SavingsAccount(acct_num, int_rate,
                                      balance)

    # Получить номер счета, процентную ставку,
    # остаток счета и дату погашения счета CD.
    print('Введите данные о счете CD.')
    acct_num = input('Номер счета: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))
    maturity = input('Дата погашения: ')

    # Создать объект CD.
    cd = accounts.CD(acct_num, int_rate, balance, maturity)

    # Показать введенные данные.
    print('Вот введенные Вами данные:')
    print()
    print('Сберегательный счет')
    print('-------------------')
    print('Номер счета:', savings.get_account_num())
    print('Процентная ставка:', savings.get_interest_rate())
    print('Остаток: $',
          format(savings.get_balance(), ',.2f'),
          sep='')
    print()
    print('Счет депозитного сертификата (CD)')
    print('---------------------------------')
    print('Номер счета:', cd.get_account_num())
    print('Процентная ставка:', cd.get_interest_rate())
    print('Остаток: $',
          format(cd.get_balance(), ',.2f'),
          sep='')
    print('Дата погашения:', cd.get_maturity_date())

# Вызвать главную функцию.
main()


# ## 11.2 Полиморфизм

# ### Программа 11-9 (animals.py)

# In[1]:


# Класс Mammal представляет род млекопитающих животных.

class Mammal:

    # Метод __init__ принимает аргумент для
    # вида млекопитающего животного.

    def __init__(self, species):
        self.__species = species

    # Метод show_species выводит сообщение
    # о виде млекопитающего животного.

    def show_species(self):
        print('Я -', self.__species)

    # Метод make_sound издает характерный
    # для всех млекопитающих звук.

    def make_sound(self):
        print('Грррррр')

# Класс Dog является подклассом класса Mammal.

class Dog(Mammal):

    # Метод __init__ вызывает метод __init__
    # надкласса, передавая 'собака' в качестве вида.

    def __init__(self):
        Mammal.__init__(self, 'собака')

    # Метод make_sound переопределяет  
    # метод make_sound надкласса.

    def make_sound(self):
        print('Гаф-гаф!')

# Класс Cat является подклассом класса Mammal.

class Cat(Mammal):

    # Метод __init__ вызывает метод __init__
    # надкласса, передавая 'кот' в качестве вида.

    def __init__(self):
        Mammal.__init__(self, 'кот')

    # Метод make_sound переопределяет 
    # метод make_sound надкласса.

    def make_sound(self):
        print('Мяю!')


# ### Программа 11-10 (polymorphism_demo.py)

# In[2]:


# Эта программа демонстрирует полиморфизм.

import animals

def main():
    # Создать объект Mammal, объект Dog и
    # и объект Cat.
    mammal = animals.Mammal('обычное животное')
    dog = animals.Dog()
    cat = animals.Cat()

    # Показать информацию о каждом животном.
    print('Вот несколько животных и')
    print('звуки, которые они издают.')
    print('--------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)

# Функция show_mammal_info принимает объект
# в качестве аргумента и вызывает свои методы 
# show_species и make_sound.

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

# Вызвать главную функцию.
main()


# ### Программа 11-11 (wrong_type.py)

# In[10]:


def main():
    # Передать симольное значение в функцию show_mammal_info
    show_mammal_info('Я – цепочка символов')

# Функция show_mammal_info принимает объект
# в качестве аргумента и вызывает свои методы 
# show_species и make_sound methods.

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

# Вызвать главную функцию.
main()


# ### Программа 11-12 (polymorphism_demo2.py)

# In[3]:


# Эта программа демонстрирует полиморфизм.

import animals

def main():
    # Создать объект Mammal, объект Dog и
    # объект Cat.
    mammal = animals.Mammal('обычное животное')
    dog = animals.Dog()
    cat = animals.Cat()

    # Показать информацию о каждом животном.
    print('Вот несколько животных и')
    print('звуки, которые они издают.')
    print('--------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info('Я – цепочка символов')

# Функция show_mammal_info принимает объект
# в качестве аргумента и вызывает свои методы 
# show_species и make_sound.

def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('Это не млекопитающее животное!')

# Вызвать главную функцию.
main()

