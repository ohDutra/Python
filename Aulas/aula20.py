'''
tipo de list - mutavel
metodos uteis:
append - adiciona um item ao final da lista
insert - adiciona um item no indice escolhido
pop - remove um item no final ou no indice escolhido
del - apaga um indice
clear - limpa a lista
extend estende a lista
+ - concatena listas 
create read update   delete
criar, ler, alterar, apagar = lista[i] (CRUD)

'''



lista = ['nome', 'idade', 'data nacimento', ]



nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
data_de_nacimento = input('Digite sua data de nacimento: ')
lista[0] = nome
lista[1] = idade
lista[2] = data_de_nacimento

print(lista)