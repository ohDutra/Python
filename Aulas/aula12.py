'''
Formatação basica de strings
- string
- int
- float
< numero de digitos> f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< direita
^ centro
Sinal - + ou -
Ex.: 0>-10,.1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:#>10}')

print(f'{10000.0000000000:,.1f}')