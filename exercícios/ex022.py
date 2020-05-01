print('-' * 40)
print(f'{"VELOCIDADE":^40}')
print('-' * 40)
while True:
    vel = float(input('Em que velocidade está? '))
    if vel >= 80:
        multa = (vel * 2.00) - 80
        print('MULTADO! Utrapaçou o limite de velocidade. Multa: R${:.2f}'.format(multa))
    else:
        print('LIVRE! Está no limite!')