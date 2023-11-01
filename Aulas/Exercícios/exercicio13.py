"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re
import sys

entrada = input('Digite o seu CPF:[746.824.890-70] ')

cpf_enviado = re.sub(
    r'[^0-9]',
    '',
    entrada
    
)

verificacao_de_numeros_repetidos = entrada == entrada[0] * len(entrada)

if verificacao_de_numeros_repetidos:
    print('Voce não digitou um CPF')
    sys.exit()




nove_digito = cpf_enviado[:9]
contador_regressivo_1 = 10

soma_dos_nove_digitos = 0
primeiro_digito_calculado = 0

for digito in nove_digito:
    
    soma_dos_nove_digitos += (int(digito) * contador_regressivo_1) * 10
    contador_regressivo_1 -= 1
    primeiro_digito_calculado = soma_dos_nove_digitos % 11

primeiro_digito_calculado = primeiro_digito_calculado if primeiro_digito_calculado <= 9 else 0


dez_digito = nove_digito + str(primeiro_digito_calculado)
contador_regressivo_2 = 11

soma_dos_dez_digitos = 0
segundo_digito_calculado = 0

for digito in dez_digito:
    soma_dos_dez_digitos += (int(digito) * contador_regressivo_2) * 10 
    contador_regressivo_2 -= 1
    segundo_digito_calculado = soma_dos_dez_digitos % 11

segundo_digito_calculado = segundo_digito_calculado if segundo_digito_calculado <= 9 else 0


novo_cpf = f'{nove_digito}{primeiro_digito_calculado}{segundo_digito_calculado}'

if cpf_enviado == novo_cpf:
    print(f'O CPF {cpf_enviado} é valido')

else:    
    print(f'O CPF {cpf_enviado} é invalido')
















