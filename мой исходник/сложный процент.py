
# Будущая стоимость

# Главная функция
def main():

    # Локальные переменные для вводимых пользователем значений
    presentValue = 0.0
    interestRate = 0.0
    months = 0
    futureValue = 0.0

    # Получить от пользователя конкретные значения
    presentValue = float(input('Введите текущую сумму ' \
                               'на счету в долларах: '))
    
    day_interestRate = float(input('Введите ежедневную процентную ' \
                               'ставку: '))
    interestRate=day_interestRate*30
        
    months = int(input('Введите количество месяцев: '))
    
    # Получить ожидаемую будущую сумму на счету 
    futureValue = getFutureValue(presentValue, interestRate, months)

    print ('Информация по Вашему счету следующая:')
    print('Текущая сумма: $', format(presentValue, ',.2f'), sep='')
    print('Процентная ставка: %', format(interestRate, '.2f'), sep='')
    print('После ', months, \
          ' месяцев, сумма на счету составит $', \
          format(futureValue, '.2f'), sep='')

# Функция getFutureValue получает текущую сумму, процентную  
# ставку и количество месяцев, в течение которых деньги будут 
# оставаться на счету, и возвращает будущую сумму на счету. 
def getFutureValue(P, interest, t):
    # Определить локальную переменную
    F = 0.0
    i = interest / 100 # написать процент как дробь
    F = P * ((1 + i) **t)
    return F

# Вызвать главную функцию.
main()
