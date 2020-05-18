print('-' * 25)
print(f'{"Convertendo Horas":^25}')
print('-' * 25)
while True:
    try:
        horas = int(input('Quantas horas você quer converter: '))
    except:
        print('[ Try Again ] ')
    else:
        print('-' * 25)
        try:
            confirm = int(input('[ 1 ] Minutos\n[ 2 ] Segundos\n[ '))
        except:
            print('[ Try Again ]')
        else:
            if confirm == 1:
                print(f'Em Minutos, {horas}h são {horas * 60}m')
            elif confirm == 2:
                print(f'Em Segundos, {horas}h são {horas * 3600}s')
            else:
                print('Try Again')
            resp = ' '
            while not resp in 'SN':
                resp = str(input('Quer Continuar: ')).strip().upper()[0]
            if resp in 'N':
                break