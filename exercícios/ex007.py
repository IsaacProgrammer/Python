print('-' * 50)
print(f'{"Menu de Opções":^50}')
print('-' * 50)
while True:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    opcao = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Dividir\n[ 4 ] Mostrar Maior\n[ 5 ] Mostrar Menor\n[ 6 ]Subtrair\n[ '))
    print('-' * 50)
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} = {n1 * n2}')
    elif opcao == 3:
        print(f'A Divisão entre {n1} e {n2} = {n1 / n2}')
    elif opcao == 4:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            maior = 0
        print(f'O Maior número é {maior}')
    elif opcao == 5:
        menor = n1
        if n2 < menor:
            menor = n2
        print(f'O menor número é {menor}')
    elif opcao == 6:
        print(f'{n1} - {n2} = {n1 - n2}')
    else:
        print(f'Informação Errada')