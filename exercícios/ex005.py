print('-' * 50)
print(f'{"IMC":^50}')
print('-' * 50)
peso = float(input('Qual é o seu peso? '))
alt = float(input('Qual é sua Altura? '))
imc = peso / (alt ** 2)
print(f'Seu IMC -> {imc:.1f}')
if imc < 18.5:
    print('CUIDADO: Seu índice está em MAGRESA')
elif imc >= 18.5 and imc <= 24.9:
    print('Seu índica esta em NORMAL')
elif imc >= 25.0 and imc <= 29.9:
    print('CUIDADO: Seu índice está em SobrePeso')
elif imc >= 30.0 and imc <= 39.9:
    print('CUIDADO: Seu índice está em Obesidade')
else:
    print('CUUIIDADOOO: Seu índice está em Obesidade Grave')