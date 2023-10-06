while True:
   primeiro_numero = input('Digite um numero: ')
   segundo_numero = input('Digite mais um numero: ')
   operador = input('Digite um operador ( + - / *) ')


   numeros_validos = None
   primeiro_numero_float = 0
   segundo_numero_float = 0

   try:
      primeiro_numero_float = float(primeiro_numero)
      segundo_numero_float = float(segundo_numero)
      numeros_validos = True

   except:
      numeros_validos = None


   if numeros_validos is None:
      print('Um ou ambos os numeros digitados são invalidos ')
      continue



   operadores_permitidos = '+-/*'

   if operador not in operadores_permitidos:
      print('Operador invalido')
      continue  
 

   if len(operador) > 1:
      print('Digite apenas um operador.')
      continue

   if operador == '+':
      print(primeiro_numero_float + segundo_numero_float)

   elif operador == '-':
      print(primeiro_numero_float - segundo_numero_float)

   elif operador == '*':
      print(primeiro_numero_float * segundo_numero_float)    

   elif operador == '/':
      print(primeiro_numero_float / segundo_numero_float)
 

   pergunta_de_parada = input('Deseja sair? Digite [ S ]').lower

   if pergunta_de_parada == 's':
         break
   else:
      continue
  