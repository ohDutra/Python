"""
                             Estrutura Sequencial
1
print('Hello World')



2
numero_digitado = input('Digite um numero: ')
print(f'O numero digitado foi {numero_digitado}')


3

primeiro_numero_digitado = int(input('Digite o primeiro numero: '))
segundo_numero_digitado = int(input('Digite o segundo numero: '))

soma = (primeiro_numero_digitado + segundo_numero_digitado)

print(f'A soma dos numero {primeiro_numero_digitado} + {segundo_numero_digitado} é {soma}')


4
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))
quarta_nota = float(input('Digite a quarta nota: '))


media_bimestre = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4
print(
    f'A media bimestral é: {media_bimestre}'
    )

5
metros_digitados = float(input('Digite a metragem que deseja converter em centimetros: '))

centimetros_convertidos = metros_digitados * 100

print(
    f'{centimetros_convertidos:.0f} centimetros'
    )

6
raio_do_circulo = int(input('Digite o raio do circulo para ser convertido: '))

raio_dividido = int(raio_do_circulo / 2) ** 2
conversao_para_area = raio_dividido * 3,14


print(conversao_para_area)


7

tamanho_do_quadrado = int(input('Digite o tamanho do quadrado: '))

area_do_quadrado = tamanho_do_quadrado ** 2 
dobro_da_area = area_do_quadrado * 2



print(
    f'A area do quadrado é {area_do_quadrado} cm, e o dobro dessa area é {dobro_da_area}cm'
      )
      
8

valor_recebido_por_hora = int(input('Digite o valor que recebe por hora: '))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas no dia: '))
quantidade_de_dias_trabalhados = int(input('Digite a quantidade de dias trabalhados: '))

calculo_do_salario = (horas_trabalhadas * quantidade_de_dias_trabalhados) * valor_recebido_por_hora



print(
    f'O Valor do seu salario mensal é {calculo_do_salario}'
    )

9    

fahrenheit = int(input('Digite os graus em Fahrenheit: '))

calculo = 5 * ((fahrenheit - 32) / 9)

print(
    f'A conversão de {fahrenheit} fahrenheit para {calculo:.1f}° celsius'
    )


    10
celsius = int(input('Digite a temperatura em graus Celsius: '))

calculo = ((celsius * 1.8) + 32)

print(
    f'A conversão de {celsius}° Celsius para {calculo}° Fahrenheit'
    )

11

altura = float(input('Digite a sua altura: '))

calculo = (72.7 * altura) - 58


print(
    f'O calculo do seu peso ideal é: {calculo:.1f}'
    )


verificacao = input('Para verificar seu peso ideal, digite (m) para mulher e (h) para homem: ')

12

if verificacao == 'm' or verificacao == 'M':
    altura_mulher = float(input('Digite a sua altura: '))
    calculo_mulher = (62.1*altura_mulher) - 44.7
    print(
        f'Seu peso ideal é: {calculo_mulher:.1f}'
        )

elif verificacao == 'h' or verificacao == 'H':
    altura_homem = float(input('Digite a sua altura: '))
    calculo_homem =  (72.7* altura_homem) - 58    
    print(
        f'Seu peso ideal é: {calculo_homem:.1f}'
        )

else:
    print('Escolha uma das opções indicadas ')    
    

13


peso_de_peixes = float(input('Digite quantos kilos: ')) 


limite_de_kilos_permitidos = 50
multa_por_excesso = 0
kilos_excedido = 0

if peso_de_peixes > limite_de_kilos_permitidos:
    
    kilos_excedido = peso_de_peixes - 50
    multa_por_excesso = kilos_excedido  * 4 

print(f'Limite de kilos de peixe permitido {limite_de_kilos_permitidos:.1f} kg')
print(f'kilos de peixe informados {peso_de_peixes} kg')
print(f'Valor da multa por excesso R$ {multa_por_excesso:.2f}')
print(f'Kilos de peixe excedido {kilos_excedido:.1f} kg')


14

horas_trabalhadas_mes = float(input('Digite quantas horas trabalha por mês: '))
valor_ganho_por_hora = float(input('Digite quanto recebe por hora trabalhada: '))


salario_bruto = (horas_trabalhadas_mes * valor_ganho_por_hora)

desconto_inss = (8 * salario_bruto) / 100
desconto_imposto_de_renda = (11 * salario_bruto) / 100
desconto_sindicato = (5 * salario_bruto) / 100
descontos = (24 * salario_bruto) / 100
salario_liquido = (salario_bruto - descontos)


print(f'+ Salario Bruto : R$ {salario_bruto}')
print(f'- IR : R$ {desconto_imposto_de_renda}')
print(f'- INSS : R$ {desconto_inss}')
print(f'- Sindicato : R$ {desconto_sindicato}')
print(f'- Descontos : R$ {descontos}')
print(f'= Salario Liquido : R$ {salario_liquido}')

"""
# 1 litro a cada 3 metros
# lata com 18 litros
# valor da lata 80 reais
# 1 lata faz 54 metros


metros_area = float(input('Digite a area a ser pintada: '))


contador = 1

while metros_area > 54:
    metros_area = - 54
    contador += 1

print(contador)







