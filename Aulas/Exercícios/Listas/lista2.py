'''
Ex 1

numeros_positivos = []
numeros_negativos = []
contador = 0

try:
    while contador <= 10:
        numero_digitado = int(input('Digite um numero: '))
        if numero_digitado > 0:
            numeros_positivos.append(numero_digitado)
            contador += 1


        else:
            numeros_negativos.append(numero_digitado)
            contador += 1


except:
    print('Isso não é um numero !!!')

print(
    f'Os numeros positivos são {numeros_positivos} e os numeros negativos são {numeros_negativos}'
)    

Ex 2 



nomes_ate_5_letras = []
nomes_com_mais_de_5_letras = []

contador = 0

try:
    while contador <= 5:
        nome_digitado = input('Digite um nome: ')
        if len(nome_digitado) <= 5:
            nomes_ate_5_letras.append(nome_digitado)
            contador += 1

        else:
            nomes_com_mais_de_5_letras.append(nome_digitado)
            contador += 1

except:
    print('ERRO !!!')



print(
    f'Os nomes com até 5 letras são {nomes_ate_5_letras} e os nomes com mais de 5 letras são {nomes_com_mais_de_5_letras}'
)    

'''


def saudacao(nome):
    print(f'Ola, {nome}')

saudacao(input('Digite seu nome: '))    