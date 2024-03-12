resultado = []
def soma(a, b, c):
    for i in range(3):

        resultado.append(a + b + c)

def multi(a, b, c):
    for i in range(3):

        resultado.append(a * b * c)



print("[S]oma ou [M]ulti")

entrada = input(". . . . . ")

primeiroNumero = int(input("Digite"))
segundoNumero = int(input("Digite"))
terceiroNumero = int(input("Digite"))



if entrada == "S" or entrada == "s":
    soma(primeiroNumero,segundoNumero,terceiroNumero)
    print(resultado)

else:
    multi(primeiroNumero,segundoNumero,terceiroNumero)
    print(resultado)    