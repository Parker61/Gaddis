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