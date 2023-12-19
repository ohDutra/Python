
x, y, z, *resto =  13, 23, 33, 43, 53, 63  

def multip_de_args(*args):
    total = 1

    for numero in args:
        total *= numero

    return total    

 
multiplicacao = multip_de_args(1, 2, 3, 4, 5) 
print(multiplicacao)






def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é Par'
    
    return f'{numero} é  Impar'
    


print(par_impar(2))    
print(par_impar(3))    
print(par_impar(5))    
print(par_impar(10))    






