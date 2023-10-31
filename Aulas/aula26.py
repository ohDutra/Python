numeros = 12345

lista = ['Gabriel', 'Aparecido', 'Dutra', 1, 2, 3, 'Lima']

strings = 'Gabriel'

salas = [
    # 0        1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine'] ,   #  1
    # 0         1       2
    ['Luiz', 'João', 'Eduarda', 'Marcos']  # 2
]
#g, a, d, l ,*__= lista

print(*numeros)
print(*lista)
print(*strings)
print(*salas)