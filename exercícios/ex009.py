from time import sleep
print('-' * 50)
print(f'{"FIBONACCI":^50}')
print('-' * 50)
while True:
    n = int(input('Quer ver quantos elementos do fatorial. Informe 0 para parar: '))
    if n == 0:
        break
    t1 = 0
    t2 = 1
    c = 0
    print(t1, end=' ') 
    sleep(1)
    print(t2, end=' ')
    sleep(1)
    while c <= n:
        t3 = t1 + t2
        print(t3, end=' ')
        t1 = t2
        t2 = t3
        c += 1
        sleep(1) 
    print()
print('-' * 50)
print('Obrigado!!! Volte sempre')
