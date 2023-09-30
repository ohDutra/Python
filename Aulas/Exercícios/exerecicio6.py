"""
Faça um programa que peça ao usuario para digitar um numero inteiro, informe se este numero é par ou impar. Caso o usuario não digite um numero inteiro, informe que não é um numero inteiro.
"""

numero_recebido = input('Digite um numero inteiro: ')


if '.' in numero_recebido:
    print(f'{numero_recebido} não é um numero inteiro')

else:
    numero_inteiro = int(numero_recebido)    

    if (numero_inteiro % 2) == 0:
        print(f'{numero_inteiro} é par')

    else:
        print(f'{numero_inteiro} é impar')



"""
Faça um programa que pergunto a hora ao usuario e, baseando=se no horario descrito. exiba a saudação apropriada. Ex: Bom dia 0 - 11 , boa tarde 12 = 17 e boa noite 18 - 23.



horario_digitado = input('Digite um horario: ')

BOM_DIA = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)    
BOA_TARDE = (12, 13, 14, 15, 16, 17)
BOA_NOITE = (18, 19, 20, 21, 22, 23)



if horario_digitado in BOM_DIA:
    print('Bom dia')

elif horario_digitado in BOA_TARDE:
    print('Boa tarde')

else:
    print('Boa noite')    

"""

horario_digitado = input('Digite um horario: ')

verificacao_de_horario = int(horario_digitado)

if verificacao_de_horario >= 0 and verificacao_de_horario <= 11:
    print('Bom dia ')

elif verificacao_de_horario >= 12 and verificacao_de_horario <= 17:
    print('Boa tarde')    

else:
    print('Boa noite')  

    

"""

faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal "; maior que 6 escreva "Seu nome é muito grande"

"""


nome_digitado = input('Digite seu nome: ')

nome_verificado = len(nome_digitado)


if nome_verificado <= 4:
    print(f"Seu nome é curto ele tem {nome_verificado} letras")

elif nome_verificado >= 5 and (nome_verificado <= 6 ):
    print(f"Seu nome é normal ele tem {nome_verificado} letras")   

else:
    print(f'Seu nome é muito grande ele tem {nome_verificado} letras') 
      
