'''
def saudacoes(saudacao):
    def nomes(nome):
        return f'{saudacao}, {nome}!'
    return nomes

bom_dia = saudacoes('Bom Dia')
boa_noite = saudacoes('Boa noite')

for lista_de_nomes in ['Gabriel', 'Clicia', 'Fuba']:
    print(bom_dia(lista_de_nomes))
    print(boa_noite(lista_de_nomes))
'''





def dobrar(numero):
    print(f'Dobrando {numero}')
    return numero * 2
def triplicar(numero):
    print(f'Triplicando {numero}')
    return numero * 3
def quadruplicar(numero):
    print(f'Quadruplicando {numero}')
    return numero * 4


print(dobrar(5))
print(triplicar(5))
print(quadruplicar(5))