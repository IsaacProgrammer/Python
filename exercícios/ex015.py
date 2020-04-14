from time import sleep
from random import randint
lista = ['PE', 'PA', 'TE']
print('-' * 50)
print(f'{"Pedra, Papel, Tesoura":^50}')
print('-' * 50)
print('Vamos jogar: Pedra, Papel, Tesoura???')
print('-' * 50)
print('As Informações:\nInforme PE para Pedra - PA para Papel - TE para Tesoura\nSe você vencer ganhará um ponto, mas se perder não ganha\nO Computador jogará com você')
print('-' * 50)
sleep(2)
p1 = p2 = 0
while True:
    print(f'{"Você {} Vs  {} Computador":^50}'.format(p1, p2))
    print('-' * 50)
    jogador = ' '
    while not jogador in 'PEPATE':
        jogador = str(input('[ PE ] Pedra - [ PA ] Papel - [ TE ] Tesoura- [ ')).strip().upper()[0:2]
    print('-' * 50)
    sor = randint(0, 2)
    computador = lista[sor]
    print(computador)
    if computador in 'PE':
        if jogador in 'PE':
            print(f'Você escolheu: Pedra\nO Computador Escolheu: Pedra')
            print('-' * 50)
            print('[ EMPATE ]')
        elif jogador in 'PA':
            print(f'Você escolheu: Papel\nO Computador Escolheu: Pedra')
            print('-' * 50)
            print('[ Você Venceu ]')
            p1 += 1
        elif jogador in 'TE':
            print(f'Você escolheu: Tesoura\nO Computador Escolheu: Pedra')
            print('-' * 50)
            print('[ Você Perdeu ]')
            p2 += 1
    elif computador in 'PA':
        if jogador in 'PE':
            print(f'Você escolheu: Pedra\nO Computador Escolheu: Papel')
            print('-' * 50)
            print('[ Você Perdeu ]')
            p2 += 1
        elif jogador in 'PA':
            print(f'Você escolheu: Papel\nO Computador Escolheu: Papel')
            print('-' * 50)
            print('[ EMPATE ]')
        elif jogador in 'TE':
            print(f'Você escolheu: Tesoura\nO Computador Escolheu: Papel')
            print('-' * 50)
            print('[ Você Venceu ]')
            p1 += 1 
    elif computador in 'TE':
        if jogador in 'PE':
            print(f'Você escolheu: Pedra\nO Computador Escolheu: Tesoura')
            print('-' * 50)
            print('[ Você Venceu ]')
            p1 += 1
        elif jogador in 'PA':
            print(f'Você escolehu: Papel\nO Computador Escolheu: Tesoura')
            print('-' * 50)
            print('[ Você Perdeu ]')
            p2 += 1
        elif jogador in 'TE':
            print(f'Você ecolheu: Tesoura\nO Computador Escolheu: Tesoura')
            print('-' * 50)
            print('[ EMPATE ]')
    sleep(1)
    print('-' * 50)
    
