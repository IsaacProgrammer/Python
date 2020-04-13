print('-' * 50)
print(f'{"TABUADA":^50}')
print('-' * 50)
while True:
    n = int(input('Informe um número para mostrar a sua tabuada: '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 50)
print('-' * 50)
print('Obrigado, volte sempre!')
print('-' * 50)
