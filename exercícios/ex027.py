print('=' * 25)
print(f'{"Tabuada v2.0":^25}')
print('=' * 25)
while True:
    try:
        number = int(input('Informe um número para ver sua tabuada: '))
    except:
        print('[ ERROR ] Try Again')
    else:
        if number >= 1:
            for c in range(1, 11):
                print(f'{number} x {c} = {number * c}')
            print('=' * 25)
        else:
            print('Tabuada Encerrada...Obrigado!')
            break