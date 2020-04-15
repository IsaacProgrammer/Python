from time import sleep
from random import randint
print('-' * 50)
print(f'{"Jogo da Adivinhação":^50}')
print('-' * 50)
print('Pensei um número entre 0 e 50...\nConsegui Adivinhar???')
print('-' * 50)
sleep(1)
c = randint(0, 50)
while True:
    n = int(input('Em qual número eu pensei: '))
    if n == c:
        break
    elif n > c:
        print('Eitaa...Menor')
    elif n < c:
        print('Eitaa...Maior')
    print('-' * 50)
print('-' * 50)
print('Você acertou, Pensei nesse número mesmo')
print('Obrigado por jogar!!!')
