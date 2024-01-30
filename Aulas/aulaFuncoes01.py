"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).

Escopo significa o local onde aquele codigo pode atingir.
Existe o escopo global e local
O escopo global é o oscopo onde todo codigo é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos
A palavra global faz uma variavel de escopo externo ser a mesma no escopo interno 

args argumentos não nomeados
* - *args (empacotamento e desempacotamento)



#def soma(x, y, z):
    #Difinição de função
#    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z)

#soma(1, 2 , 3)
#soma(1, y = 2, z=3)

#print(1,2,3, sep='-')



primeiro_numero = 5

def escopo():

    primeiro_numero = 6
    segundo_numero = 7
    print(primeiro_numero, segundo_numero)

    def sergundo_Escopo():
        
        primeiro_numero = 8
        segundo_numero = 9

        print(primeiro_numero, segundo_numero)

    sergundo_Escopo()
   

print(primeiro_numero)
escopo()
print(primeiro_numero)    
"""



def soma(a , b, c):
    
    print(f'{a=} {b=} {c=}', '|', 'a + b + c =', a+b+c)


soma(b= 10, a= 15, c= 20)    





