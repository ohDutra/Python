lista_de_compras = []


while True:
    print('Selecione uma opção!')
    opcao = input('[a]dicionar [d]eletar [m]ostrar: ')

    if opcao == 'a' or opcao == 'A':
        novo_produto = input('Digite o nome do produto para a sua lista de compras: ')
        lista_de_compras.append(novo_produto)
        
    
    elif opcao == 'd' or opcao == 'D':
        deletar = int(input('Digite o numero que deseja apagar: '))
        lista_de_compras.pop(deletar)


    elif opcao == 'm' or opcao == 'M':

        for a,b in enumerate(lista_de_compras):

            print(a,b)
    
    
    else:
        print('Opção invalida ! Digite a, d ou m')

