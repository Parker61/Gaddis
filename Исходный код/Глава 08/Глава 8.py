
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-


# # Глава 8. Подробнее о строковых данных

# ## 8.1 Базовые строковые операции

# ### Программа 8-1 (count_Ts.py)

# In[1]:


# Эта программа подсчитывает количество появлений
# буквы T (в верхнем или нижнем регистре)
# в строковом значении.

def main():
    # Создать переменную, в котором будет храниться количество.
    # Переменная должна начинаться с 0.
    count = 0

   # Получить от пользователя строковое значение.
    my_string = input('Введите предложение: ')

    # Подсчитать буквы T.
    for ch in my_string:
        if ch == 'Т' or ch == 'т':
            count += 1

    # Напечатать результат.
    print('Буква Т появляется', count, 'раз(а).')

# Вызвать главную функцию.
main()


# ### Программа 8-2 (concatenate.py)

# In[10]:


# Эта программа конкатенирует строковые значения.

def main():
    name = 'Кармен'
    print('Имя', name)
    name = name + ' Браун'
    print('Теперь имя', name)

# Вызвать главную функцию.
main()


# ## 8.2 Получение среза строки

# ### Программа 8-3 (login.py)

# In[25]:


# Функция get_login_name принимает имя, фамилию и
# идентификационный номер в качестве аргументов.
# Она возвращает имя для входа в систему.

def get_login_name(first, last, idnumber):
    # Получить первые три буквы имени.
    # Если длина имени меньше 3 букв, то
    # срез вернет все имя целиком.
    set1 = first[0 : 3]

    # Получить первые три буквы фамилии.
    # Если длина фамилии меньше 3 букв, то
    # срез вернет всю фамилию целиком.
    set2 = last[0 : 3]

    # Получить последние три буквы фамилии идентификатора.
    # Если длина идентификатора меньше 3 символов, то
    # срез вернет весь идентификатор целиком.
    set3 = idnumber[-3 :]

    # Собрать воедино наборы символов.
    login_name = set1 + set2 + set3

    # Вернуть имя для входа в систему.
    return login_name


# ### Программа 8-4 (generate_login.py)

# In[27]:


# Эта программа получает имя и фамилию пользователя и 
# идентификационный номер студента. На основе этих данных
# она генерирует имя для входа в систему.

import login

def main():
    # Получить имя, фамилию и ИД номер пользователя.
    first = input('Введите свое имя: ')
    last = input('Введите свою фамилию: ')
    idnumber = input('Введите свой номер студента: ')

    # Получить имя для схода в систему.
    print('Ваше имя для входа в систему:')
    print(login.get_login_name(first, last, idnumber))

# Вызвать главную функцию.
main()


# ## 8.3 Проверка, поиск и манипуляция строковыми данными

# ### Программа 8-5 (string_test.py)

# In[30]:


# Эта программа демонстрирует несколько строковых методов проверки.

def main():
    # Получить от пользователя строковое значение.
    user_string = input('Введите строковое значение: ')

    print('Вот, что обнаружено в отношении введенного значения:')

    # Проанализировать строковое значение.
    if user_string.isalnum():
        print('Эта строка содержит буквы и цифры.')
    if user_string.isdigit():
        print('Эта строка содержит только цифры.')
    if user_string.isalpha():
        print('Эта строка содержит только буквы алфавита.')
    if user_string.isspace():
        print('Эта строка содержит только пробельные символы.')
    if user_string.islower():
        print('Все буквы в строке находятся в нижнем регистре.')
    if user_string.isupper():
        print('Все буквы в строке находятся в верхнем регистре.')

# Вызвать главную функцию.
main()


# ### Программа 8-6 (login2.py)

# In[31]:


# Функция get_login_name принимает имя, фамилию и
# идентийикационный номер в качестве аргументов.
# Она возвращает имя для входа в систему.

def get_login_name(first, last, idnumber):
    # Получить первые три буквы имени.
    # Если длина имени меньше 3 букв, то
    # срез вернет все имя целиком.
    set1 = first[0 : 3]

    # Получить первые три буквы фамилии.
    # Если длина фамилии меньше 3 букв, то
    # срез вернет всю фамилию целиком.
    set2 = last[0 : 3]

    # Получить последние три буквы фамилии идентификатора.
    # Если длина идентификатора меньше 3 символов, то
    # срез вернет весь идентификатор целиком.
    set3 = idnumber[-3 :]

    # Собрать воедино наборы символов.
    login_name = set1 + set2 + set3

    # Вернуть имя для входа в систему.
    return login_name

# Функция valid_password принимает пароль в 
# качестве аргумента и возвращает истину либо ложь,
# сообщая о его допустимости или недопустимости. Допустимый
# пароль должен быть как минимум 7 символов в длину,
# иметь как минимум один символ в верхнем регистре, 
# один символ в нижнем регистре и одну цифрую

def valid_password(password):
    # Назначить булевым переменным значение False.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Приступить к валидации
    # Начать с проверки длины пароля.
    if len(password) >= 7:
        correct_length = True

        # Проанализировать каждый символ и установить
        # соответствующий флаг, когда
        # требуемый символ найден.
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

        # Определить, удовлетворены ли все требования.
        # Если это так, то назначить is_valid значение True.
        # В противном случае назначить is_valid значение False.
        if correct_length and has_uppercase and             has_lowercase and has_digit:
            is_valid = True
        else:
            is_valid = False

        # Вернуть переменную is_valid.
        return is_valid


# ### Программа 8-7 (validate_password.py)

# In[32]:


# Эта программа получает от пользователя пароль и
# проверяет его допустимость.

import login

def main():
    # Получить от пользователя пароль.
    password = input('Введите свой пароль: ')

    # Проверить допустимость пароля.
    while not login.valid_password(password):
        print('Этот пароль недопустим.')
        password = input('Введите свой пароль: ')

    print('Это допустимый пароль.')

# Вызвать главную функцию.
main()


# ### Программа 8-8 (repetition_operator.py)

# In[35]:


# Эта программа демонстрирует оператор повторения.

def main():
    # Напечатать девять строк, увеличивающихся по длине.
    for count in range(1, 10):
        print('Z' * count)

    # Напечатать девять строк, уменьшающихся по длине.
    for count in range(8, 0, -1):
        print('Z' * count)

# Вызвать главную функцию.
main()


# ### Программа 8-9 (string_split.py)

# In[36]:


# Эта программа демонстрирует метод split.

def main():
    # Создать строковое значение с несколькими словами.
    my_string = 'Один два три четыре'

    # Разбить строковое значение.
    word_list = my_string.split()

    # Напечатать список слов.
    print(word_list)

# Вызвать главную функцию.
main()


# ### Программа 8-10 (split_date.py)

# In[1]:


# Эта программа вызывает метод split, используя
# символ '/' в качестве разделителя.

def main():
   # Создать строковое значение с датой.
   date_string = '01/12/2018'

   # Разбить дату.
   date_list = date_string.split('/')

   # Показать все части даты.
   print('День:', date_list[0])
   print('Месяц:', date_list[1])
   print('Год:', date_list[2])

# Вызвать главную функцию.
main()

