print('-' * 50)
print(f'{"Validação de Dados":^50}')
print('-' * 50)
sexo = ' '
while not sexo in 'MF':
    sexo = str(input('Informe seu Sexo: [ M / F ] ')).strip().upper()[0]
print('O sexo Informado foi {}'.format(sexo))