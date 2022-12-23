# Эта программа определяет, удовлетворяет ли 
# клиент требованиям банка на получение ссуды.

MIN_SALARY = 30000.0 # Минимально допустимая годовая зарплата
MIN_YEARS = 2        # Минимально допустимый стаж на текущем месте работы

# Получить размер годовой заработной платы клиента.
salary = float(input('Введите свой годовой оклад: '))

# Получить количество лет на текущем месте работы.
years_on_job = int(input('Введите количество лет' +
                         'рабочего стажа: '))

# Определить, удовлетворяет ли клиент требованиям.
if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print('Вы прошли квалификацию на получение ссуды.')
else:
    print('Вы не прошли квалификацию на получение этой ссуды.')