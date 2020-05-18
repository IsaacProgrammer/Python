from random import choice
print('=' * 25)
print(f'{"Escolhendo um Nome":^25}')
print('=' * 25)
alunos = []
c = 1
while True:
    while True:
        alunos.append(str(input(f'Nome do {c} aluno(a): ')).strip().title())
        c += 1
        resp = ' '
        while not resp in 'SN':
            resp = str(input('Quer Continuar: { S / N } ')).strip().upper()[0]
        if resp in 'N':
            break
    print('=' * 25)
    escolha = choice(alunos)
    print(f'O Aluno(a) Escolhido(a) foi {escolha}')
    resp = ' '
    while not resp in 'SN':
        resp = str(input('Quer Continuar: { S / N } ')).strip().upper()[0]
    if resp in 'N':
        break
     