# Определение главной функции.
def main():
    get_name()
    print('Привет,', name) # Это вызовет ошибку!

# Определение функции get_name.
def get_name():
    name = input('Введите свое имя: ')

# Вызвать функцию main.
main()