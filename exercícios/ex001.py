from time import sleep
print('-' * 30)
print(f'{"Conversor P/ Metros"}')
print('-' * 30)
while True:
    metros = float(input('Quantos metros: '))
    print('-' * 30)
    resp = int(input(f'Quer converter {metros:.2f}M para\n\n[ 1 ] Quilômetros\n[ 2 ] Hectametros\n[ 3 ] Decâmetros\n[ 4 ] Decímetros\n[ 5 ] Centímetros\n[ 6 ] Milímetros\n[ '))
    sleep(1.5)
    print('-' * 30)
    if resp == 1:
        km = metros * 1000
        print(f'Em Quilômetros temos {km:.2f}Km')
    elif resp == 2:
        hec = metros * 100
        print(f'Em Hectómetros temos {hec:.2f}Hm')
    elif resp == 3:
        dam = metros * 10
        print(f'Em Decâmetros temos {dam:.2f}Dam')
    elif resp == 4:
        dm = metros / 10
        print(f'Em Decímetros temos {dm:.2f}Dm')
    elif resp == 5:
        cm = metros / 100
        print(f'Em Centímetros temos {cm:.2f}Cm')
    elif resp == 6:
        mm = metros / 1000
        print(f'Em Milímetros temos {mm:.2f}Mm')
    else:
        print('Informação Errada. Tente Novamente!')
    print('-' * 30)