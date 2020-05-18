print('=' * 25)
print(f'{"Conversor de Moedas":^25}')
print('=' * 25)
while True:
    try:
        reais = float(input('Quantos reais você tem? R$'))
    except:
        print('[ ERROR ] Try Again')
    else:
        print(f'R${reais:.2f} em doláres é US${reais / 5.86:.2f}')