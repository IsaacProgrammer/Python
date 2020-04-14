def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('Erro! Digite o número novamente...')
        else:
            return n
            break


print('-' * 50)
print(f'{"Tratamento Dados":^50}')
print('-' * 50)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
