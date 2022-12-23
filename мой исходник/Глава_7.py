#алгоритмический тренажёр
#8 создание двумерного списка
li = []
rows=5
cols=3
for r in range(rows):
    li.append([])
    for c in range (cols):
        li[r].append(0)
print(li)
print(len(li)) #считывет кол строк rows, т.е. кол-во эл []

for r in range(len(li)):  #считывет кол строк rows, т.е. кол-во эл []
    
    for c in range(len(li[r])): #считывет кол столбцов cols в строке,
                                #т.е. кол-во эл в строке [кол-во эл в строке]
        li[r][c]=input("num: ") 
print(li)

#1
def main():
    sales=[]
    days=[1,2,3,4,5,6,7]
    t=0
    for x in range(len(days)):    
        print("day",x+1)
        s=float(input("sales: "))
        sales.append(x)
        t+=s      
    print("total sales:",t,"for",len(days),"days")
    print("list sales:",sales)
main()

#1 v2
def main():
    t=0
    days=3
    sales=[]    
    for r in range(days): #создаём список с кол-м эл = days
        sales.append([0])    
    print(sales)
    
    for x in range(days): #для каждого индекса запись соотв продаж
        sales[x]=float(input("sales:"))
    for x in sales: # расчет суммирует все эл в списке
        t+=x
    print("Total",t)
main()


#2
import random
def main():
    n=[0]*7
    print(len(n))
    
    for r in range(len(n)):
        n[r]=random.randint(0,9)
    print(n)
    
    for r in range(len(n)):
        print(n[r],end='    ')
main()

#2
def main():
    t=0
    mounth=3
    li=[0]*mounth
    print(len(li))
    mo=[0]*mounth 
    for r in range(len(li)):#создаём месяца списком
        mo[r]=r+1
    print(mo)

    for r in range(len(li)): #вводим данные в список
        li[r]=float(input("presepetation " \
                          +str(mo[r])+":"))

    for r in range(len(li)): 
        t+=li[r]            #суммируем
    tm=t/len(li)#среднее
    hmi=li.index(max(li))#нах индекс мес с макс знач в li[]
    #x=max(li)
    hm=mo[hmi]  #нах знач в месяце соответвующее макс в li[]
    hli=li.index(min(li))#нах индекс мес с мин знач
    hl=mo[hli]
    print(t,"среднее",format(tm,'.2f'),"max mo",max(li),"min mo",min(li),
          "max",hm,"min",hl)
main()


#4
def main():
    nq=10
    n=3
    num=[0]*n
    for r in range(len(num)):                  
                   num[r]=float(input("num from 1 to "+\
                                      str(nq)+\
                                      ": "))                   
    tot=sum(num)               
    tm=tot/len(num)
    th=max(num)
    tl=min(num)
    print(tot,format(tm,'.2f'),th,tl)
main()


#5 v1
def main():
    try:        
        t=0
        num=[]
        d=open (r'c:\Users\Павел\num.txt','r')
        r=d.readline()        
        print(r)# вывод 1-го зночение из файла
        while r!="":
            r=r.rstrip('\n')
            num.append(r)#запись по строчно в список
            r=d.readline()
        d.close()
        print(num)#вывод списка
        
        p=input("pass: ")#ввод значение как str
        
        if p in num:#всё видит как str             
              print("true")
        else:
            print("false, try again")
            
    except IOError:
        print("not num")    
main()
#5 v2
def main():
    try:        
        d=open (r'c:\Users\Павел\num.txt','r')
        li=d.readlines() #читаем весь файл одной строкой       
        for i in range(len(li)):
            li[i]=li[i].rstrip('\n')#убрали \n в каждом эл           
        print(li)
        d.close()
        
        p=input("pass: ")#ввод значение как str
        
        if p in li:#всё видит как str             
              print("true")
        else:
            print("false, try again")
            
    except IOError:
        print("not num")    
main()


#6 v1
def main():
    n=int(input("enter n: "))
    w=open(r'c:\Users\Павел\num.txt','r')
    nu=w.readlines()
    for i in range(len(nu)):
        nu[i]=nu[i].rstrip('\n')
        
    for i in range(len(nu)):
        if n<int(nu[i]):
            print(nu[i])
      
    print(nu)
main()

#6 v2
def main():
    #num=[1,2,3,4,5,6,7,8,9,19]
    n=int(input("enter n: "))
    w=open(r'c:\Users\Павел\num.txt','r')
    num=w.readlines()
    for i in range(len(num)):
        num[i]=num[i].rstrip('\n')
        num[i]=int(num[i]) #перевести из str в int
    print(num)
        
    func(n,num)     #задать значения в функцию
    
def func(n,num):
    
    f=[]            #создать список куда будут писаться значения которые больше n
    for i in num:   #перебрать каждое число из списка
        
        if i > n:
            f.append(i)   # добавить если больше
    print(f)
main()

#6 v3 its ok
def main():
    n=int(input("enter n: "))
    w=open(r'c:\Users\Павел\num.txt','r')#берём список
    num=w.readlines() #считываем
    for i in range(len(num)):
        num[i]=num[i].rstrip('\n')#удаляем \n
        num[i]=int(num[i]) #перевести из str в int
    print(num)
        
    func(n,num)     #передать значения n и  списка num в функцию
    
def func(n,num):    
    f=[]            #создать список куда будут писаться значения которые больше n
    for i in range(len(num)):   #перебрать каждое число из списка        
        if num[i]>n:
            f.append(num[i])   # добавить если больше
    print(f)
main()


#7 v1
def main():
        tru=[]
        fal=[]
        t=0
        numfal=[]
        ans = ['a', 'C', 'a', 'A', 'd','b', 'C', 'a','C', 'B','A', 'D','C', 'A', 'D',
                'C', 'B', 'B', 'D', 'A']
        x=open(r'c:\Users\Павел\student_solution.txt', 'r')
        orig=x.readlines()

        for i in range(len(orig)):
            orig[i]=orig[i].rstrip('\n')# отсекли \n

        for i in range(len(orig)): #сравниваем значения в списках ans
            if orig[i]==ans[i]:
                 )
                print("TRUe,",i+1,":",ans[i])
            else:
                fal.append(ans[i])
                t+=1
                numfal.append(i+1)
                print("FAiL,",i+1,":",ans[i],"it should be",orig[i])
                
        if len(tru)>=15:
            print("test done")
        else:
            print("!!!test not done!!!") 
        print("TRUE",len(tru),"FALSE",t,"num wrongs:",numfal)        
main()

#7 v2
def main():
        tru=[]
        fal=[]
        numfal=[]
        x=open(r'c:\Users\Павел\student_solution.txt', 'r')
        orig=x.readlines()
        stud=[]        
        for i in range(len(orig)):
            orig[i]=orig[i].rstrip('\n')# отсекли \n
        print(orig,stud) #создали 2 списка

        for i in range(len(orig)):            
            stud.insert(i,input("enter letter: "))
        print("НАБРАННЫЕ ЗНАЧЕНИЯ",stud) # вставили заначения в stud[]

        for i in range(len(orig)): #сравниваем значения в списках stud

            if orig[i]==stud[i]:
                tru.append(stud[i])#добаляем в список tru
                print("TRU",i+1,":",stud[i])
            else:
                fal.append(stud[i])#добаляем в список fal
                numfal.append(i+1)    #запись в список с неправильными ответами
                print("FAL",i+1,":",stud[i],"it should be",orig[i])
                
        if len(tru)>=15:
            print("test done")
        else:
            print("!!!test not done!!!") 
        print("TRUE",len(tru),"FALSE",len(fal),"№ wrong answers",numfal)
main()

#8
def main():
    try:        
        xb=open(r'c:\Users\Павел\BoyNames.txt','r')
        xg=open(r'c:\Users\Павел\GirlNames.txt','r')
        b=xb.readlines()
        g=xg.readlines()
        for i in range (len(b)):
            b[i]=b[i].rstrip('\n')
        for i in range (len(g)):
            g[i]=g[i].rstrip('\n')

        ng=input("name girl: ")
        nb=input("name boy: ")
        
        if ng=='' or ng=='no':# сравнить для девочек
            print()            
        elif ng in  g:
            print('there is such a name:',ng)
        else:
            print('there is no such a name girl')
            
        if nb=='' or nb=='no':# сравнить для мальчиков
            print()            
        elif nb in  b:
            print('there is such a name:',nb)
        else:
            print('there is no such a name girl')  

    except ValueError:
        print("none,try again")
main()

#9
def main():
    try:
        t=0
        x=open(r'c:\Users\Павел\USPopulation.txt','r')
        p=x.readlines()
        for i in range(len(p)):
            p[i]=p[i].rstrip('\n')
            p[i]=int(p[i])
        dp=[]
        i=0
        dp.append(p[i])
        for i in range((len(p)-1)):#запись дельты по годам
            dp.append(p[i+1]-p[i])

        del dp[0]
        for i in range(len(dp)):
            t+=dp[i]
            
        print(dp)
        print(max(dp))
        print(min(dp))
        yim=dp.index(max(dp))
        yii=dp.index(min(dp))
        print("medium:",format(t/len(dp),'.1f'),"max",max(dp),"in:",yim+1951,"min",min(dp),"in:",yii+1951)
    except:
        print("Error")
main()

#9 v2 красивее
def main():
    try:
        x=open(r'c:\Users\Павел\USPopulation.txt','r')
        p=x.readlines()
        for i in range(len(p)):
            p[i]=p[i].rstrip('\n')
            p[i]=int(p[i])
        dp=[]
        i=0

        for i in range(len(p)-1):#запись дельты по годам
            dp.append(p[i+1]-p[i])# 1951-1950
            
        tot=sum(dp)
        yim=dp.index(max(dp))
        yii=dp.index(min(dp))
        print("mean:",format(tot/len(dp),'.2f'),"max",max(dp),"in:",yim+1951,"min",min(dp),"in:",yii+1951)
    except:
        print("Error")
main()


#10
def main():
    try:
        t=0        
        x=open(r'c:\Users\Павел\WorldSeriesWinners.txt','r')
        w=x.readlines()
        for i in range(len(w)):
            w[i]=w[i].rstrip('\n')
            
        s=input("seek: ")
        if s not in w:
            print("not team")
        else: 
            for i in range(len(w)):
                if s==w[i]:
                    t+=1
            print("it is true",t)
            
    except:
        print("Error")
main()



#11
def main():    
    t=0
    r=3#строки
    c=3#столбцы
    sq=[]
    ss=[ [4, 9, 2],
         [3, 5, 7],
         [8, 1, 6] ]
    sum_r0=sum(ss[0]) #sum_r0= ss[0][0]+ ss[0][1]+ss[0][2] сумма строк
    sum_r1=sum(ss[1])
    sum_r2=sum(ss[2])
    print(sum_r0,sum_r1,sum_r2)
    sum_c0=ss[0][0]+ss[1][0]+ss[2][0]# сумма по столбцам
    sum_c1=ss[0][1]+ss[1][1]+ss[2][1]
    sum_c2=ss[0][2]+ss[1][2]+ss[2][2]
    print(sum_c0,sum_c1,sum_c2)
    sum_d1=ss[0][0]+ss[1][1]+ss[2][2]#сумма по диагонали
    sum_d2=ss[0][2]+ss[1][1]+ss[2][0]
    print(sum_d1,sum_d2)
    if sum_r0==sum_r1==sum_r2== sum_c0 ==sum_c1 ==sum_c2 ==sum_d1 ==sum_d2:
        print("good square!",ss)
    else:
        print("usually square",ss)

    squ(ss,r,c)

def squ(ss,r,c):    
    for v in range(r):
        for w in range(c):
            print(ss[v][w])

main()

#######################################################  11
def main():    
    t=0
    r=3#строки
    c=3#столбцы
    minn=1
    maxx=9
    ss=[]
    ss=[ [4, 9, 2],
         [3, 5, 7],
         [8, 1, 6] ]
    #for v in range(r): #создание списка
        #ss.append([])
        #for w in range(c):            
            #ss[v].append(input("first letter:"))    
    print(ss)

    fshow(ss,r,c)
   
    squ(ss,r,c,minn,maxx)
    
    if squ(ss,r,c,minn,maxx):#если status=True в def squ: 
        print("good square!")
    else:
        print("usually square")
        
def fshow(ss,r,c):#показать все цифры таблицы построчно
    for v in range(r):
        for w in range(c):            
            print(ss[v][w],end=' ')
        print()
        
def squ(ss,r,c,minn,maxx):
    status=False    
    ra=frange(ss,r,c,minn,maxx)
    un=funi(ss,r,c,minn,maxx)
    sr=fsr(ss,r,c) #sum_r0= ss[0][0]+ ss[0][1]+ss[0][2] сумма строк
    sc=fsc(ss,r,c)
    sd=fsd(ss,r,c)
    if ra  and un and sr and sc and sd:
        status=True
    return status    

def frange(ss,r,c,minn,maxx):
    status=True
    for v in range(r):
        for w in range(c):
            if ss[v][w] < minn or \
               ss[v][w] > maxx:
                status = False              
    return status
            
def funi(ss,r,c,minn,maxx):
    status=True
    t=0
    sear=minn
    while sear<=maxx and status==True:      
        for v in range(r):
            for w in range(c):                
                if ss[v][w]==sear:
                    t+=1        
                if t>1:
                    status=False
        sear+=1
        t=0
    return status
        
def fsr(ss,r,c):
    status =True
    sum_r0=sum(ss[0]) 
    sum_r1=sum(ss[1])
    sum_r2=sum(ss[2])
    #print(sum_r0,sum_r1,sum_r2)
    if sum_r0!=sum_r1!=sum_r2:
        status=False
    return status

def fsc(ss,r,c):
    status =True
    sum_c0=ss[0][0]+ss[1][0]+ss[2][0]# сумма по столбцам
    sum_c1=ss[0][1]+ss[1][1]+ss[2][1]
    sum_c2=ss[0][2]+ss[1][2]+ss[2][2]
    #print(sum_c0,sum_c1,sum_c2)
    if sum_c0!=sum_c1!=sum_c2:
        status=False
    return status    
    
def fsd(ss,r,c):
    status =True
    sum_d1=ss[0][0]+ss[1][1]+ss[2][2]#сумма по диагонали
    sum_d2=ss[0][2]+ss[1][1]+ss[2][0]
    #print(sum_d1,sum_d2)
    if sum_d1!=sum_d2:
        status=False
    return status    
main()

############################   12
def main():
    n=int(input("num: "))
    li=[]    
    for r in range(2,n): #создаём список с кол-м эл нач с 2-х и до n-1
        li.append(r)    
    print(li)
    
    func(li,n)
    if func(li,n):
        print(n,"prime number")
    else:
        print(n, 'составное число')
        
def func(li,n):
    status=True
    for i in (li):
        if n%i==0:
            print(n,"делится на:",i)
            status=False
    return status
main()

########12 v2 ok
def func(n):
    status = False
    
    for i in range(2, n):
        if n % i == 0:
            status = True

    if status:
        print(n, 'является составным.')
    else:
        print(n, 'является простым.')

def main():
    # Получить от пользователя целое число.
    usn = int(input('Введите целое число больше 1: '))
    li = []  
    # Заполнить список числами.
    for i in range(2, usn + 1):
        li.append(i)
    # Определить, является ли каждый элемент простым или составным.
    for i in range(len(li)):
        func(li[i])
main()


###############13
#13
import random
def main():
    z=open(r'c:\Users\Павел\8_ball_responses.txt','r')
    l=z.readlines()
    z.close()    
    for i in range(len(l)):
           l[i]=l[i].rstrip('\n')
    print(len(l))

    again='y'
    while again=='y':
        n=input("questin:")
        sh=random.randint(1,len(l))# случ число от 1 до len(l)включительно
        print(l[sh])
        again=input("more quastin?") 
main()

############################  14
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family']     = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize']  = (4, 3.8)#размер окна 
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9    #шрифт

def main():
    x=open(r'c:\Users\Павел\expenses.txt','r')
    li=x.readlines()
    for i in range(len(li)):
        li[i]=li[i].rstrip('\n')
    x.close()
    print(li)
    m=['rent','pays','oil','food','clothers','pay for cars']
    plt.pie(li,labels=m)
    plt.title("costs")
    plt.show()
main()

################################### 15
import matplotlib.pyplot as plt

def main():
    x=open(r'c:\Users\Павел\1994_Weekly_Gas_Averages.txt','r')
    li=x.readlines()         #Y ось ординат
    for i in range(len(li)):
        li[i]=li[i].rstrip('\n')
    #print(li,len(li))
    w=[]                   #X ось абсцисс
    for i in range(len(li)):     #недели
        w.append(i)        
  
    print(w,len(li))
    xc=w
    yc=li
    plt.plot(xc,yc,marker='*')
    plt.title('price for oil in 1994')
    plt.xlabel("weeks")
    plt.ylabel("price for oil")
    plt.xlim(xmin=1,xmax=52)
    plt.ylim(ymin= 0.995 ,ymax= 47)
    plt.xticks([0,26,52],[0,26,52])
    plt.yticks([0,26,52],[0.992,1.04,1.125])
    plt.grid(True)

    plt.show()
main()
################################### 15 v2
import matplotlib.pyplot as plt

def main():
    t=0
    r=open(r'c:\Users\Павел\1994_Weekly_Gas_Averages.txt','r')
    y=r.readlines()                   #Y ось ординат priceсписок y[]
    for i in range(len(y)):
        y[i]=y[i].rstrip('\n')
    print(y,len(y))
    
    x=[]                           #X ось абсцисс
    for i in range(1,len(y)+1):     #список снеделями список x[] weeks
        x.append(i)
        
    n=len(y)# кол недель 52
    
    for i in range(len(y)):        # находим сумму
        t+=float(y[i])
    
    ser=t/len(y)     # находим среднее
    num=str(1.079)   #перевод в str чтобы передать в функцию примерно равное ser 1.078
    imed=y.index(num)
    #ii=float(ii)
    print(y[51],"imed",imed,"ser:",format(ser,'.3f'),x,len(y),n,y[n-1])
    
    plt.plot(x,y,marker='*')
    plt.title('price for oil in 1994')
    plt.xlabel("weeks")
    plt.ylabel("price for oil")
    plt.xlim(xmin=1,xmax=n)
    plt.ylim(ymin= 0.995 ,ymax= n)
    plt.xticks([0,imed,n],[x[0],imed,n]) # т к отсчёт с индекса 0 по 51 чтобы было 52 недели
    plt.yticks([0,imed,n],[y[0],num,y[n-1]])# т к отсчёт с 1 по 53 чтобы было 52 недели
    plt.grid(True)

    plt.show()
main()
