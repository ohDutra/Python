nome = input('Digite seu nome: ')


contador = 0
novo_nome = ''

while contador < len(nome):
    letra = nome[contador]
    novo_nome += f' {letra}'
    contador += 1

print(f'O seu nome tem {len(novo_nome)} caracteres no total. {novo_nome}')    
