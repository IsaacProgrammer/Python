from time import sleep
print('-' * 50)
print(f'{"Preenchendo Matriz":^50}')
print('-' * 50)
tot = totp = somap = toti = somai = dp = somadp = 0
vet = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        vet[l][c] = int(input(f'Digite um número para a posição [{l}, {c}]: '))
sleep(1.5)
print('-' * 50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {vet[l][c]:2} ]', end=' ')
        if vet[l][c] % 2 == 0:
            totp += 1
            somap += vet[l][c]
        else:
            toti += 1
            somai += vet[l][c]
        if l == c:
            somadp += vet[l][c]
        tot += vet[l][c]
    print()
sleep(1)
print('-' * 50)
print(f'Foram digitados {totp} números pares, que dá o total de {somap}')
print(f'Foram digitados {toti} números ímpares, que dá o total de {somai}')
print(f'Foram Digitados {somadp} na diagonal principal')
print(f'Ao todo tem {tot} números')

