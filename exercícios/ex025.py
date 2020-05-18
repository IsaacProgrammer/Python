from datetime import date
print('=' * 25)
print(f'{"Classificando Atletas":^25}')
print('=' * 25)
while True:
    try:
        nasc = int(input('Ano de Nascimento: '))
        idade = date.today().year - nasc
    except:
        print('[ ERROR ] Try Again')
    else:
        if idade <= 7:
            print(f'Idade: {idade} anos\nClassificação: Mirin')
        elif idade <= 14:
            print(f'Idade: {idade} anos\nClassificação: Infantil')
        elif idade <= 19:
            print(f'Idade: {idade} anos\nClassificação: Junior')
        elif idade <= 25:
            print(f'Idade: {idade} anos\nClassificação: Sênior')
        else:
            print(f'Idade: {idade} anos\nClassificação: Master')
        print('=' * 25)
