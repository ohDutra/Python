"""
DocString
"""
#\r\n = CRLF
# print(1+1 , 2+2, sep='-', end='') # argumentos são divididos por virgulas
# print(1+3 , 2+4, sep='-') # argumentos são divididos por virgulas


pergunta = int(input("quer somar mais um numero? 1 [Sim] ou 2 [Não]"))


while pergunta == 1:
   print(1+1)
   pergunta = int(input("quer somar mais um numero? 1 [Sim] ou 2 [Não]"))
    
   if pergunta == 1:
      continue
   else:
      break

    