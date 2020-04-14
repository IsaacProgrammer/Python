print('-' * 50)
print(f'{"PARTIDA DE FUTEBOL":^50}')
print('-' * 50)
times = []
time1 = []
time2 = []
for i in range(0, 2):
    times.append(str(input(f'Qual o nome do {i+1}° time? ')))
    times.append(int(input(f'Quantos gols {times[0]} fez? ')))
    if i == 0:
        time1.append(times[:])
        times.clear()
    elif i == 1:
        time2.append(times[:])
        times.clear()
    print('-' * 50)
for t1 in time1:
    for t2 in time2:
        if t1[1] > t2[1]:
            dif = t1[1] - t2[1]
        elif t2[1] > t1[1]:
            dif = t2[1] - t1[1] 
        else:
            dif = 0
print(f'A diferença de gols foi de: {dif} gols')
print('-' * 50)
print('Isso classifica uma partida:', end=' ')
if dif == 0:
    print('EMPATE')
elif dif <= 3:
    print('NORMAL')
elif dif <= 5:
    print('GOLEADA')
elif dif <= 7:
    print('HARD CORE')
else:
    print('SURREAL')
         