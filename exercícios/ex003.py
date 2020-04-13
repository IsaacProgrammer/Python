from time import sleep
print('-' * 50)
print(f'{"Reajuste Salárial":^50}')
print('-' * 50)
nomefun = []
novo = []
while True:
    nome = str(input('Qual o nome da Empresa? ')).strip().title()
    fun = int(input(f'Quantos funcionários(as) na Empresa {nome}? '))
    print('AGUARDE...')
    sleep(1.5)
    print('-' * 50)
    for c in range(0, fun):
        nomefun.append(str(input('Qual é o nome do Funcionário(a): ')).strip().title())
        nomefun.append(float(input(f'Quanto o funcionário(a) {nomefun[0]} ganha: ')))
        nomefun.append(int(input(f'Em quantos Porcento quer aumentar do salário da {nomefun[0]}: ')))
        novo.append(nomefun[:])
        nomefun.clear()
    break
print('-' * 50)
for item in novo:
    novoSal = item[1] + (item[1] * item[2] / 100)
    print(f'O Novo salário de {item[0]} agora vai ser R${novoSal:.2f}')
    print('-' * 50)
