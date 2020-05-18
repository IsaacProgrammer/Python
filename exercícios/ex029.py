print('-' * 25)
print(f'{"Primeiro e Última":^25}')
print('-' * 25)
while True:
    frase = str(input('Gigite uma frase: ')).strip()
    confirm = frase.split()
    resp = ' '
    print(f'A Primeira palavra dessa frase é {confirm[0]}')
    print(f'A Última palavra dessa frase é {confirm[-1]}')
    while not resp in 'SN':
        resp = str(input('Quer Continuar: [ S / N ] ')).strip().upper()[0]
    if resp in 'N':
        break