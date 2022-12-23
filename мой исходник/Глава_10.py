############   9 v2
import quest #импорт модуля
def main():
    player1=0
    player2=0
    questions = get_questions()
    #print('questions[0]',questions[0])
    #print('len(questions)',len(questions))
    for i in range(len(questions)): #количество вопросов в списке
        if i%2==0: #если четное то вопрос игроку 1
            p='1'
            print('quest for player',p,': ')
        else:
            print('quest for player 2: ') # иначе игроку 2

        print(questions[i])  #перебор поочерёдно вопросов из списка
        user=int(input('your answer: '))
        if questions[i].iscorrect(user): # сравнение ответа пользователя и ответа в списке
            if p=='1': #если ответ дан во время ответа игрока 1
                print('It is wright')
                player1+=1
            else:
                print('It is wright')
                player2+=1
        else:  # если неверно ответили
            print('it is wrong answer')
            #questions[i].get_wa() # передача в функцию списка и вывод из него ответа

    print('player1',player1)
    print('player2', player2)
    if player1==player2:
        print('Ничья.')
    elif player1>player2:
        print('Первый игрок побеждает в игре.')
    else:
        print('Второй игрок побеждает в игре.')

def get_questions():
    questions = [] # Создать перечень вопросов и добавить в список.
    question1 = quest.Question('Сколько дней в лунном ' + \
                                  'году?', '354', '365', \
                                   111)
    questions.append(question1) # добавляем переменные в список
    question2 = quest.Question('Какая самая большая планета?', \
                                   'Земля', \
                                  'Юпитер', 2)
    questions.append(question2)
    return questions

main()

###########  9 v1
import question

def main():
    q1 = ['how old are you1?', '1', '2', '1']  #индекс 0-вопрос, 1,2-вырианты ответов,3-индекс ответа
    q2 = ['how old are you2?', '1', '2', '2']
    li1=[q1,q2] #список вопросов для первого игрока
    qq1 = ['1:?', '1', '2', '1']
    qq2 = ['2:?', '1', '2', '2']
    li2=[qq1,qq2]
    #dct={'1':'1','2':['2','3']}
    #print(dct['2'][1])
    ques=question.Question()
    checkout='y'
    while checkout == 'y':
        for i in li1: #цикл для первого игрока
            ques.set_answer_1(i)
        for i in li2:
            print(i[0])
            print(i[1],i[2])
            us=input('your answer: ')
            ques.set_answer_2(us,i)
        checkout=input('try again?(y)')
    ques.get_compare()


main()

##############  8 v2
import cashReg  # вызов модуля cashReg при этом при присваивании переменной нужно прописывать имя модуля и класс
import retailItem  #

# from cashReg import CashReg,RetailItem  # вызов только классов CashRegister,RetailItem в модуле cashReg далее при вызове для переменной не нужно указывать имя модуля а срузу класс нужный
# from cashReg import *   #вызов всех классов из модуля cashReg при присваивании переменной имя модуля не пишется , а сразу имя класса
JACKET = 1  # Константы для вариантов покупаемых товаров
JEANCE = 2


def main():
    jacket = retailItem.RetailItem('jacket', 10, 5)  # Создать продаваемые товары.
    jeance = retailItem.RetailItem('jeance', 15, 3)
    sale_dct = {JACKET: jacket, JEANCE: jeance}  # Создать словарь продаваемых товаров.
    cash = cashReg.CashRegister(jacket, jeance)  # Создать кассовый аппарат и добавить в него все товары в наличии
    checkout = 'y'
    while checkout == 'y':
        ch = choice()  # выбор номера товара в фунции
        item = sale_dct[ch]  # соотв значение в словаре под ключём ch и присвоение этого значения переменной item

        if item.get_number() == '0':  # если кол-во товара равно 0
            print('no more wear')
        else:
            cash.wear(item) # обработка данных в корзине товар цена и количество каждого типа товара
            print('Sum in basket now: ', format(cash.get_numtotal(), '.2f'))  # сумма покупки в корзине

            ####  обновляем словарь с новой позицией   #####
            new_item = retailItem.RetailItem(item.get_description(), \
                                             item.get_number() - 1, \
                                             item.get_price())  # обновляем количество на 1 позицию меньше
            sale_dct[ch] = new_item
            checkout = input('are you ready ? (y or n): ')

    cash.show()  # итоговый вывод всех позиций
    print('Total buy sum: ', format(cash.get_numtotal(), '.2f'))
    cash.clear()  # очистка корзины


def choice():
    ch = int(input('choice wear: '))
    while ch > JEANCE or ch < JACKET:  # если выбор за диапозоном значений
        ch = int(input('correct choice PROD: '))
    return ch


main()

###################   8 v1
import cashReg # вызов модуля cashReg при этом при присваивании переменной нужно прописывать имя модуля и класс
import retailItem  #
#from cashReg import CashReg,RetailItem  # вызов только классов CashRegister,RetailItem в модуле cashReg далее при вызове для переменной не нужно указывать имя модуля а срузу класс нужный
#from cashReg import *   #вызов всех классов из модуля cashReg при присваивании переменной имя модуля не пишется , а сразу имя класса
JACKET = 1  # Константы для вариантов покупаемых товаров
JEANCE = 2
def main():
    jacket=retailItem.RetailItem('jacket', 10, 19.99)  # Создать продаваемые товары.
    jeance=retailItem.RetailItem('jeance', 15, 12.50)
    t_jacket=0
    t_jeance=0
    sale_dct={JACKET:jacket,JEANCE:jeance}   # Создать словарь продаваемых товаров.

    cash = cashReg.CashRegister()    # Создать кассовый аппарат
    checkout='y'
    while checkout=='y':
        ch=choice()         #выбор номера товара в фунции
        item=sale_dct[ch] #соотв значение в словаре под ключём ch и присвоение этого значения переменной item
        #print('item: ',item)
        #print('ch: ',ch)
        if item.get_number()=='0': #если кол-во товара равно 0
            print('no more wear')
        else:
            #печать........
            cash.purchase_item(item)  #добавить значение в список, который присваивается атрибуту __items в методе purchase_item
            if ch == 1:
                t_jacket += 1
            elif ch == 2:
                t_jeance += 1
            if t_jacket>0:
                print('jacket-', t_jacket)
            if t_jeance>0:
                print('jeance-', t_jeance)

            new_item=retailItem.RetailItem(item.get_description(), \
                                           item.get_number()-1,\
                                           item.get_price())  #обновляем количество на 1 позицию меньше
            sale_dct[ch]=new_item           #обновляем словарь с новой позицией

            print('Buy sum: ', format(cash.get_numtotal(), '.2f'))
            checkout=input('are you ready ? (y or n): ')
    print('Buy sum: ',format(cash.get_numtotal(),'.2f'))
    cash.show() #итоговый вывод всех позиций
    if t_jacket>0:
        print('jacket-',t_jacket) #вывод количества по каждой позиции
    if t_jeance>0:
        print('jeance-',t_jeance)
    cash.clear() #очистка корзины

def choice():
    ch = int(input('choice wear: '))
    while ch > JEANCE or ch < JACKET:  #если выбор за диапозоном значений
        ch = input('correct choice PROD: ')
    return ch
main()

####################  7
import pickle
import employee
LOOK = 1   # Глобальные константы для элементов меню
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILE=r'dct.dat'

def main():

    dct=dctt()
    ch=0   # Инициализировать переменную для выбора пользователя.
    while ch!=QUIT:
        ch=get_user()
        if ch==LOOK:
            look(dct)
        elif ch==ADD:
            add(dct)
        elif ch==CHANGE:
            change(dct)
        elif ch == DELETE:
            delete(dct)
        #print(dct)
        save(dct)  # Законсервировать результирующий словарь.

def look(dct):
    id = input('key id: ')
    #if id in dct: #можно через if
        #print(dct[id])
    #else:
        #print('key incorrect')
    print(dct.get(id,'key incorrect')) #выводит ключ если нет то запись поумолчанию

def change(dct):
    id = input('enter id(key) to change data: ')
    if id in dct:  # Изменить адрес, если имя существует.
        name = input('name: ')
        division = input('division: ')
        new_dct=employee.Employee(name, id, division)
        dct[id]=new_dct # выдачи значений из класса метода str name, id и division
        #list=dct[id] #можно значения ключа передать в список там в нём изменить и обратно передать в словарь в виде списка
        #list[0]=name
        #list[1] = division
        #dct[id]=list
        #print(dct) #но при этом значения тогда можно будет увидеть только через функцию look()

def add(dct):
    id = input('add id: ')
    if id not in dct:
        name = input('name: ')
        division = input('division: ')
        new_dct = employee.Employee(name, id, division)
        dct[id]=new_dct # выдачи значений из класса метода str name, id и division
        #dct[id]=[name,division] #можно в словарь записать значения
        #dct[id]=[0,0]  #можно просто пустой сделать
    else:
        print('there is id in dct')

def delete(dct):
    id = input('add id: ')
    if id in dct:
        del dct[id]
    else:
        print('this id is not')

def save(dct):
    inf=open('dct.dat','wb')
    pickle.dump(dct,inf)
    inf.close()


def dctt():
    try:
        inf=open(FILE,'rb')# Расконсервировать словарь.
        dct=pickle.load(inf)
        inf.close()
        print(dct)
    except IOError: #если нет для открытия то создать
        #i = int(input("сколько сотрудников: ")) # можно сразу добавить в словарь но тогда передачи в класс не будет и соответвенно вывод из метода __str__класса Employee будет без  значения id
        dct = {}
        #for i in range(1, int(i + 1)):
            #id = input("id: ")
            #name = input("name: ")
            #division = input("division: ")
            #dct[id] = [name, division]
            #li.append([name,id,sub]) # можно переать и в список
            #new_dct = employee.Employee(name,id,division)
        #print('new_dct: ',new_dct) #вывод из экземпляра класса Employee  из метода __str__
        #print('dct: ',dct)  # просто вывод в виде словаря
        #print('dct.items(): ',dct.items()) # вывод ключей и значений в виде кортежа
        #print(dct.get(id,'---')) #вывод только посленего знаечния ключа
    return dct

def get_user():
    ch = int(input('enter choice: '))
    while ch<LOOK or ch>QUIT:
        ch = int(input('enter correct : '))
    return ch
main()


##########  6
import patient
import procudure

def main():
    pac_1=patient.Patient('Jon','Moscow', 777)
    proc_1=procudure.Procudure('uzi','28/02/2022','Kov',250.00)
    proc_2 = procudure.Procudure('ykg', '01/02/2022', 'Kov', 500.00)
    proc_3 = procudure.Procudure('uzi', '28/02/2022', 'Kov', 200.00)
    total=proc_1.get_cost() + proc_2.get_cost() + proc_3.get_cost()
    print(pac_1)

    print(proc_1,proc_2)
    print('total:', total)

main()
###########  5
import retailItem
def main():
    prod_1=retailItem.RetailItem('jacket',12, 59.95)
    prod_2=retailItem.RetailItem('jeance',40, 34.95)
    prod_3=retailItem.RetailItem('shirt',20, 24.95)
    print(prod_1)
    print()
main()

############  4
import employee

def main():
    li=[]
    dct={}
    i=int(input("i: "))
    for i in range(1,int(i+1)):
        name=input("name: ")
        id = input("id: ")
        sub = input("sub: ")
        #dct[name]=[id,sub]
        #li.append([name,id,sub])
        cl=employee.Employee('name',id,sub) #можно name передать через перменную а можно сразу прописать как строковое значение главное соблюдать очередность при передачи аргументов
        print(cl) #печатает метод str из класса Employee
        #print(cl.get_name(),cl.get_id(),cl.get_sub()) # вывод значений без метода str в классе Employee
main()

#############  3 v1
import information
def main():
    my = ['my_1', 'my_2']
    ex = list()
    for i in range(len(my)):
        name = input('name: ')
        adress = input('adress: ')

        print(my[i], '-', end='')
        my[i] = information.Information(name, adress)
        print(' name: ', my[i].get_name(), '; adress: ', my[i].get_adress())
        ex.append([my[i].get_name(), my[i].get_adress()])  # запись в список каждого экземпляра

    for i in range(len(ex)):
        print('name: ', ex[i][0])
        print('adress: ', ex[i][1])

main()

####   3 v2
import information
def main():
    # Создать три экземпляра класса Information
    my_info =information.Information('Джон Доу','111 Моя улица', \
                               '22', '555-555-1281')
    mom_info = information.Information('Мать', '222 Мамина улица', \
                                52, '555-555-1234')
    sister_info = information.Information('Джейн Доу', '333 Ее улица', \
                                   20, '555-555-4444')

    print('Информация обо мне:')
    display_info(my_info)
    print()
    print("Информация о матери:")
    display_info(mom_info)
    print()
    print ("Информация о сестре:")
    display_info(sister_info)

def display_info(info):
    print('Имя: ', info.get_name())
    print('Адрес: ', info.get_address())
    print('Возраст: ', info.get_age())
    print('Телефон: ', info.get_phone_number())

main()
################   2
import car #импорт модуля
def main():
    num=1                        #задаём ускорение
    num_break=1                  #задаём торможение
    mo=input("model: ")          #задаём модель
    my=car.Car(mo)               #вызываем модуль класса car для создания экземпляра класса Car и присвоить переменной my
    print('speed_start: ', my.get_speed()) #вывод начального знач заданного в атрибуте
    for i in range(1,6):          #вызов функции my.accelerate(num) - с аргументом ускорения 1 нужное количество раз
        my.accelerate(num)
        print('speed_accel: ', my.get_speed())

    for i in range(1,6):  #торможение
        my.break_(num_break)
        print('speed_break: ', my.get_speed())

    print('model: ', my.get_model())

main()

########### 1
import pet
def main():

    name=input('name: ')
    type=input(('type: '))
    age=input('age: ')

    my_pet = pet.Pet(name,type,age)

    print('neme: ', my_pet.get_name())
    print('type: ', my_pet.get_type())
    print('age: ', my_pet.get_age())

main()


# v3 не понятно как работает
# x=8
# for r in range(x):
# for x in range(x):
# print('*', end='')
# print()
    




