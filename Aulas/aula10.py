'''
Operadores logicos

and (e) or (ou) not (não)

and - todas as condições precisam ser verdadeiras
 
or - qualquer cindição()

not - True = False
not - False = True

and 



Operadores in e not in

Strings são interaveis

0 1 2 3 4 5 6

G a b r i e l

-7-6-5-4-3-2-1
'''


entrada = input('Digite [E] para entrar, e [S] para sair: ')
senhaDigitada = input('Senha: ')

senhaPermitida = 159

if (entrada == 'E' or entrada == 'e') and senhaDigitada == senhaPermitida :
    print('Entrar')

else:
    print('Sair')

