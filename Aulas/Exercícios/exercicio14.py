
#                                   gerador de CPF


import random


nove_digito = ''

for i in range(9):
    nove_digito += str(random.randint(0, 9))


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

print(novo_cpf)