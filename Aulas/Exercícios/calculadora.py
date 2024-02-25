def adicao(a, b):
    print(f"{a} + {b} = {a + b}")

def subtracao(a, b):
    print(f"{a} - {b} = {a - b}")

def multiplicacao(a, b):
    print(f"{a} x {b} = {a * b}")  

def dividir(a, b):
    print(f"{a} / {b} = {a / b:.2f}")      
    
numeros_digitados = []
for i in range(2):
    numeros_digitados.append(int(input("Digite um numero: ")))

print()
print("Escolha uma opção\n5Adição (A)\nSubtração (S)\nMultiplicação (M)\nDivisão (D)")    

opcao = input()

while True:     

    if opcao == 'A' or opcao == 'a':
        adicao(numeros_digitados[0], numeros_digitados[1])
    elif opcao == 'S' or opcao == 's':
        subtracao(numeros_digitados[0], numeros_digitados[1])
    elif opcao == 'M' or opcao == 'm':
        multiplicacao(numeros_digitados[0], numeros_digitados[1])   
    elif opcao == 'D' or opcao == 'd':
        dividir(numeros_digitados[0], numeros_digitados[1])     

    pergunta = int(input("quer somar mais um numero? 1 [Sim] ou 2 [Não]"))

    if pergunta is True:
        break



#dividir(numeros_digitados[0], numeros_digitados[1])