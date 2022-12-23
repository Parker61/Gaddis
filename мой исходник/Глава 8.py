########## 14
def main():
    g=open(r'c:\Users\Павел\Desktop\GasPrices.txt','r')
    gas=g.readlines()
    average_year(gas)
    average_month(gas)
    max_price_year(gas)
    min_price_year(gas)
    low_to_hight_price(gas)
    hight_to_low_price(gas)

def hight_to_low_price(gas):
    gas_copy=[]
    hight_to_low_price=[]
    for i in gas:# Сделать копию списка gas
        gas_copy.append(i)
        
    while (len(gas_copy)>0):
        highest_ind=ind_max_pos(gas_copy)# индекс элемента с самой большой ценой.
        highest=gas_copy[highest_ind]      # Получить этот элемент.
        hight_to_low_price.append(highest)#добавить в список
        del gas_copy[highest_ind]# удалить предыдущее макс значение из списка
        
    for i in range(10):#первые 10 мин значений
        hi=hight_to_low_price[i].split(':')
        hi[1]=float(hi[1])
        print('№',i+1,':','low to hight price:',hi[0],' ',format(hi[1],'.2f'),sep='')    
    
def low_to_hight_price(gas):# отсортированные в порядке возрастания цены.
    gas_copy=[]
    low_to_hight_price=[]
    for i in gas:# Сделать копию списка gas
        gas_copy.append(i)
        
    while (len(gas_copy)>0):
        lowest_ind=ind_min_pos(gas_copy)# индекс элемента с самой низкой ценой.
        lowest=gas_copy[lowest_ind]      # Получить этот элемент.
        low_to_hight_price.append(lowest)#добавить в список
        del gas_copy[lowest_ind]# удалить предыдущее мин значение из списка
        
    for i in range(10):#первые 10 мин значений
        low=low_to_hight_price[i].split(':')
        low[1]=float(low[1])
        print('№',i+1,':','low to hight price:',low[0],' ',format(low[1],'.2f'),sep='')        

def ind_min_pos(gas_copy):#возвращает самое низкое значение из списка gas_copy
    lowest = get_price(gas_copy[0])
    position = 0
    for i in range(1, len(gas_copy)):
        if get_price(gas_copy[i]) < lowest:
            lowest = get_price(gas_copy[i])
            position = i
    return position

def ind_max_pos(gas_copy):       #возвращает самое большое значение из списка gas_copy
    highest = get_price(gas_copy[0])
    position = 0
    for i in range(1, len(gas_copy)):
        if get_price(gas_copy[i]) > highest:
            highest = get_price(gas_copy[i])
            position = i
    return position

def max_price_year(gas):
    current_y=get_year(gas[0])# тек знач месяца
    hi=get_price(gas[0])# тек макс знач в этой строке, т.е. в этом месяце    
    for i in gas:
        if get_year(i)==current_y:
            if get_price(i)>hi:
                hi=get_price(i)
        else:
            print('max_price_year in',current_y,':',format(hi,'.2f'))
            current_y=get_year(i)
            hi=get_price(i)
    print('max_price_year in',current_y,':',format(hi,'.2f'))# самая выс цена для последнего года

def min_price_year(gas):
    current_y=get_year(gas[0])# тек знач месяца
    mi=get_price(gas[0])# тек min знач в этой строке, т.е. в этом месяце
    for i in gas:
        if get_year(i)==current_y:
            if get_price(i)<mi:
                mi=get_price(i)
        else:
            print('min_price_year in',current_y,':',format(mi,'.2f'))#мин в этом году
            current_y=get_year(i)
            mi=get_price(i)
    print('min_price_year in',current_y,':',format(mi,'.2f')) # самая низкая цена для последнего года   
    
def average_month(gas):
    month_names = ['январь', 'февраль', 'март', 'апрель', 'май','июнь', 'июль', 'август', 'сентябрь', 'октябрь','ноябрь', 'декабрь']
    total=0
    count=0
    average=0
    current_m=get_month(gas[0])# тек знач месяца
    current_y=get_year(gas[0]) 
    for i in gas:
        if (get_month(i)==current_m) and (get_year(i)==current_y):
            total+=get_price(i)
            count+=1
        else:
            average=total/count
            #print(month_names[current_m-1],format(average,'.2f'),'year:',current_y)
            current_m=get_month(i)  #задаём новое тек знач месяца из списка gas
            current_y=get_year(i)
            total=0
            count=0
    print(month_names[current_m-1],format(average,'.2f'),'year:',current_y)# среднее за последний месяц
    
def average_year(gas):    
    for i in range(1993,2013+1):
        print(i,':',format(average_price(gas,i),'.2f'))
        
def average_price(gas,year):#принимает список строковых значений и год i=year и возвращает ср знач за год
    total=0
    count=0
    for i in gas:
        if get_year(i)==year:
            total+=get_price(i)
            count+=1
    average=total/count
    return average
            
def get_year(gas): 
    gas=str(gas) #чтобы разбить split(':') нужно gas перевести в str,т к до этого gas был записан в список - gas=g.readlines() 
    yea=gas.split(':')     # в формате ММ-ДД-ГГГГ:price
    year=yea[0].split('-') # в формате ММ-ДД-ГГГГ
    return int(year[2])    #вернуть год ГГГГ в int

def get_price(str):#построчно gas[0] ММ-ДД-ГГГГ:price  передаём значения и автоматически переводим из списка в str формат
    price=str.split(':') # разбиваем строку и переводим в список
    return float(price[1]) # отправляем price из ММ-ДД-ГГГГ:price

def get_month(str):
    month=str.split('-')
    return int(month[0])    
main()


##########################   13 
def main():
    lim=69
    nums=numb() # Перевести в список все лотерейные числа.
    fr=franc(nums,lim)# Получить частоту каждого числа.
    sort=most(fr) # Получить список наиболее распространенных значений.
    
    for i in range(10):  # Показать 10 наиболее распространенных чисел.
        print('sort[i]',sort[i])
    sort.reverse()
    for i in range(10):
        print('sort.revers()',sort[i])
    
def numb():    
    w=open(r'c:\Users\Павел\Desktop\pbnumbers.txt','r')
    n=w.readlines() # Прочтитать содержимое файла в список.
    w.close()
    print(n)
    for i in range(len(n)):  
        n[i]=n[i].rstrip('\n')
    print(len(n))
    print(n)
    nums=[]
    for i in range(len(n)): # Разбить каждый элемент на отдельные числа
        num=n[i].split()  # Разбить каждую строку
        for j in range(len(num)): # в каждой строке записать  в int
            nums.append(int(num[j]))
    print('nums',nums)
    return nums
def franc(n,lim):
    fr=[0]*(lim+1) ## Создать список для частоты каждого числа.
                   #Каждый элемент списка инициализируется нулем.
    print(n[0])
    for i in range(len(n)):
        nu=n[i]
        fr[nu]+=1# Увеличить частоту этого числа.    
    print('fr:',fr)
    return fr
def most(fr):
    print('fr:::',fr)
    sort=[]# Создать пустой список для позиций самых распространенных значений.
    temp=[]# Сделать копию списка fr.
    for i in fr:
       temp.append(i)

    for i in range(len(temp)):
        numpos=posh(temp)      #индекс наибольшей позиции
        sort.append(numpos)
        temp[numpos]=-1
    print('sort',sort)
    return sort

def posh(fr):
    h=0
    hpos=0
    #print('temp',temp)
    for i in range(len(fr)):
        if fr[i]>h:
            print('temp[i]',fr[i])
            h=fr[i]
            hpos=i  #индекс знач втречающиеся наиб кол раз = самому числу из списка fr[]
            print('hpos',hpos)
    return hpos               
main()

#### 12 v1
def main():
    tex=''
    t = input('Введите строковое значение: ')#Привет и Как Дела
    l=t.split()
    for i in range(len(l)):
        l[i]=l[i].upper()
        tex=l[i][1:] +l[i][0]+'ки'
        
        if len(l[i])==1:
            tex=l[i]+'ки'
        print(tex, end=' ') 
main()

#####  12 v2
def main():
    tex=''
    t = input('Введите строковое значение: ')#Привет и Как Дела
    l=t.split()
    for i in range(len(l)):
        li=l[i].upper()
        
        if len(li)==1:  # Для однобуквенных слов
            tex+=li+'ku'
        else:
            tex+=li[1:]+li[0]+'ku'   # Для слов с двумя и более буквами, 

        if i<len(l)+1: # Если есть еще слова, то добавить к результату пробел.
            tex+=' '
    print(tex)
main()

##### 11 v1
def main():
    tex=''
    t = input('Введите строковое значение: ')#ПриветКакДела
    print(t[0])
    tex=tex+t[0].upper()
    for i in t[1:]:
        #tex+=i
        if i.isupper():
            i=i.lower()
            #tex.replace(i,i.lower())
            tex+=' '
        tex+=i
    print(tex)   
main()


##### 10 v1
def main():
    li=[]
    t=input('text: ')
    for i in range(len(t)):
        g=0
        for j in t:
            if j in t[i]:
                if j!=' ' and j!='.': #кроме этотих символов
                    g+=1
        li.append(g)  
    print(li)
    m=max(li)    #Если несколько символов имеют  одинаковую самую высокую частоту, то она показывает  первый символ с этой частотой.
    y=li.index(m)        
    print('try',m,'\n','index',y,'\n','article',t[y].upper())
main()

#### 10 v2
def main():
    li=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
	         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    let = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    fr=0
    us = input('Введите строковое значение: ')
    for i in us:
        i=i.upper()
        ind=let.find(i)
        if ind>=0:
            li[ind]+=1

    for i in range(len(li)):  #находим самую частую букву
        if li[i]>li[fr]:
            fr=i
    print(let[fr])
main()

#### 9 v1
def main():
    lg=['a','e','i']
    ls=['b','c','d','f']
    t=input("text: ")
    fung(t,lg)
    funs(t,ls)    
def fung(t,lg):
    tg=0    
    for i in t:
        for j in range(len(lg)):
            if i.lower()==lg[j]:                
                tg+=1               
    print('glas: ',tg)
    
def funs(t,ls):    
    ts=0
    for i in t:
        for j in range(len(ls)):
            if i.lower()==ls[j]:                
                ts+=1
    print('sogl: ',ts)
main()

######  9 v2
def main():
    g='аеёиоуыэюя'
    s= 'бвгджзйклмнпрстфхцчшщъь'
    t=input("text: ")
    fung(t,g)
    funs(t,s)    
def fung(t,g):
    tg=0    
    for i in t:
        for j in range(len(g)):
            if i.lower()==g[j]:                
                tg+=1               
    print('glas: ',tg)
    
def funs(t,s):    
    ts=0
    for i in t:
        for j in range(len(s)):
            if i.lower()==s[j]:                
                ts+=1
    print('sogl: ',ts)
main()

####### 9 v3
def main():
    g='аеёиоуыэюя'
    s= 'бвгджзйклмнпрстфхцчшщъь'
    t=input("text: ")
    fg=fung(t,g)
    fs=funs(t,s)
    print('sogl: ',fs,'glas: ',fg)
    
def fung(t,g):
    tg=0    
    for i in t:
        if g.find(i.lower())>=0:               
                tg+=1               
    return tg
    
def funs(t,s):    
    ts=0
    for i in t:
        if s.find(i.lower())>=0:                
                ts+=1
    return ts
main()

##### 8 v1
def main():    
    t=input("enter: ")    
    #print(t[-1])
    fun(t)
def fun(t):
    t+='  '
    ind=0    
    #print(len(t))
    print(t[0].upper(),end='')
    while ind<(len(t)-1):        
        ind+=1
        print(t[ind],end='')
                    
        if t[ind]=='?'and t[ind]!=t[-1]:           
            ind+=1
            print(t[ind],end='')
            ind+=1
            print(t[ind].upper(),end='')            
        if t[ind]=='!'and t[ind]!=t[-1]:
            ind+=1
            print(t[ind],end='')
            ind+=1
            print(t[ind].upper(),end='')
            
        if t[ind]=='.'and t[ind]!=t[-1]:
            ind+=1
            print(t[ind],end='')
            ind+=1
            print(t[ind].upper(),end='')            
        #if  t[-1]=='.' or t[-1]=='?' or t[-1]=='!':
            #ind==(len(t)-1)
               
main()

########## 8 v2
def main():    
    t=input("enter: ")    
    tt=fun(t)
    print(tt)
    
def fun(t):
    gen=True
    text=''
    words=''
    li=t.split()
  
    for i in li:                
        if gen:           # Создать новое слово, в котором первый символ
                          # переведен в верхний регистр.		
            text=i[0].upper()+i[1:]
        else:
            text=i 
        
        if i[-1]=='!' or i[-1]=='.' or i[-1]=='?':
            gen=True
        #else:
            #gen=False            
        words+=text +' '
    return words              
main()


##### 7
def main():
    d=0
    u=0
    l=0
    s=0
    x=open(r'c:\text.txt','r')
    y=x.read()
    for i in y:
        if i.isdigit():
            d+=1
        if i.isupper():
            u+=1
        if i.islower():
            l+=1
        if i.isspace():
            s+=1
    x.close()
    print(d,u,l,s)
main()


#### 6
def main():
    s=0
    t=0
    x=open(r'c:\text.txt','r')
    f=x.readline()
    print(f)
    while f!='':
        #print(f)
        s+=1#sentensis
        tt=0#word in sentens
        for i in f:
            if i==' ':                
                t+=1#word
                tt+=1#word in sentens
        print('word',  t,'sentensis',s,'word in sentens',tt)
        f=x.readline()
    print('mid words: ',format(t/s,'.2f'))
main()

##### 5
def main():
    num=''
    li1=['a','b','c','d','e','f','g','h','i']
    li2=['2','3','4']
    n=input(":")
    print(li1,li2)
    for i in n:
        #if i.isdigit():
            #print(i,end='')            
        if i.isalpha():
            if i=='a' or i=='b' or i=='c':
                #print('2',end='')
                ind=0
            if i=='d' or i=='e' or i=='f':
                #print('3',end='')
                ind=1
            if i=='g' or i=='h' or i=='i':
                #print('4',end='')
                ind=2
            i=li2[ind]
        num+=i# Конкатенировать цифры в строковое значение.
    print(num,end='')
            #print(li2[ind],end='')
main()

######  4
def main():
    li1=[' ',',','.']
    li2=['.-','-...','-.-.']
    n=input(":")
    print(li1,li2)
    for i in n:
        ii=li1.index(i)
        print(li2[ii],end='')
main(

##### 3 v1
def main():
    d=input("data: ")
    li=d.split('/')
    print(int(li[1]))
    fun(li)
    sh(li)
def fun(li):    
    for i in li:
        if li[1]=='01':
            li[1]='jun'
        if li[1]=='02':
            li[1]='feb'            
        if li[1]=='03':
            li[1]='mar'
    return li

def sh(li):            
    for i in li:        
        print(i,'',end='')
    print('г.')
main()

#####3 v2
def main():
    m=['jun','feb','mar']
    d=input("data: ")
    li=d.split('/')
    print(li)
    day=li[0]    
    m1=m[int(li[1])-1]    
    y=li[2]    
    tot=day + ' ,'+ m1+ ' '+ y +' г'
    print(tot)
main()


###### 2
def main():
    n=input('num: ')
    su=fun(n)
    print(su)
def fun(n):
    s=0
    for i in n:
        s+=int(i)
    return s   
main()

#### 1 v1
def main():
    f=input("first name: ")
    l=input(' last name: ')
    o=input('otchestvo: ')
    print(f[0].upper(),'.',l[0],o[0],sep='')
main()

#v2
def main():
    f='Kov Pav vic'
    li=f.split()
    print(li[0][0],'.',sep='')
    print(li[1][0],'.',sep='')
    print(li[2][0].upper(),'.',sep='')    
main()

#v3!!!!
def main():
    f='Kov Pav vic'
    li=f.split()
    for i in li:
        print(i[0].upper(),'.',sep='',end='')
main()
