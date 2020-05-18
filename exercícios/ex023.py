from math import sqrt
print('=' * 30)
print(f'{"Dobro, Triplo, Raiz Quadrada":^25}')
print('=' * 30)
while True:
    try:
        number = int(input('Número: '))
    except:
        print('[ ERROR ] Try Again')
    else:
        confirm = 0
        while confirm > 3 or confirm < 1:
            confirm = int(input('[ 1 ] Dobro\n[ 2 ] Triplo\n[ 3 ] Raiz Quadrada\n[ '))
        if confirm == 1:
            print(f'O Dobro de {number} é {number * 2}')
        elif confirm == 2:
            print(f'O Dobro de {number} é {number * 3}')
        elif confirm == 3:
            print(f'A Raiz Quadrada de {number} é {sqrt(number):.2f}')
        