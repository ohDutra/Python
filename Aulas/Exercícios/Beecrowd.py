resultado = []
def soma(a, b):
    for i in range(3):

        resultado.append(a + b )

def multi(a, b):
    for i in range(3):

        resultado.append(a * b )



print("[S]oma ou [M]ulti")

entrada = input(". . . . . ")

primeiroNumero = int(input("Digite"))
segundoNumero = int(input("Digite"))



if entrada == "S" or entrada == "s":
    soma(primeiroNumero,segundoNumero)
    print(resultado)

else:
    multi(primeiroNumero,segundoNumero)
    print(resultado)    