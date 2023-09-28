'''
introdução ao try / except
except -> ocorreu alguem erro ao tentar executar 
'''

numero_str = input('Vou dobrar os numeros que vc digitar: ')




'''
if numero_str.isdigit():
    numero_int = int(numero_str)
    print(f'O dobro de {numero_str} é {numero_int * 2}')

else:
    print('Isso não é um numero')
'''


try:
    numero_int = int(numero_str)
    print('INT', numero_int)
    print(f'O dobro de {numero_str} é {numero_int * 2}')

except:
    print('Isso não é um numero')