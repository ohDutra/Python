"""
split e join com list e str, recebe um argumento para quebrar a frase
split - dividi uma string
join - une uma string
"""


frase = 'que dia quente que fez hoje, amanha tem que esfriar'

lista_de_palavras = frase.split(',')

for i,frase in enumerate(lista_de_palavras):
    print(lista_de_palavras[1].strip())

print(lista_de_palavras)