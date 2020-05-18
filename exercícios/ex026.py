print('=' * 28)
print(f'{"Fatorial":^28}')
print('=' * 28)
f = 1
while True:
    try:
        number = int(input('Qual o número para calcular fatorial: '))
    except:
        print('[ ERROR ] Try Again')
    else:
        print('=' * 28)
        for c in range(number, 0, -1):
            f *= c
        print(f'O fatorial de {number} é {f}')
        print('=' * 28)