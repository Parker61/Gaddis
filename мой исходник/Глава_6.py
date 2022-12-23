####### 12 v1
def main():
    jun=31
    feb=jun+28
    mar=feb+31
    apr=mar+30
    x=open('steps.txt','r')

    sj=int(func(jun)/31)
    sf=int((func(feb)-func(jun))/28)
    sm=int((func(mar)-func(feb))/31)
    sa=int((func(apr)-func(mar))/30)
    print("sj",sj,sf,sm,sa)
    
def func(m):
    s=0
    d=0
    x=open('steps.txt','r')
    for i in range(m):        
        f=x.readline()
        f=f.rstrip('\n')
        f=int(f)
        s+=f
        d+=1
        #print(f,d)
        sm=s/d
    #print("mouth",s,'sm',sm)
    return s
main()


###### 12 v2
def main():
    jun=31
    feb=28
    mar=31
    x=open('steps.txt','r')
    fun(x,'jun',jun)
    fun(x,'feb',feb)
    fun(x,'mar',mar)

def fun(x,n,m):
    sum=0
    for i in range(m):
        sum+=int(x.readline())
    mid=int(sum/m)       
    print(n,"mid",mid)
main()


#########10
def main():
     try:             
         #x=open(r'c:\golf.txt','a')
         x=open('golf.txt','a')
         again='y'
         while again=='y' or again=='Y':
             again=input("if yes: 'y'")
             if again=='y' or again=='Y':
                 y=x.write(input("gamer:")+'\n')
                 y=x.write(str(input("score:"))+'\n')

         x=open('golf.txt','r')
         n=x.readline()
         s=x.readline()
         while n!='' or s!='':
             n=n.rstrip('\n')
             s=s.rstrip('\n')
             print('gamer: ',n)
             print('score: ',s)
             print()
             n=x.readline()
             s=x.readline()                 
     except ValueError:
          print("Error value, again try")
     except IOError:
          print("not file")
     except :
          print("unknown Error")
main()

#9
def main():
     try:
          t=0
          n=0
          y= open(r'c:\Users\Павел\num.txt','r') 
          for x in y:
               x=int(x)
               t+=1
               n+=x
          print("mean: ",int(n/t))
          y.close()
     except ValueError:
          print("Error value, again try")
     except IOError:
          print("not file")
     except :
          print("unknown Error")
main()

#8
def main():
     t=0
     z=0
     x=open(r'C:\Users\Павел\num.txt','r')
     y=x.readline()
     while y!='':
           y=int(y)
           t+=1
           print(t,y)
           z+=y
           y=x.readline()
     print("N:",t, "sum:",z)
     x.close()
main()
#####8 v3
def main():
     li=[]
     x=open(r'c:\Users\Павел\num.txt','r')
     li=x.readlines()
     
     for i in range(len(li)):
         li[i]=li[i].rstrip('\n')
         li[i]=int(li[i])
         print("N:",i+1, "num:",li[i])
         
     print('SUM',sum(li))
     x.close()
main()
#v2
def main():
     t=0
     z=0
     x=open(r'C:\Users\Павел\num.txt','r')
     for y in x:
           y=int(y)
           t+=1
           print(t,y)
           z+=y
     print("N:",t, "sum:",z)
     x.close()
main()

#7
import random
def main():
     li=[]
     x=open(r'c:\Users\Павел\num.txt','w')
     y=int(input("num: "))
     for z in range (y):
          n=random.randint(1,500)
          x.write(str(n)+'\n')
          print(n)

     x=open(r'c:\Users\Павел\num.txt','r')
     li=x.readlines()
     for i in range(len(li)):
         li[i]=li[i].rstrip('\n')
     print(li)
     x.close()
main()

#6
def main():
     t=0
     n=0
     y= open(r'C:\Users\Павел\Desktop\Гэддис дополнение\Решения задач по программированию\Глава 06\data\numbers.txt', 'r') #?????
     for x in y:
          x=float(x)
          t+=1
          n+=x
     print("mean: ",n/t)
     y.close()
main()

#6
#v2
def main():
     t=0
     t1=0
     y= open(r'C:\Users\Павел\Desktop\Гэддис дополнение\Решения задач по программированию\Глава 06\data\numbers.txt', 'r') #?????
     x=y.readline()
     while x!='':
          x=float(x)
          t+=x
          t1+=1
          x=y.readline()
     print("sum: ",t/t1)
     y.close()
main()


#5
#v2
def main():
     t=0
     y= open(r'C:\Users\Павел\Desktop\Гэддис дополнение\Решения задач по программированию\Глава 06\data\numbers.txt', 'r') #?????
     x=y.readline()
     while x!='':
          x=float(x)
          t+=x
          x=y.readline()
     print("sum: ",t)
     y.close()
main()
#v1
def main():
     t=0
     y= open(r'C:\Users\Павел\Desktop\Гэддис дополнение\Решения задач по программированию\Глава 06\data\numbers.txt', 'r') #?????
     for x in y:          
          x=float(x)
          print(x)
          t+=x
     print("sum: ",t)
     y.close()
main()

#4
def main():
     t=0
     y= open(r'C:\Users\Павел\Desktop\Гэддис дополнение\Решения задач по программированию\Глава 06\data\names.txt', 'r') #?????
     x1=y.readlines()
     print("scan names: ",(len(x1)))
     y= open(r'C:\Users\Павел\Desktop\Гэддис дополнение\Решения задач по программированию\Глава 06\data\names.txt', 'r') #?????
     x=y.readline()
     while x!='':
          t+=1
          x=y.readline()
     print("scan names: ",t)
     y.close()
main()

#3
def main():
     t=0
     x=input("file: ")
     y=open(r'c:\Users\Павел\\'+x,'r')
     z=y.readline()
     while z!='':
          z=z.rstrip('\n')
          t+=1
          print(t,":",z,sep='')
          z=y.readline()
     y.close()
main()

#1
def main():
     n=open(r'c:\Users\Павел\numbers.txt','r')
     n1=n.read()
     print(n1)     
     n.close()
main()


#2
#v1
def main():
     #x=input("name file: ")
     t=1
     y=open(r'c:\Users\Павел\num.txt','r')
     #y=open("data\\"+ x,'r') ????
     a=y.readline()
     while a!='' and t<=5:
          a=a.rstrip('\n')
          t+=1
          print(a)
          a=y.readline()
     y.close()
main() 
#2
#v2
def main():
     y=open(r'c:\Users\Павел\num.txt','r')
     for z in range(10):
          a=y.readline()
          #z=int(z)
          a=a.rstrip('\n')
          if a!='':
             print(a)
     y.close()
main() 
