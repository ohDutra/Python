login = ['dutra']
password = [159]

contador = 0

while contador <= 4:
    
    usuario = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    
    if usuario in login:
        if senha in password:
            print('Acesso Liberado')

        else:
            print('Login ou Password invalidos')
            contador += 1
print('Recuperar senha')            


