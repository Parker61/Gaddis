# Следующее используется в качестве глобальной константы
# Ставка взноса компании.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Введите заработную плату: '))
    bonus = float(input('Введите сумму премий: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# Функция show_pay_contrib принимает заработную
# плату в качестве аргумента и показывает взнос
# в пенсионные накопления исходя из этого размера оплаты.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Взнос исходя из заработной платы: $',
          format(contrib, ',.2f'),
          sep='')

# Функция show_bonus_contrib принимает сумму премий
# в качестве аргумента и показывает взнос в
# пенсионное накопление исходя из этой суммы оплаты.
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print('Взнос исходя из суммы премий: $',
          format(contrib, ',.2f'),
          sep='')

# Вызвать функцию main.
main()