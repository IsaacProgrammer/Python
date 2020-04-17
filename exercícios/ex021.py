print('-' * 50)
print(f'{"Cadastro":^50}')
print('-' * 50)
print('Cadastre-se aqui')
print('-' * 50)
pessoas = 1
ida = ids = mas = 0
while True:
    nome = str(input(f'Nome da {pessoas}° pessoa: ')).strip().title()
    idade = int(input(f'Idade de {nome}: '))
    sal = float(input(f'Quanto {nome} ganha: '))
    sexo = ' '
    while not sexo in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    es = ' '
    while not es in 'SCD':
        es = str(input('Estado Civil: Soteiro(a) - Casado - Divorsiádo\n[ S ]\n[ C ]\n[ D ]\n[ ')).strip().upper()[0]
    pessoas += 1
    resp = ' '
    if idade >= 18:
        ida += 1
    else:
        ids += 1
    if sexo in 'M':
        mas += 1
    while not resp in 'SN':
        resp = str(input('Quer Continuar: [ S / N ] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-' * 50)
print(f'Existem {ida} pessoas que tem mais de 18 anos ou 18 completo')
print(f'Existem {ids} pessoas que tem menos de 18 anos')
print(f'Existem {mas} que são do sexo Masculino')
