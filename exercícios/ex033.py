# Importação para o programa

from datetime import date

# Função para mostrar o ID no arquivo

c = 0


def counter():
    global c
    try:
        a = open('people.txt', 'rt')
    except:
        print('{ ERROR }')
    else:
        for linha in a:
            register = linha.split(';')
            if not register[0] in '':
                d = int(register[0])
                c = d
    count = counter1(c)
    count += 1
    return count


def counter1(c):
    return c

# Funções para criar o arquivo


def check(arc):
    try:
        a = open(arc, 'rt')
    except:
        return False
    else:
        return True


def create(arc):
    try:
        a = open(arc, 'wt+')
    except:
        print('[ ERROR ] Error to create the archive')
    else:
        print('[ SUCCESS ] Archive created Successfully')


def read(arc):
    try:
        a = open(arc, 'rt')
    except:
        print('[ ERROR ] ')
    else:
        for linha in a:
            register = linha.split(';')
            register[2] = register[2].replace('\n', '')
            print(f'{register[0]:2} | {register[1]:<8} | {register[2] + " Anos"}')
        print(line())


def write(arc, name, age):
    c = counter()
    try:
        a = open(arc, 'at')
    except:
        print('[ ERROR ] ')
    else:
        try:
            a.write(f'{c};{name};{age}\n')
        except:
            print('ERROR')
        else:
            print('New people registered successfully')
            print(line())

# Funções para o cabeçalho


def line(t=100):
    return '=' * t


def header(msg):
    print(line())
    print(f'{msg:^100}')
    print(line())


def menu(lst):
    c = 1
    for item in lst:
        print(f'{c}° {item}')
        c += 1
    print(line())
    option = number('Option: ')
    return option


def number(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('[ Try Again ] Just Numbers')
        else:
            return n
            break


# Começando o programa

arc = 'people.txt'

if not check(arc):
    create(arc)

header('Register People')

while True:
    option = menu(['Cadastrar Pessoa', 'Ver pessoas cadastradas', 'Quit'])
    if option == 1:
        name = str(input('Nome: ')).strip().title()
        birth = number('Ano de Nascimento: ')
        age = date.today().year - birth
        write(arc, name, age)
    elif option == 2:
        read(arc)
    elif option == 3:
        header('Exiting')   
        break
