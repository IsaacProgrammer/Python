print('-' * 50)
print(f'{"Pintando Parede":^50}')
print('-' * 50)
larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
área = larg * alt
print(f'A área dessa parede é {larg}x{alt} = {área}m²')
tinta = área / 2
print(f'O total gasto de tinta será de {tinta}L')