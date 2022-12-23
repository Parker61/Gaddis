# Эта программа имитирует 10 бросков монеты.
import random

# Константы
HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        # Имитировать бросание монеты.
        if random.randint(HEADS, TAILS) == HEADS:
            print('Орел')
        else:
            print('Решка')

# Вызвать функцию main.
main()