print('-' * 50)
print(f'{"Sistema de Segurança":^50}')
print('-' * 50)
email = str(input('Seu E-mail: ')).strip().title()
while True:
    try:
        senha = int(input('Informe uma senha: (somente númerso inteiros): '))
    except:
        print('Senha Inválida...Informe Novamente')
    else:
        while True:
            try: 
                confirma = int(input('Confime a sua senha: '))
            except:
                print('Senha Inválida...Informe novamente.')
            else:
                if senha == confirma:
                    break
                else:
                    print('Digite a senha novamente. (senhas não correspondem)')
        break
print('-' * 50)
print(f'Olá {email}, seja bem-vindo(a)')
print('-' * 50)
