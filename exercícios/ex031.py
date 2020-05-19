from random import shuffle
print('=' * 25)
print(f'{"Sorteando Aluno":^25}')
print('=' * 25)
alunos = []
c = 1
print('Escreva quais são os alunos que vão apresentar')
confirm = ' '
while True:
    try:
        aluno = int(input('Quantos aluno: '))
    except:
        print('Try Again')
    else:
        for a in range(0, aluno):
            alunos.append(str(input(f'Nome do(a) {a}° aluno(a): ')).strip().capitalize())
        print('=' * 25)
        shuffle(alunos)
        print('A Ordem é: ')
        for aluno in alunos:
            print(f'O(a) {c} aluno(a) a apresentar será {aluno}')
            c += 1
        resp = ' '
        while not resp in 'SN':
            resp = str(input('Quer Continuar: [ S / N ] ')).strip().upper()[0]
        if resp in 'N':
            break
        
