from time import sleep
print('-' * 50)
print(f'{"Contador de Pares"}')
print('-' * 50)
n = int(input('Quer contar até onde? '))
print('-' * 50)
totp = totsoma = 0
for c in range(0, n):
    if c % 2 == 0:
        totp += 1
        totsoma += c
    print(c, end=' ')
print()
print(f'Os {c} números selecionados, só os pares são {totp} a soma desses é {totsoma}')