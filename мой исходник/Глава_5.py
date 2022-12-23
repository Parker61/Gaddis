##### 27
def screen_setup():
	# Настроить экран
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    turtle.bgcolor('black')

 
############## 26
import turtle
# Функция square чертит квадрат. Параметры x и y являются
# координатами левого нижнего угла. Параметр width
# является шириной каждой стороны.
def square(x, y, width, color):  # Функция square чертит квадрат
    turtle.penup()            # Поднять перо
    turtle.goto(x, y)         # Переместить в указанную позицию
    turtle.fillcolor(color)   # Задать цвет заполнения
    turtle.pendown()          # Опустить перо
    turtle.begin_fill()       # Начать заполнение
    for count in range(4):    # Начертить квадрат
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()         # Завершить заполнение

def main():
    turtle.speed(0)
    turtle.hideturtle()
    color = 'black'

    for y in range(250, -250, -100):
        for x in range(-250, 250, 100):
            square(x, y, 100, color)
            if color == 'black':
                color = 'white'
            else:
                color = 'black'
main()

    
#############  25
import turtle
def main():
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    w = 100
    h = 80
    rectangular_pattern(w, h)
# Именованные константы
ANIMATION_SPEED = 9
BASE_X = 0
BASE_Y = 0
def rectangle(x, y, width, height, color):
    turtle.setheading(0)
    turtle.fillcolor(color)     # Задать цвет заполнения
    turtle.penup()              # Поднять перо
    turtle.goto(x, y)           # Переместить в указанную позицию
    turtle.pendown()            # Опустить перо    
    # Начертить прямоугольник.
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()    
def lines(x1,y1,x2,y2): # Начертить линиии гориз и вертик
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)    
def rectangular_pattern(width, height):
    # Узор состоит из 3 вложенных прямоугольников, в которых
    # диагональные отрезки соединяют углы и четыре стороны.	
    # Начертить самый внешний прямоугольник.
    rectangle(BASE_X, BASE_Y, width, height, 'white')
    # Начертить средний прямоугольник.
    middle_x = BASE_X + width / 8
    middle_y = BASE_Y + height / 8
    middle_width = width - width / 4
    middle_height = height - height / 4
    rectangle(middle_x, middle_y, middle_width, middle_height, 'white')
    # Начертить самый внутренний прямоугольник.
    inner_x = BASE_X + width / 4
    inner_y = BASE_Y + height / 4
    inner_width = width - width / 2
    inner_height = height - height / 2
    rectangle(inner_x, inner_y, inner_width, inner_height, 'black')
    # Начертить диагональные соединяющие отрезки.
    lines(BASE_X, BASE_Y,inner_x, inner_y)
    lines(BASE_X + width, BASE_Y + height,inner_x + inner_width, inner_y + inner_height)
    lines(BASE_X + width, BASE_Y,inner_x + inner_width, inner_y)
    lines(BASE_X, BASE_Y + height,inner_x, inner_y + inner_height)
    # Начертить горизонтальные соединяющие отрезки.
    lines(BASE_X, BASE_Y + height / 2, inner_x, BASE_Y + height / 2)
    lines(BASE_X + width, BASE_Y + height / 2, inner_x + inner_width, BASE_Y + height / 2)
    # Начертить вертикальные соединяющие отрезки.
    lines(BASE_X + width / 2,BASE_YBASE_X + width / 2,inner_y,)
    lines(BASE_X + width / 2,BASE_Y + height,BASE_X + width / 2,inner_y + inner_height)
main()
#############  23
import turtle
def main():    
    tr(0, 0, 100, 0, 0, -100, 'red')
    tr(0, 0, -100, 0, 0, -100, 'green')
    tr(0, -100, -100, -200, 100, -200, 'blue')

def tr(x1, y1, x2, y2, x3, y3, color):
    turtle.fillcolor(color)
    turtle.penup()
    turtle.goto(x1, y1)

    turtle.pendown()
    turtle.begin_fill()
    
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()   
main()
#############  22
import random
def main():
    x=random.randint(1,3)
    print("comp",x)
    y=int(input("num: "))
    print(y)
    gen(x,y)
    
def gen(x,y):
    if x==1 and y==2 or x==2 and y==3 or x==3 and y==1:
        print("win comp")   
    elif x==y:
        print("win both")
    elif y>3:
        print("from 1 till 3 number")
    else:
        print("win user") 
main()

#############  21 v1 почему то не работает?
import random
def main():   
    g=0
    x=1
    #while x>0:
    g=random.randint(1,100)
    print(g)
    x=gen(g)            
    print(x,'Спасибо за игру!')    

def gen(g):    
    u=int(input("num: ")        

    while u > 0:
        if u>g:  
            t1+=1
            print("по-меньше")
            u=int(input("num: ")
        elif u<g:
                t2+=1
                print("по-больше")
                u=int(input("num: "
        else:
            print("win")
            return u
    return u        
    #print('t1',t1,'t2',t2,'g',g)
main()

#############  21 v2
import random
def main():
    #g = 0
    #x = 1

    # Продолжить представлять числа для угадывания пользователю
    # то тех пор, пока пользователь желает продолжать игру.
    #while(x > 0):
    g = random.randint(1, 100)
    print(g)
    x = gen(g)
    #play = playGuessingGame(number)
    print(x,'Спасибо за игру!')
# Функция playGuessingGame получает в качестве аргумента
# число, которое пользователю нужно угадать и предлагает
# пользователю его угадать. Если пользователь угадывает неправильно,
# то он получает об этом сообщение, и ему предлагается попытаться еще.
# В противном случае возвращается догадка пользователя. 
def gen(g):
    # Получить догадку пользователя.
    u = int(input('Введите число между 1 и 100, ' \
                          'либо 0, чтобы завершить игру: '))
    # До тех пор, пока пользователь не хочет прекратить игру
    while u > 0:
        if u > g:
            print('Слишком высоко, попробуйте еще раз')
            u = int(input('Введите число между 1 и 100, ' \
                                  'либо 0, чтобы завершить: '))
        elif u < g:
            print('Слишком низко, попробуйте еще раз')
            u = int(input('Введите число между 1 и 100, ' \
                                  'либо 0, чтобы завершить: '))
        else:
            print('Поздравляем! Вы угадали правильное число!')
            return u  # Start the game again
    return u # userGuess равно 0, и пользователь хочет завершить.
main()
#################   19
def main():
    n = int(input('Введите целое число больше 1: '))
    
    for i in range(1,n+1):        
        if func(i):
            print(i,"простое")
        else:
            print(i,"составное")
              
def func(i):
    status=True
    for j in range(2,i):
        if i%j==0:            
            status = False
    return status
main()

#################   18
def main():
    n = int(input('Введите целое число больше 1: '))
    func(n)
    if func(n):
        print("составным")
    else:
        print("простое")
              
def func(n):
    for i in range(2,n):
        if n%i==0:
            return True
main()


#17
#v1
import random
def main():
     t1=0
     t2=0
     r=int(input("range: "))     
     for z in range (r):
          num=random.randint(1,100)
          print(num)
          if num%2==0:
               t1+=1
          else:
               t2+=1
     print ("чётных: ",t1)
     print ("нечётных: ",t2)            
main()

#V2
import random
def main():
     t1=0
     t2=0
     r=int(input("range: "))     
     for z in range (r):
          num=random.randint(1,100)
          print(num)
          if func(num):
               t1+=1
          else:
               t2+=1
     print ("чётных: ",t1)
     print ("нечётных: ",t2)
def func(num):
     if num%2==0:
          return True          
     else:
          return False              
main()

#16
def main():
     x1=int(input("x1: "))
     x2=int(input("x2: "))
     a=calc_average(x1,x2)
     print ("x1: \t",x1, determine_grade(x1))
     print ("x2: \t",x2, determine_grade(x2))
     print("calc_average: ",a,"determine_grade: ",determine_grade(a))
def calc_average(x,y):
     return round((x+y)/2)# огруглить до целого
def determine_grade(z):
     if z>=90:
          return "A"
     elif z>=80:
          return "B"
     elif z>=70:
          return "C"
     elif z>=60:
          return "D"
     else:
          return "F"     
main()

#15
def main():
     m=float(input("m: "))
     v=float(input("v:"))
     k=kinetic (m,v)
     print ("kinetic: ", format(k,".2f"))   
def kinetic (m,v):
     k= 1/2*m*v**2
     return k
main()


#14 
g=9.8
def main():      
     for t in range(1,11):
          falling_distance(t)
def falling_distance(t):
     h=(1/2*g*t**2)
     print("time:",t,"- h:",(format(h,'.1f')))  
main()

################ 13
def main():
    n1=int(input("num1: "))
    n2=int(input("num1: "))
    f=func(n1,n2)
    print(f)
def func(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
main()

#################  11,12
import random
def main():
    li=[]
    for i in range(2):
        n1=random.randint(1,100)
        print(n1)
        li.append(n1)

    #print("sum",sum(li),li)
    s=sum(li)
    np=int(input("your sum: "))
    
    show(np,s)
    if show(np,s):
        print(s,"WIN!equals")
    else:
        print(s,", wrong, try again",sep='')
        
def show(np,s):
    status=False
    if np==s:
        status=True
    return status 
main()

#9
fedt=0.05
munt=2.5
def main():
     s=int(input("S: "))
     m=mun(s,munt)
     f=fed(s,fedt)
     t=tt(m,f)
     show (m,f,t)
def mun (s,munt):
     return s*munt
def fed (s,fedt):
    return s*fedt
def tt (m,f):
     return m+f
def show (m,f,t):
     print(m,f,t)
main()


#8
w_hours=2000
m2_colour=5/10
m2_hours=8/10
def main():
     s=int(input("S: "))
     pr=int(input("price 5L colour: "))
     my_nv=nv(s,m2_colour)
     my_h=hour(s,m2_hours)
     my_p=price_colour(my_nv,pr)
     my_w=price_work(w_hours,my_h )
     total_price=my_p+my_w
     show(my_nv, my_h, my_p, my_w, total_price)
     #print(my_nv, my_h, my_p, my_w, total_price)
def nv(x,y):
     z=x*y
     return z
def hour(x,y):
     z=x*y
     return z
def price_colour(x,y):
     z=x*y
     return z
def price_work(x,y):
     z=x*y
     return z
def show(a,b,c,d,e):
     print("nv",a, "hour",b,"price_colour",c,"price_work",d,"total_price",e)
main()

#7
a1=20
a2=15
a3=10
def main():
     a=float(input("a: "))
     b=float(input("b: "))
     c=float(input("c: "))
     
     profit (a,b,c)
def profit (x,y,z):
     a=x*a1
     b=y*a2
     c=z*a3
     print(a,b,c)
main()

#4
def main():
     oil=float(input("oil: "))
     gas=float(input("gas: "))
   
     coust (oil,gas)
def coust (x,y):
     mo= x+y
     ye=mo*12
     print ("mo: ", mo)
     print ("ye: ", ye)
main()

#3
c=0.8
fed=0.03
def main():
     coust=float(input("coust: "))
     insurance (coust)
     
     
def insurance (coust):
     su= c*coust
     print ("insurance: ", su)

main()

#2
reg=0.02
fed=0.03
def main():
     sales=float(input("sales: "))
     y=reg_t(sales)
     x=fed_t(sales)
     t=fed_t(sales)+reg_t(sales)
     print ("total: ", t,'$',sep='')
     print ("reg_t: ", y)
     print ("fed_t: ", x)
def reg_t (x):
     tr= reg*x
     return tr
def fed_t (x):
     tf= fed*x
     return tf
main()



#1
k=0.6214
def main():
        
    km=float(input("km: "))
    miles(km)
def miles(km):
     m=k*km
     print("miles: ",format(m,'.2f'))
     print ("km: ", km)
main()
