# Importações para o programa

from time import sleep
from random import randint

# funções para fazer o cabeçalho


def line(t=100):
    return '=' * t


def header(msg):
    print(line())
    print(f'{msg:^100}')
    print(line())


def menu(lst):
    c = 1
    for item in lst:
        print(f'{c}° {item}')
        c += 1
    print(line())
    option = number('Option: ')
    return option


def number(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('[ Try Again ] Just Numbers ')
        else:
            return n
            break


# Começando a fazer a seleção do jogos


header('GAME SELECTION')

while True:
    option = menu(['Jogo da Adivinhação', 'Jogo da Advinhação v2.0', 'Quit'])
    print('Verifying...')
    sleep(1.5)
    if option == 1:
        header('Welcome to Game of divination')
        print(f'Eu pensei em um número de 0 á 100...\nVocê só tem uma chance. Consegue Adivinhar???')
        sleep(2)
        print("Let's go!")
        print(line())
        computer = randint(0, 100)
        option = number('Qual o seu palpite: ')
        print('Vamos Verificar se você acertou... ')
        sleep(2)
        print(line())
        if option == computer:
            print('Parabéns. Você Acertou!')
        else:
            print(f'Você errou! A resposta certa era {computer}')
        sleep(5)
    elif option == 2:
        header('Welcome to Game of Divination v2.0')
        print('Eu peisei em um número de 0 á 500...\nVocê consegue acertar???')
        sleep(2)
        print("Let's go!")
        print(line())
        computer = randint(0, 500)
        p = 0
        while True:
            option = number('Qual é o seu palpite: ')
            sleep(2)
            p += 1
            if option > computer:
                print("[ Try again ] Informe um número Menor...")
            elif option < computer:
                print('[ Try Again ] Inform um número Maior...')
            else:
                break
        print(line())
        print('Parabéns! Você acertou!')
    elif option == 3:
        header('Exiting')
        sleep(5)
        break
    print(line())
