'''
Operadores logicos

and (e) or (ou) not (não)

and - todas as condições precisam ser verdadeiras
 
or - qualquer cindição()
'''

entrada = input('Digite [E] para entrar, e [S] para sair: ')
senhaDigitada = input('Senha: ')

senhaPermitida = 159

if (entrada == 'E' or entrada == 'e') and senhaDigitada == senhaPermitida :
    print('Entrar')

else:
    print('Sair')






