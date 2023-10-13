
import os


palavra_secreta = 'elefante'
letras_acertadas = ''
numero_de_tentativas = 0



while True :
    
    letra_digitada = input('Digite uma letra: ')
    numero_de_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!!')

        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada 

    palavra_formada = ''

    for letras_secretas in palavra_secreta:
        if letras_secretas in letras_acertadas:
            palavra_formada += letras_secretas
            
            

        else:
            palavra_formada += '*'

    print(palavra_formada)        


    if palavra_formada == palavra_secreta:
        

        print(f'Parabens !!! você acerto a palavra secreta que era {palavra_secreta}')     
        print(f'Você tentou {numero_de_tentativas} vezes')   
        letras_acertadas = ''
        numero_de_tentativas = 0
        

