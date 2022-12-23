#18
#v1
import turtle
turtle.speed(0)
turtle.right(270)

for x in range (1,500,10):
     turtle.forward(x)
     turtle.left(90)




#17
import turtle
turtle.speed(6)
for x in range (8):
     turtle.forward (300)
     turtle.left(135)
turtle.hideturtle()

#16
#v1
import turtle
turtle.speed(0)
turtle.setheading(90)
turtle.penup()
turtle.goto(300,-300)
turtle.pendown ()
for x in range (1,1000,4):
     for z in range (4):
          turtle.forward (x+4)
          turtle.left(90)
#v2
import turtle
turtle.speed(0)
xcor=100
ycor=-100
size=8
step=4
for x in range (5):
     turtle.penup()
     turtle.goto(xcor,ycor)
     turtle.pendown ()
     for z in range (4):
          turtle.forward (size)
          turtle.right(90)
     xcor=xcor-step
     ycor=ycor+step
     size=size+step

     
#15
#v1
x=int(input("enter number: "))
print("##")
for c in range (x):
     print("#",end='')
     for z in range (c+1):
          print(" ",end='')
     print("#")
     
#v2
x=int(input("enter number: "))
for x in range (x):
     for c in range (x+2):
          if c==0 or c==x+1:
               print('#',end='')
          else:
               print(' ',end='')
     print()


#14
#v1 ok
n =8
#for r in reversed(range(n)): #диапазон  собратной последовательностью
for r in range(n,0,-1):
    for c in range(r):
        print('*', end='')
    print()
     
#v2 more undestand!!!
x=int(input("num row: "))
for r in range (x):
     for r in range (x,r,-1):
          print('*', end='')
     print()

#v3 не понятно как работает
x=int(input("num row: "))
for r in range(x):
     for x in range(x):
          print('*', end='')
     print()




#13
s=2
p=0.3
d=10
for x in range (d):
     
     print(x+1,format(s,'.5f'))
     s+=s*p


#12
f=1
n=int(input("enter factorial: "))
for x in range (1,n+1):
     f*=x
     print("factorial from:",x,"is",f)


#11

print("how you first weight: ", end='')
t=float(input())
for x in range(7):
     t-=1.5
     print("day: ",x+1,"weight",t)


#10
p=45000 #pay in year
percent=0.03
for x in range (5):
     p+=p*percent
     print(x+1,\
           format(p,'.2f'))

#9
rise=1.8
tmm=0

for year in range (25):
     tmm+=rise
     print("year:",year+1,"mm:",format(tmm,".1f"))

#8
t=0
x=0

while x>=0:
     x=float(input("enter nun: "))
     if x>0:
         t+=x 
     
print(format(t,'.2f'))

#7
#v1
t=1
d=int(input("day:"))
for x in range (d):
     if x==0:
          print("for day:","1",'0.01')
     else:
          t=t*2#для x-го дня m копейка/100
          print("for day:",x+1,t/100)
t+=t#накопление суммы

print('$',(t-1)/100,"days:",d, sep=' ')

#v2
d=0
m=1 #money in day
t=0

d=int(input("day:"))
for x in range (1,d+1):
     
     print(x,m/100)  #для x-го дня m копейка/100
     t+=m/100  #накопление суммы/100
     m*=2    #удваивание каждый день m=m(за предыдущий день)*2
  
print('$ ', format(t,'.2f'), 'for days',d)



#6
for c in range (21):
     f=9*c/5+32
     print(c, '\t',format(f,'.0f'))



#5
ys=int(input("years: "))
t=0
y=0
tm=0
for year in range (1,ys+1):
     print("for: ", year, "year")
     for m0 in range (12):
          print("for: ", m0+1, "mounth:",end='')
          m=float(input("rainfall: "))
          tm+=1
          t+=m
avarange_value_rainfall=float(t/tm)
print("mounth: ", tm, '\n',
     "sum rainfall: ", t, '\n',
     "avarange value rainfall: ", \
      format(avarange_value_rainfall,'.2f'))

#4

v=int(input("velocity: "))
h=int(float(input("hours: ")))
print ('hours \t distance')
print ('---------------------------------')
for x in range (1,h+1):
     s=x*v
     print(x,'\t',s)
#2
print ('Минуты \t калории')
print ('---------------------------------')
for m in range (10,31,5):
     c=m*4.2
     print (m ,'\t', c)

#3
m=int(input("for a mounth: "))
n='y'
t=0
while n=='y':
    c=float(input("costs: "))
    t+=c
    n=(input("next? y/n :"))
    
if t>m:
    print("overun:", t-m)
elif t<m:
    print("remainder:", m-t)
else:
    print("equal")
    

#1
t=0
for x in range(5):
     bug=int(input("bugs: "))
     t+=bug
print("total bugs: ", t)


