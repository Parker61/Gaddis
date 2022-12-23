#v 18
#v3
v=input("Will be vegeterian: ")
vn=input("Will be vegan: ")
g=input("Will be gluten: ")
ve=False
ven=False
gl=False
if v=='y':
    ve=True
if vn=='y':
    ven=True
if g=='y':
    gl=True
if not ve and not ven and not gl:
    print("Djo")
if not ven:
    print("Pizza")
if not gl and not ven:
    print("Ital")
print("Cafe")
print("Chef")

#v2
v=input("Will be vegeterian: ")
vn=input("Will be vegan: ")
g=input("Will be gluten: ")
ve=False
ven=False
gl=False

if not ve and not ven and not gl:
    print("djo")
if not ven and not gl:
    print("Ital")
if not ven:
    print("Pizza")
print("Cafe")
print("Chef")


#v1
v=input("Will be vegeterian: ")
vn=input("Will be vegan: ")
g=input("Will be gluten: ")

print('total: ')
#Chef
if v=='y' and vn=='y' and g=='y':
    C=True
elif v=='n' and vn=='y' and g=='y':
    C=True
elif v=='n' and vn=='n' and g=='y':
    C=True
elif v=='n' and vn=='n' and g=='n':
    C=True
elif v=='y' and vn=='n' and g=='y':
    C=True
elif v=='y' and vn=='n' and g=='n':
    C=True
else:
    C=False

if C:
    print("Chef")

#Cafe    
if v=='y' and vn=='y' and g=='y':
    Ca=True
elif v=='n' and vn=='y' and g=='y':
    Ca=True
elif v=='n' and vn=='n' and g=='y':
    Ca=True
elif v=='n' and vn=='n' and g=='n':
    Ca=True
elif v=='y' and vn=='n' and g=='y':
    Ca=True
elif v=='y' and vn=='n' and g=='n':
    Ca=True
else:
    Ca=False

if Ca:
    print("Cafe")


#Pizza   
if v=='y' and vn=='n' and g=='y':
    P=True
elif v=='n' and vn=='n' and g=='y':
     P=True
elif v=='y' and vn=='n' and g=='n':
     P=True
else:
    P=False

if P:
    print("Pizza")

    
   
    
#Dgo  
if v=='n' and vn=='n' and g=='n':
    D=True
else:
    D=False

if D:
    print("Djo")

 
#Italian   
if v=='y' and vn=='n' and g=='n':
    I=True
elif v=='n' and vn=='n' and g=='n':
     I=True
else:
    I=False

if I:
    print("Italian")


#v 17
print('reset comp')
print('Did you corrected the problem?:', end='')
x=input()


if x=='n':
    print('reset swith')
    x=input("Did you corrected the problem?: ")
    if x=='n':
            print('add LAN')
            x=input("Did you corrected the problem?: ")
    else:
        x=='y'
        print("yes")
    if x=='n':
            print('move modem')
            x=input("Did you corrected the problem?: ")
    else:
        x=='y'
        print("yes")
    if x=='n':
            print('buy new modem')
            
    else:
        x=='y'
        print("yes")  
else:
    x=='y'
    print("good bay")

#16
# Упражнение по программированию 3-16

# Дни в феврале

# Эта программа определяет количество дней в
# феврале для того или иного года.

print('Введите год: ', end='')
year = int(input())
if year % 100 == 0:
    if year % 400 == 0:
        leap_year = True
    else:
        leap_year = False
else:
    if year % 4 == 0:
        leap_year = True
    else:
         leap_year = False
if leap_year:
    print('Это високосный год. В феврале 29 дней.')
else:
    print('Это не високосный год. В феврале 28 дней.')


    
#15
#v2


s = int(input('time sec: '))

if s>=86400:
    d=s//86400 # d
    so1=s%86400 #left sec from d
    h=so1//3600 #h
    so2=so1%3600 #left sec from h
    m=so2//60#m
    so3=so2%60#left sec from m
    s=so3%60#left sec 
            
elif s>=3600:
    d=0
    h=s//3600 #h
    so1=s%3600 #left sec from h
    m=so1//60#m
    so2=so1%60#left sec from m
    s=so2%60#left sec
elif s>=60:
        d=0
        h=0
        m=s//60#m
        so1=s%60#left sec from m
        s=so1%60#left sec
elif s>=0:
        d=0
        h=0
        m=s//60#m
        so1=s%60#left sec from m
        s=so1%60#left sec

   
print(" days",d,"\n","hours",h,"\n","minutes",m,"\n","sec",s)


#v1 кривая
s = int(input('time sec: '))

if s>=86400:
    d=s//86400 # d
    so1=s%86400 #left sec from d
    if so1>=3600:
        h=so1//3600 #h
        so2=so1%3600 #left sec from h
        m=so2//60 #m
        so3=so2%60 #left sec from m
        s=so3 #sec
    else:
        h=0
        m=so1//60#m
        so2=so1%60#left sec from m
        s=so2#left sec
        if so2>=60:
             m=so2//60#m
             s=so2%60#left sec from m
        else:
             m=0
             s=so2#sec
 
else:#<86400
    d=0
    if s>=3600:
        h=s//3600#h
        so1=s%3600#left sec from h
        m=so1//60#m
        so2=so1%60#left sec from m
        s=so2#left sec
    elif s>=60:
        h=0
        m=s//60#m
        s=s%60#left sec from m
    elif s<60:
        h=0
        m=0
        s+=0#sec
    else:#<3600
        h=0
        m=s//60#m
        so1=s%60#left sec from m
        s=so1#left sec   
   
print(" days",d,"\n","hours",h,"\n","minutes",m,"\n","sec",s)





#14

# Упражнение по программированию 3-14

# Индекс массы тела

# Локальные переменные
weight = 0.0
height = 0.0
IMT = 0.0    # индекс массы тела - имт

# Получить от пользователя вес.
weight = float(input('Введите свой вес в килограммах: '))

# Получить от пользователя рост.
height = float(input('Введите свой рост в метрах: '))

# Вычислить массу тела.
IMT = weight / (height **2)

# Показать ИМТ.
print('Ваш индекс массы тела равняется', format(IMT, '.2f'))

# Определить и показать весовую категорию.
if IMT > 25:
    print('Вы весите выше нормы.')
elif IMT < 18.5:
    print('Вы весите ниже нормы.')
else:
    print('Ваш вес оптимален.')
#13
 # Упражнение по программированию 3-13

# Стоимость доставки

# Локальные переменные
weight = 0.0
shippingCost = 0.0

# Получить от пользователя вес пакета.
weight = float(input('Введите вес пакета: '))

# Вычислить стоимость доставки.
if weight > 10:
    shippingCost = 4.75
elif weight > 6:
    shippingCost = 4.00
elif weight > 2:
    shippingCost = 3.00
else:
    shippingCost = 1.50

# Показать стоимость доставки.
print ('Стоимость доставки: $', format(shippingCost, '.2f'))   


#12
# Упражнение по программированию 3-12

# Реализация программного обеспечения

# Именованная константа
RETAIL_PRICE = 99

# Локальные переменные
quantity = 0
fullPrice = 0.0
discountRate = 0.0
discountAmount = 0.0
totalAmount = 0.0

# Получить количество
quantity = int(input('Введите количество приобретенных пакетов: '))

# Вычислить скидочную ставку
if quantity > 99:
    discountRate = 0.40
elif quantity > 49:
    discountRate = 0.30
elif quantity > 19:
    discountRate = 0.20
elif quantity > 9:
    discountRate = 0.10
else:
    discountRate = 0

# Вычислить полную цену
fullPrice = quantity * RETAIL_PRICE

# Вычислить сумму скидки
discountAmount = fullPrice * discountRate

# Вычислить общую сумму
totalAmount = fullPrice - discountAmount

# Напечатать результаты
print ('Сумма скидки: $', format(discountAmount, '.2f'))
print ('Общая сумма: $', format(totalAmount, '.2f'))




#11
# Упражнение по программированию 3-11

# Очки книжного клуба

# Локальные переменные
number = 0
points = 0

# Получить количество книг, приобретенных пользователем.
number = int(input('Введите количество приобретенных книг: '))

# Определить количество заработанных очков.
if number >= 8:
    points = 60
elif number >= 6:
    points = 30
elif number >= 4:
    points = 15
elif number >= 2:
    points = 5
else: 
    points = 0

# Показать количество заработанных очков.
print('Вы приобрели', number, 'книг.')
print('В результате вы заработали', points, 'очков.')

#10
# Упражнение по программированию 3-10

# Игра в подсчитывание монет

# Глобальные переменные
COIN5_VALUE = 5
COIN10_VALUE = 10
COIN50_VALUE = 50
KOPECKS_IN_ROUBLE = 100

# Локальные переменные
coin5 = 0
coin10 = 0
coin50 = 0
totalValue = 0.0
totalRoubles = 0.0

# Получить от пользователей количество 
# монет достоинством 5, 10 и 50.
coin5 = int(input('Введите количество монет достоинством 5 коп.: '))
coin10 = int(input('Введите количество монет достоинством 10 коп.: '))
coin50 = int(input('Введите количество монет достоинством 50 коп.: '))

# Сумма монет достоинством 5, 10 и 50 копеек
# для получения общей суммы в копейках.
totalValue = (coin5 * COIN5_VALUE) + \
             (coin10 * COIN10_VALUE)+ \
             (coin50 * COIN50_VALUE)



# Определить, выиграл ли пользователь игру:
if totalValue > 100:
    # Сумма была больше одного рубля.
    print('Извините, введенная вами сумма больше одного рубля.')
elif totalValue < 100:
    # Сумма была меньше одного рубля.
    print('Извините, введенная вами сумма меньше одного рубля.')
else:
    # Сумма была равна ровно одному рублю.
    print('Поздравляем!')
    print('Сумма, которую вы ввели, равняется ровно одному рублю!')
    print('Вы выиграли!')


#9
pocketNum = int(input('Введите количество карманов от 0 до 36: '))

# Определить, является ли номер кармана допустимым.
if pocketNum < 0 or pocketNum > 36:
    outputStr = 'Ошибка: введено недопустимое значение'
    
# Определить цвет номера кормана.

    # Для карманов с 1 по 10, карманы с нечетными номерами - 
    # красные, и карманы с четными номерами - черные.    
elif pocketNum >= 1 and pocketNum <= 10:
    if pocketNum % 2:   
            outputStr = 'Черный'  # Четный
    else:
            outputStr = 'Красный' # Нечетный

    # Для карманов с  11 по 18, карманы с нечетными номерами -
    # черные, и карманы с четными номерами - красные.              
elif pocketNum >= 11 and pocketNum <= 18:
    if pocketNum % 2:
                            outputStr = 'Красный' # Четный
    else:
            outputStr = 'Черный'  # Нечетный

    # Для карманов с 19 по 28, карманы с нечетными номерами -
    # красные, и карманы с четными номерами - черные.              
elif pocketNum >= 19 and pocketNum <= 28:
    if pocketNum % 2:
            outputStr = 'Черный'  # Четный
    else:
            outputStr = 'Красный' # Нечетный
            
    # Для карманов с 29 по 36, карманы с нечетными номерами -
    # черные, и карманы с четными номерами - красные.              
elif pocketNum >= 29 and pocketNum <= 36:
    if pocketNum % 2:
            outputStr = 'Красный' # Четный
    else:
            outputStr = 'Черный'  # Нечетный

    # Карман 0 - зеленый.
else:
        outputStr = 'Зеленый'        # Зеро (ноль)

# Показать результат.
print(outputStr)



#8
#var8.2
Np=int(input(" person:"))
Nh=int(input(" hot-dog:"))
t=Np*Nh
Npac_sausage=(Np*Nh)//10
Npac_buns=(Np*Nh)//8

Nleft_sausage=(Np*Nh)%10
Nleft_buns=(Np*Nh)%8


if Np>0 and Nh>0: 
    if Nleft_sausage>0:
       Npac_sausage+=1
    else:
       Nleft_sausage=0             
    if Nleft_buns>0:
       Npac_buns+=1
    else:
         Nleft_buns=0
    print(" Nleft_buns",Nleft_buns, "Npac_buns",Npac_buns,
      "\n","Nleft_sausage", Nleft_sausage, "Npac_sausage",Npac_sausage)
else: 
    print("false")


    
#var8.1
Np=int(input(" person:"))
Nh=int(input(" hot-dog:"))

if Np<0 or Nh<0:
   print("false")
else:
    Nbalance_cake=(Np*Nh)%8
    Nbalance_sausage=(Np*Nh)%10
    Ninteger_cake=(Np*Nh)//8
    Ninteger_sausage=(Np*Nh)//10
 
if Nbalance_cake >0:
   Ninteger_cake +=1
   
elif Nbalance_sausage >0:
     Ninteger_sausage+=1
     
elif Nbalance_cake==0:
     Ninteger_cake=Ninteger_cake+0
     
elif Nbalance_sausage==0:
     Ninteger_sausage=Ninteger_sausage+0

print(" Nbalance_cake: ", Nbalance_cake,
"\n","Nbalance_sausage: ", Nbalance_sausage,
"\n","Ninteger_cake: ", Ninteger_cake,
"\n","Ninteger_sausage: ",Ninteger_sausage)




#7
C1=str(input("enter color: "))
C2=str(input("enter color: "))

if C1=='red' and C2=='blue' or C2=='red' and C1=='blue':
    print("fiolet")
elif C1=='red' and C2=='yelow'or C2=='red' and C1=='blue':
    print("green")
elif C1=='yelow' and C2=='blue'or C2=='red' and C1=='blue':
    print("orange")
elif C1!='red' or C2!='red'or C1!='blue' or C2!='blue'or C1!='yelow' or C2!='yelow':
    print("Error")
elif C1=='red' and C2=='red'or C1=='blue' or C2=='blue'or C1=='yelow' or C2=='yelow':
    print("Errorrrrrrr")
else:
    print("false")
