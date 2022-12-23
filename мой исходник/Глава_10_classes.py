
#############  9 v2
class Question:
    def __init__(self,q,a1,a2,wa):
        self.__q=q
        self.__a1=a1
        self.__a2=a2
        self.__wa=wa

    def set_q(self,q):
        self.__q=q
    def set_a1(self,a1):
        self.__a1=a1
    def set_a2(self,a2):
        self.__a2=a2
    def set_wa(self,wa):
        self.__wa=wa

    def get_q(self):
        return self.__q
    def get_a1(self):
        return self.__a1
    def get_a2(self):
        return self.__a2
    def get_wa(self):
        return self.__wa

    def __str__(self):
        result=self.get_q()+'\n'+self.get_a1()+ '\n' \
               +self.get_a2()
        return result

    def iscorrect(self,user):
        return user==self.get_wa() #возврат True в случае если они равны



#############  9 v1
class Question:
    def __init__(self):
        self.__li1=[]
        self.__li2=[]


    def set_answer_1(self,i):
        print(i[0]) #индекс 0-вопрос, 1,2-вырианты ответов,3-индекс ответа
        print(i[1], i[2])
        us = input('your answer: ')
        if us!=i[3]:
            print('no correct answer')
        else:
           print('it is wright')
           self.__li1.append(1) #если верно запись в список

    def set_answer_2(self,us,i):
        if us!=i[3]:
            print('no correct answer')
        else:
           print('it is wright')
           self.__li2.append(1)

    def get_compare(self):
        print(len(self.__li1))
        print(len(self.__li2))
        if len(self.__li1)>len(self.__li2):
            print('us1 - win')
        elif len(self.__li1)==len(self.__li2):
            print('us1=us2')
        else:
            print('us2 - win')

#############  8 v2
#import retailItem
class CashRegister:
    def __init__(self,i,j):
        self.__list = [] #лист для подсчёта сумму цен товаров
        self.__d_wear = {i.get_description(): 0, j.get_description(): 0} #создаём словарь ключи-начальное количество товара из класса RetailItem все позиции по нулям

    def clear(self):
        self.__items=[]
        #self.__d_wear = {'jacket': 0, 'jeance': 0} # необязательно прописывать очистку словаря он всё равно чистится

    def wear(self,item):
        self.__list.append(item.get_price()) #добавить стоимость в список
        print('в корзину добавлено сейчас: 1', item.get_description(),'за',item.get_price(),'$') #значения из из класса RetailItem
        print('in basket now: ',end=' ') #считаем сколько в корзине количество каждой единицы
        n=1
        self.__d_wear[item.get_description()]+=n # добавить по 1 для соотвкетсвкующего значения
        for k in self.__d_wear:
            if self.__d_wear[k] > 0: #вывод товара только который добавили в корзину
                print(k, '-', self.__d_wear[k], end='; ')
        print()

    def get_numtotal(self):
        total=0
        for i in self.__list:  #передаём атрибут из метода wear где в list список добавляли цены
            total+=i  #работа метода get_price() из модуля RetailItem выдаёт стоимость подсчёт суммы цен
        return total  #можно выдать через return

    def show(self):
        print('Товары в кассовом аппарате:')
        #wear=set()
        #for i in self.__items:
            #wear.add(i.get_description()) #добавить название товара во множество чтбы не было повторения
        #for w in wear:
            #print(w,end='')
            #print()
        for k in self.__d_wear: # перебор ключей словаря
            if self.__d_wear[k] > 0: #вывод значения ключа только который >0 , т.е. добавили в корзину
                print(k,'-', self.__d_wear[k])

#############  8 v1
#import retailItem
class CashRegister:
    def __init__(self):
        self.__items = []

    def clear(self):
        self.__items=[]

    def purchase_item(self,wear):
        self.__items.append(wear)
        print('в корзину добавлено сейчас: 1',wear.get_description())
        print('в корзене лежит:')

    def get_numtotal(self):
        total=0
        for i in self.__items:
            total+=i.get_price()  #работа метода get_price() из модуля RetailItem выдаёт стоимость
        return total

    def show(self):
        print('Товары в кассовом аппарате:')
        wear=set()
        for i in self.__items:
            wear.add(i.get_description()) #добавить название товара во множество чтбы не было повторения
        for w in wear:
            print(w,end='')
            print()

class RetailItem:
    def __init__(self,description ,number,price):
        self.__description =description
        self.__number=number
        self.__price = price

    def set_description (self,n):
        self.__description =n

    def set_number(self,i):
        self.__number=i

    def set_price(self, i):
        self.__price = i

    def get_description (self):
        return self.__description
    def get_number(self):
        return self.__number
    def get_price(self):
        return self.__price

    def __str__(self):
        result='description : '+str(self.get_description ())+\
            '| '+'stock balance: '+str(self.get_number())+\
            '| price: '+str(self.get_price())+\
            '\n'
        return result



############### 7
class Employee:
    def __init__(self,name,id,division):
        self.__name=name
        self.__id=id
        self.__division = division

    def set_name(self,n):
        self.__name=n
    def set_id(self,i):
        self.__id=i
    def set_division(self, i):
        self.__division = i

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_division(self):
        return self.__division

    def __str__(self):
        result='id: '+self.get_id()+\
               '\nname: '+self.get_name()+\
            '\ndivision: '+self.get_division()
        return result

#########  6
class Patient:
    def __init__(self,name,city,num):
        self.__name=name
        self.__city=city
        self.__num = num

    def set_name(self,n):
        self.__name=n
    def set_city(self,i):
        self.__city=i
    def set_num(self, i):
        self.__num = i

    def get_name(self):
        return self.__name
    def get_city(self):
        return self.__city
    def get_num(self):
        return self.__num

    def __str__(self):
        result='name: '+self.get_name()+\
            '\ncity: '+self.get_city()+\
            '\nnum: '+format(self.get_num(),'.1f')
        return result

class Procudure:
    def __init__(self,name,data,doctor,cost):
        self.__name = name
        self.__data = data
        self.__doctor = doctor
        self.__cost = cost

    def set_name(self,n):
        self.name=n
    def set_data(self,n):
        self.data=n
    def set_doctor(self,n):
        self.doctor=n
    def set_cost(self,n):
        self.cost=n

    def get_name(self):
        return self.__name
    def get_data(self):
        return self.__data
    def get_doctor(self):
        return self.__doctor
    def get_cost(self):
        return self.__cost


    def __str__(self):
        result='procedura: '+self.get_name()+\
            '\ndata'+self.__data+\
            '\ndoctor'+self.get_doctor()+\
            '\ncost: '+format(self.__cost,'.1f')
        return result

###########  5
class RetailItem:
    def __init__(self,name,id,sub):
        self.__name=name
        self.__id=id
        self.__sub = sub

    def set_name(self,n):
        self.__name=n
    def set_id(self,i):
        self.__id=i
    def set_sub(self, i):
        self.__sub = i

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_sub(self):
        return self.__sub

    def __str__(self):
        result='name: '+self.get_name()+\
            '\nid: '+str(self.get_id())+\
            '\nsub: '+str(self.get_sub())
        return result


##########  4
class Employee:
    def __init__(self,name,id,sub):
        self.__name=name
        self.__id=id
        self.__sub = sub

    def set_name(self,n):
        self.__name=n
    def set_id(self,i):
        self.__id=i
    def set_sub(self, i):
        self.__sub = i

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_sub(self):
        return self.__sub

    def __str__(self):
        result='name: '+self.get_name()+\
            '\nid: '+self.get_id()+\
            '\nsub: '+self.get_sub()
        return result

#########  3  v1
class Information:
    def __init__(self, name, adress):
        self.__name = name
        self.__adress = adress
        # self.__age=age
        # self.__number=number

    def set_name(self, n):
        self.__name = n

    def set_adress(self, a):
        self.__adress = a

    def set_age(self, a):
        self.__age = a

    def set_number(self, a):
        self.__number = a

    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    def get_age(self):
        return self.__age

    def get_number(self):
        return self.__number

##########   3v2
class Information:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number
################ 2
class Car:
    def __init__(self,m):
        self.__model=m
        #self.__make=make
        self.__speed=5 #начальное значение в атрибуте


    def accelerate(self,add_num):
        #print(add_num)
        self.__speed += add_num # при каждом вызове прибавляет к атрибуту =5

    def break_(self, num):
        self.__speed -= num

    def set_model(self, model): # нет надобности в этой функции
        self.__model=model
    def set_make(self, make):
        self.__make=make


    def get_model(self):
        return self.__model
    def get_make(self):
        return self.__make
    def get_speed(self):
        return self.__speed

############# 1
class Pet:
    def __init__(self,name,type,age):
        self.__name=name #нижнее подчеркивание для сокрытия атрибутов
        self.__type=type
        self.__age=age

    def set_name(self,name):
        self.__name=name
    def set_type(self,type):
        self.__type=type
    def set_age(self,age):
        self.__age=age

    def get_name(self):
        return self.__name
    def get_type(self):
        return self.__type
    def get_age(self):
        return self.__age



# v3 не понятно как работает
# x=8
# for r in range(x):
# for x in range(x):
# print('*', end='')
# print()
    




