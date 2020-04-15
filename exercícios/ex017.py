from random import randint
from time import sleep
print('-' * 50)
print(f'{"Jogo Dois ou Um":^50}')
print('-' * 50)
print('Jogo Dois ou Um...Quem colocar um número diferente dos outros dois, Ganha!!!\n\nVocê joga com mais dois jogadores')
print('-' * 50)
sleep(1)
p1 = p2 = p3 = 0
while True:
    print(f'{"PONTOS":^50}')
    print('-' * 50)
    print(f'Jogador 1: {p1}')
    print(f'Jogador 2: {p2}')
    print(f'Jogador 3: {p3}')
    print('-' * 50)
    j1 = 0
    while j1 < 1 or j1 > 2:
        j1 = int(input('Jogador 1: Dois ou Um: '))
    print('Jogador 2: Dois ou Um:', end=' ')
    sleep(1)
    j2 = randint(1, 2)
    print(j2)
    print('Jogador 3: Dois ou Um:', end=' ')
    sleep(1)
    j3 = randint(1, 2)
    print(j3)
    print('-' * 50)
    if j1 != j2 and j1 != j3:
        if j2 == j3:
            print('Empate entre o Jogador 2 e Jogador 3')
            print('-' * 50)
        print('Jogador 1: Ganhou!!!')
        p1 += 2
    elif j2 != j1 and j2 != j3:
        if j1 == j3:
            print('Empate entre o Jogador 1 e Jogador 3')
        print('-' * 50)
        print('Jogador 2: Ganhou!!!')
        p2 += 2
    elif j3 != j1 and j3 != j2:
        if j1 == j2:
            print('Empate entre o Jogador 1 e Jogador 2')
            print('-' * 50)
        print('Jogador 3: Ganhou!!!')
        p3 += 2
    elif j1 == j2 and j2 == j3:
        print('ENPATE')
        p1 += 1
        p2 += 1
        p3 += 1
    elif j1 == j2:
        print('Empate entre Jogador 1 e Jogador 2')
        print('Mas, o Jogador 3 ganhou!!!')
    print('-' * 50) 