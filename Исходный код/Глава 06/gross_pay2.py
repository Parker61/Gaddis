# Эта программа вычисляет заработную плату до удержаний.

def main():
    try:
        # Получить количество отработанных часов.
        hours = int(input('Сколько часов вы отработали? '))

        # Получить почасовую ставку оплаты труда.
        pay_rate = float(input('Введите свою почасовую ставку: '))

        # Вычислить заработную плату до удержаний.
        gross_pay = hours * pay_rate

        # Показать заработную плату.
        print('Зарплата: $', format(gross_pay, ',.2f'), sep='')
    except ValueError:
        print('ОШИБКА: Отработанные часы и почасовая ставка оплаты')
        print('должны быть допустимыми числами.')

# Вызвать главную функцию.
main()