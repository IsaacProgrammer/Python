from random import randint
from time import sleep
print('-' * 50)
print(f'{"Jogo Par ou Ímpar":^50}')
print('-' * 50)
computador = randint(0, 100)
while True:
    n = int(input('Informe um número: '))
    resp = ' '
    while not resp in 'PI':
        resp = str(input('Par ou Ímpar? [ P / I ] ')).strip().upper()[0]
    soma = n + computador
    print('-' * 50)
    print(f'Você digitou o número {n} e o computador escolheu {computador}\nA soma disto deu {soma}')
    print('-' * 50)
    sleep(1.5)
    if soma % 2 == 0 and resp in 'P':
        print('Parabéns você Ganhou!')
    elif soma % 2 == 0 and resp in 'I':
        print('Infelizmente você perdeu')
    elif soma % 2 == 1 and resp in 'P':
        print('Infelismente você perdeu')
    elif soma % 2 == 1 and resp in 'I':
        print('Parabéns você Ganhou!')
    print('-' * 50)
    print('Vamos Jogar Novamente!')
    print('-' * 50)

