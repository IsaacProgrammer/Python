print('-' * 50)
print(f'{"CAIXA ELETRÔNICO":^50}')
print('-' * 50)
while True:
    valor = float(input('Deseja sacar quanto? R$'))
    total = valor
    céd = 100
    totcéd = 0
    while True:
        if total >= céd:
            total -= céd
            totcéd += 1
        else:
            if totcéd > 0:
                print(f'Sacando...{totcéd} notas de R${céd:.2f}')
            if céd == 100:
                céd = 50
            elif céd == 50:
                céd = 20
            elif céd == 20:
                céd = 10
            elif céd == 10:
                céd = 5
            elif céd == 5:
                céd = 2
            elif céd == 2:
                céd = 1
            totcéd = 0
            if total == 0:
                break
    print('-' * 50)
