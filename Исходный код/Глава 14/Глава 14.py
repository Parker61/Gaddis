
# coding: utf-8

# In[24]:


# -*- coding: utf-8 -*-


# # Глава 14. Основы функционального программирования

# ## 14.2 Оператор lambda, функции map, filter, reduce и другие

# In[25]:


def standard_function(x, y):
    return x + y


# In[26]:


lambda x, y: x + y


# In[27]:


(lambda x, y: x+y)(5, 7)


# In[28]:


lambda_function = lambda x, y: x + y


# In[29]:


lambda_function(5,7)


# In[30]:


func = lambda_function


# In[31]:


func(3,4)


# In[33]:


dic = {'функция1': lambda_function}


# In[34]:


dic['функция1'](7,8)


# In[35]:


seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)
seq2 = (5, 6, 7, 8, 9, 0, 3, 2, 1)
result = map(func, seq, seq2)
result


# In[36]:


list(result)


# In[38]:


is_even = lambda x: x % 2 == 0


# In[39]:


seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)
filtered = filter(is_even, seq)
list(filtered)


# In[41]:


filtered = filter(lambda x: x % 2 == 0, seq)
list(filtered)


# In[42]:


def reduce(fn, seq, initializer=None):
    it = iter(seq)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = fn(value, element)
    return value


# In[43]:


seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)
get_sum = lambda a, b: a + b
summed_numbers = reduce(get_sum, seq)
summed_numbers


# In[45]:


sentences = ["Варкалось.", 
             "Хливкие шорьки пырялись по наве, и", 
             "хрюкотали зелюки, как мюмзики в мове."]
wsum = lambda aсс, sentence: aсс + len(sentence.split())
number_of_words = reduce(wsum, sentences, 0)
number_of_words


# In[46]:


x = 'абв'
y = 'эюя'
zipped = zip(x, y)
list(zipped)


# In[51]:


x2, y2 = zip(*zip(x, y))
x2


# In[52]:


y2


# In[49]:


x == ''.join(x2) and y == ''.join(y2)


# In[4]:


lazy = enumerate(['а','б','в'])
list(lazy)


# In[54]:


convert = lambda x: x[1].upper()+str(x[0])
list(map(convert, enumerate(['а','б','в'])))


# ## 14.3 Включение в последовательность

# In[55]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = [x*x for x in numbers]
squared_numbers


# In[56]:


squared_numbers = []
for x in numbers:
    squared_numbers.append(x*x)
squared_numbers


# In[57]:


seq = (1, 2, 3, 4, 5, 6, 7, 8, 9)
seq2 = (5, 6, 7, 8, 9, 0, 3, 2, 1)
result = [x+y for x,y in zip(seq, seq2)]
result


# In[58]:


result = [x for x in seq if is_even(x)]
result


# ## 14.4 Замыкание

# In[78]:


def adder(n, m):
    return n + m


# In[79]:


def adder(n):
    def fn(m):
        return n + m
    return fn


# In[59]:


adder = lambda n: lambda m: n + m


# In[60]:


sum_three = adder(3)
sum_three


# In[61]:


sum_three(1) 


# In[63]:


def power_generator(base):
    return lambda x: pow(x, base)


# In[64]:


square = power_generator(2)  # функция возведения в квадрат
square(2)


# In[65]:


cube = power_generator(3)    # функция возведения в куб
cube(2)


# In[66]:


COUNT = 0
def count_add(x):
    global COUNT
    COUNT += x
    return COUNT


# In[80]:


def make_adder():
    n = 0    
    def fn(x):
        nonlocal n
        n += x
        return n
    return fn


# In[81]:


my_adder = make_adder()
print(my_adder(5))     # напечатает 5
print(my_adder(2))     # напечатает 7 (5 + 2)
print(my_adder(3))     # напечатает 10 (5 + 2 + 3)


# ## 14.5 Функциональное ядро программы на основе конвейера

# In[69]:


# Конвейер обработки данных

def pipe(data, *fseq):
    for fn in fseq: 
        data = fn(data)
    return data


# In[2]:


pipe(2,
     lambda x: x + 5,
     lambda x: x * x,
     lambda x: str(x))


# ### Программа 14.1 (factorial_functional.py)

# In[3]:


# Эта программа демонстрирует 
# функциональную версию функции factorial из главы 12

def pipe(data, *fseq):
    for fn in fseq: 
        data = fn(data)
    return data

def reduce(fn, seq, initializer=None):
    it = iter(seq)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = fn(value, element)
    return value

def main():
    # Конвейер (функциональное ядро c нерекурсивным алгоритмом факториала)
    pipe(int(input('Введите неотрицательное целое число: ')),    
         lambda n: (n, reduce(lambda x, y: x * y, range(1, n + 1))),    
         lambda tup: 
             print(f'Факториал числа {tup[0]} равняется {tup[1]}'))        

# Вызвать главную функцию
main()


# ### Программа 14.2 (factorial_functional2.py)

# In[82]:


# Эта программа демонстрирует 
# функциональную версию функции factorial из главы 12

def pipe(data, *fseq):
    for fn in fseq: 
        data = fn(data)
    return data

def reduce(fn, seq, initializer=None):
    it = iter(seq)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = fn(value, element)
    return value

def get_int(msg=''):
    return int(input(msg))

def main():
    # Алгоритм 1. Рекурсивная версия с хвостовой рекурсией
    def factorial_rec(n): 
        fn = lambda n, acc=1: acc if n == 0 else fn(n - 1, acc * n)
        return n, fn(n) 
    
    # Алгоритм 2. Нерекурсивная версия
    def factorial(n):  
        return n, reduce(lambda x, y: x * y, range(1, n + 1)) 
    
    # Ввод данных
    def indata():
        def validate(n):  # Валидация входных данных
            if not isinstance(n, int):
                raise TypeError("Число должно быть целым.")
            if not n >= 0:
                raise ValueError("Число должно быть >= 0.")
            return n        
        msg = 'Введите неотрицательное целое число: '
        return pipe(get_int(msg), validate)
    
    # Вывод данных
    def outdata():
        def fn(data):
            n, fact = data
            print(f'Факториал числа {n} равняется {fact}') 
        return fn
 
    # Конвейер (функциональное ядро)
    pipe(indata(),     # вход: -       выход: int
         factorial,    # вход: int     выход: кортеж
         outdata())    # вход: кортеж  выход: -
    
# Вызвать главную функцию
main()


# ### Программа 14.3 (fibonacci_functional.py)

# In[75]:


# Эта программа демонстрирует 
# функциональную версию функции fibonacci из главы 12

def pipe(data, *fseq):
    for fn in fseq: 
        data = fn(data)
    return data

def reduce(fn, seq, initializer=None):
    it = iter(seq)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = fn(value, element)
    return value

def main():
    # Алгоритм
    def fibonacci(n, x=0, y=1):
        # Функция fib возвращает n-ое число последовательности.
        fib = lambda n, x=0, y=1: x if n <= 0 else fib(n - 1, y, x + y)
        # Функция reduce собирает результаты в список acc
        acc = []
        reduce(lambda _, y: acc.append(fib(y)), range(n + 1))
        return n, acc
    
    # Валидация входных данных
    def validate(n):         
        if not isinstance(n, int):
            raise TypeError("Число должно быть целым.")
        if not n >= 0:
            raise ValueError("Число должно быть ноль положитель-ным.")
        if n > 10:
            raise ValueError("Число должно быть не больше 10.")
        return n
    
    # Ввод данных
    def indata():
        msg = 'Введите неотрицательное целое число не больше 10: '
        return pipe(get_int(msg), validate)
    
    # Вывод данных
    def outdata():
        def fn(data):
            n, seq = data
            msg = f'Первые {n} чисел последовательности Фибоначчи:'
            print(msg) 
            [print(el) for el in seq]
        return fn

    # Конвейер (функциональное ядро)
    pipe(indata(), fibonacci, outdata()) 

# Вызвать главную функцию.
main()


# ### Программа 14.4 (range_sum_functional.py)

# In[76]:


# Эта программа демонстрирует 
# функциональную версию функции range_sum из главы 12

def pipe(data, *fseq):
    for fn in fseq: 
        data = fn(data)
    return data

def main():
    # Алгоритм
    def range_sum(data):  
        seq, params = data
        fn = lambda start, end: 0 if start > end                                   else seq[start] + fn(start + 1, end)
        return fn(*params)

    # Ввод данных
    def indata():
        seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]    
        params = (2,5)   # params - это параметры start, end
        return seq, params  
    
    # Вывод данных
    def outdata():
        def f(data):
            msg = 'Сумма значений со 2 по 5 позиции равняется '
            print(msg, format(data), sep='') 
        return f
    
    # Конвейер (функциональное ядро)
    pipe(indata(), range_sum, outdata()) 

# Вызвать главную функцию.
main()

