#### FIBO
def main():
    n=int(input('num: '))
    f=fib(n)
    print(f'fibo from {n} is {f}')
    for i in range(1,n+1):
        print(fib(i))
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
main()
#########  8
def main():
    m=2
    n=0
    f=akker(m,n)
    print(f)
def akker(m,n):
    if m==0:
        return n+1
    if n==0:
        return akker (m-1,1)
    else:
        return akker (m-1,akker(m,n-1))
main()

######  7
def main():
    x=3
    n=4
    print(x**n)
    w=f(x,n)
    print(w)
def f(x,n):
    if n==0:  #n==1  #можно и так
        return 1  #return x
    else:
        return x*f(x, n-1)
main()

######  6
def main():
    n=25
    x=f(n)
    print(x)
def f(n):
    if n==0: #n==1    #можно и так
        return 0 # return 1
    else:
        return n+f(n-1)
main()

#### 5 v2
def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x=f(list)
    print('x',x)
def f(list):
    n=len(list)
    if n==1:
        return list[0]
    else:
        return list[n-1]+f(list[0:n-1])  #второе слагаемое просто отбрасывется и поочередно перебор с конца
main()

######## 5 v1
def main():
    list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_sum=range_sum(list,0,len(list)-1)
    print('list: ',list)
    print('my_sum: ',my_sum)
def range_sum(list,start,end):
    if start>end:
        return 0
    else:
        return list[start] + range_sum(list,start+1,end)
main()

##########  4 вообще не понял?????????
def main():
    number_list = [11, 2, 12, 4, 5, 6, 33, 8, 3, 10]
    x=number_list[0:1]         #в качестве примера дале после рекурсии
    print('num ',number_list[0:1],x)

    print('Список чисел:\n', number_list, sep='')

    print('Максимальное число в списке: ', find_largest(number_list))

def find_largest(numlist):
    n  = len(numlist)
    print('len(numlist)',len(numlist))
    if n == 1:  #делаем рекурсию до n==1
        print('numlist[0]: ',numlist[0])
        return numlist[0]
    else:
        temp = find_largest(numlist[0:n-1]) #делаем рекурсию до n==2 тогда [0:2-1=1]
        print('temp',temp)
        #find_largest(numlist[0:n - 1])
        #print('find_largest(numlist[0:n-1]): ',find_largest(numlist[0:n-1]),'numlist[0:n-1]',numlist[0:n-1])
        if numlist[n-1] > temp:  #сравниваем последующее значение с предыдущим
            print('ttt')
            return numlist[n-1]
        else:
            print('pppp')
            return temp
main()


########  3v1
def main():
    n=3
    f(n)
def f(n):
    #print('*'*(n-1)) #печать наоборот с n-1 до 1 *
    if n>0:
        f(n-1)
        print('*'*n) #начинается вызов с конца с 1 и до n

main()

##### 3 v2
def main():
    n=3
    f(n)
def f(n):
    if n>1:
        f(n-1)
    for i in range(n):
        print('*',end='')
    print()
main()

##########  2
def main():
    x=1
    y=3
    s=f(x,y)
    print('s',s)
def f(x,y):
    if x==0 or y==0:
        return 0
    else:
        return y+f(x-1,y) #возврат пока Х не будет равен 0
main()

########### 1 v3
def main():
    n = int(input('Сколько показать чисел? '))
    for i in range(1, n + 1): #решение рекурсии через цикл
        print(i)

    i = [i for i in range(1, n + 1)]  # генератор списка
    print(i)
main()


############ 1 v2
def main():
 number = int(input('Сколько показать чисел? '))
 num(number)

def num(n):
    print('n start: ',n) #печать от 5 с постепенным уменьшением на n - 1 до 1
    if n > 1:
        #print('before n-1: ', n - 1)
        num(n - 1)
        #print('n-1: ', n - 1)
    print ('n: ',n, sep=' ') #  обратный возврат функции по рекурсии печать от 1 до 5
main()

 #############  1 v1
def main():
    t=1 # печать с ....
    n=5 #задать кол-во чисел
    pr(n,t)

def pr(n,t):
    if t<=n:
        print(t)
        pr(n,t+1)

main()