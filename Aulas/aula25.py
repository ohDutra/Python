salas = [
    # 0        1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine'] ,   #  1
    # 0         1       2
    ['Luiz', 'João', 'Eduarda', 'Marcos']  # 2
]


#print(salas[0][1])
#print(salas[2][2])
#print(salas[2][3][2])


for sala in salas:
    for alunos in sala:
        print(alunos)