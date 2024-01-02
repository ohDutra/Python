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

15

primeiro_numero_digitado = int(input('Digite o primeiro numero: '))
segundo_numero_digitado = int(input('Digite o segundo numero: '))

if primeiro_numero_digitado > segundo_numero_digitado:
    print(f'O numero {primeiro_numero_digitado} é maior que {segundo_numero_digitado}')

elif primeiro_numero_digitado == segundo_numero_digitado:
    print(f'O numero {primeiro_numero_digitado} e o numero {segundo_numero_digitado} são iguais')

else:
    print(f'O numero {segundo_numero_digitado} é maior que {primeiro_numero_digitado}')    


16

verificacao_de_numero = int(input('Digite um numero: '))

if verificacao_de_numero > 0:
    print(f'O numero {verificacao_de_numero} é positivo')

else:
    print(f'O numero {verificacao_de_numero} é negativo')    



17

letra_digitada = input('Digite F (Feminino) ou M (Masculino): ')


if letra_digitada == 'f' or letra_digitada == 'F':
    print('Feminino')


elif letra_digitada == 'm' or letra_digitada == 'M':
    print('Masculino')


else:
    print('Sexo invalido')


18

letra_digitada = input('Digite uma letra: ')

vogal = 'aeiou AEIOU'

consoante = ' B C D F G J K L M N P Q R S T V W X Y Z b c d f g j k l m n p q r s t v w x y z'


if letra_digitada in vogal:
    print(f'A letra {letra_digitada} é uma Vogal')

else:
    print(f'A letra {letra_digitada} é uma consoante')    

19

primeira_nota = int(input('Digite a primeira nota: '))
segunda_nota = int(input('Digite a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2


if media > 6 and media < 9 :
    print(f'Aprovado, sua media foi {media}')

elif media == 10 :
        print(f'Aprovado com Distinção, sua media foi {media}')

else:
    print(f'Reprovado, sua media foi {media}')



20

primeiro_numero_digitado = int(input('Digite o primeiro numero: '))
segundo_numero_digitado = int(input('Digite o segundo numero: '))
terceiro_numero_digitado = int(input('Digite o terceiro numero: '))

if primeiro_numero_digitado > segundo_numero_digitado and primeiro_numero_digitado > terceiro_numero_digitado:
    print(f'O numero {primeiro_numero_digitado} é maior entre eles!')

elif segundo_numero_digitado > primeiro_numero_digitado and segundo_numero_digitado > terceiro_numero_digitado:    
        print(f'O numero {segundo_numero_digitado} é maior entre eles!')

elif terceiro_numero_digitado > primeiro_numero_digitado and terceiro_numero_digitado > segundo_numero_digitado:
    print(f'O numero {terceiro_numero_digitado} é maior entre eles!')

else:
    print(f'Os tres numeros são iguais!')


21

primeiro_numero_digitado = int(input('Digite o primeiro numero: '))
segundo_numero_digitado = int(input('Digite o segundo numero: '))
terceiro_numero_digitado = int(input('Digite o terceiro numero: '))


maior_numero_digitado = 0
menor_numero_digitado = 0

if primeiro_numero_digitado > segundo_numero_digitado and primeiro_numero_digitado > terceiro_numero_digitado:

    maior_numero_digitado = primeiro_numero_digitado

elif segundo_numero_digitado > primeiro_numero_digitado and segundo_numero_digitado > terceiro_numero_digitado:

    maior_numero_digitado = segundo_numero_digitado    
else:
    maior_numero_digitado = terceiro_numero_digitado


if primeiro_numero_digitado < segundo_numero_digitado and primeiro_numero_digitado < terceiro_numero_digitado:
    menor_numero_digitado = primeiro_numero_digitado

elif segundo_numero_digitado < primeiro_numero_digitado and segundo_numero_digitado < terceiro_numero_digitado:
    menor_numero_digitado = segundo_numero_digitado

else:
    menor_numero_digitado = terceiro_numero_digitado


print(f'O maior numero é {maior_numero_digitado}')                    
print(f'O menor numero é {menor_numero_digitado}')              


22



primeiro_produto = float(input('Digite o preço do primeiro produto: '))
segundo_produto = float(input('Digite o preço do segundo produto: '))
terceiro_produto = float(input('Digite o preço do terceiro produto: '))



produto_mais_barato = 0



if primeiro_produto < segundo_produto and primeiro_produto < terceiro_produto:
    produto_mais_barato = primeiro_produto

elif segundo_produto < primeiro_produto and segundo_produto < terceiro_produto:
    produto_mais_barato = segundo_produto

else:
    produto_mais_barato = terceiro_produto


print(f'O produto mais barato custa R$ {produto_mais_barato}')            





23.	As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
o	Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
o	salários até R$ 280,00 (incluindo) : aumento de 20%
o	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o	salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o	o salário antes do reajuste;
o	o percentual de aumento aplicado;
o	o valor do aumento;
o	o novo salário, após o aumento.




salario_colaborador = int(input('Digite o salario do colaborador: '))
nome_colaborador = input('Digite o nome do colaborador: ')

reajuste = 0
salario_colaborador_reajustado = 0

if salario_colaborador <= 280:
    reajuste += salario_colaborador * 0.20 
    salario_colaborador_reajustado = reajuste + salario_colaborador
    print(f'Colaborador: {nome_colaborador}\nSalario: R$:{salario_colaborador:.2f}\nReajuste de 20% = R$:{reajuste:.2f}\nNovo Salario R${salario_colaborador_reajustado:.2f} '
    )

elif salario_colaborador >= 280 and salario_colaborador <= 700:
    reajuste += salario_colaborador * 0.15
    salario_colaborador_reajustado += reajuste + salario_colaborador
    print(f'Colaborador: {nome_colaborador}\nSalario: R$:{salario_colaborador:.2f}\nReajuste de 15% = R$:{reajuste:.2f}\nNovo Salario R${salario_colaborador_reajustado:.2f} '
    )

elif salario_colaborador >= 700 and salario_colaborador <= 1500:
    reajuste += salario_colaborador * 0.10
    salario_colaborador_reajustado += reajuste + salario_colaborador
    print(f'Colaborador: {nome_colaborador}\nSalario: R$:{salario_colaborador:.2f}\nReajuste de 15% = R$:{reajuste:.2f}\nNovo Salario R${salario_colaborador_reajustado:.2f} '
    )
else:
    reajuste += salario_colaborador * 0.05
    salario_colaborador_reajustado += reajuste + salario_colaborador
    print(f'Colaborador: {nome_colaborador}\nSalario: R$:{salario_colaborador:.2f}\nReajuste de 5% = R$:{reajuste:.2f}\nNovo Salario R${salario_colaborador_reajustado:.2f} '
    )    

    




24.	Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que  deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
o	Desconto do IR:
o	Salário Bruto até 900 (inclusive) - isento
o	Salário Bruto até 1500 (inclusive) - desconto de 5%
o	Salário Bruto até 2500 (inclusive) - desconto de 10%
o	Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
o	        Salário Bruto: (5 * 220)        : R$ 1100,00
o	        (-) IR (5%)                     : R$   55,00  
o	        (-) INSS ( 10%)                 : R$  110,00
o	        FGTS (11%)                      : R$  121,00
o	        Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00

"""







