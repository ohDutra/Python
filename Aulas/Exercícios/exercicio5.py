velocidade_do_carro = 100 # velocidade atual do carro
local_carro  = 103 #local em que o carro esta na estrada

RADAR_1 = 60  #velocidade maxima do radar 1
RADAR_2 = 100  #velocidade maxima do radar 1
RADAR_3 = 120  #velocidade maxima do radar 1
LOCAL_DO_RADAR_1 = 100  #Local aonde o radar 1 esta  
LOCAL_DO_RADAR_2 = 103  #Local aonde o radar 1 esta  
LOCAL_DO_RADAR_3 = 105  #Local aonde o radar 1 esta  
RADAR_RANGE = 1  # A distancia aonde o radar pega

velocidade_permitida_radar_1 = RADAR_1 - RADAR_RANGE
velocidade_permitida_radar_2 = RADAR_2 - RADAR_RANGE
velocidade_permitida_radar_3 = RADAR_3 - RADAR_RANGE

if local_carro == LOCAL_DO_RADAR_1 and (velocidade_do_carro > velocidade_permitida_radar_1):
    print(f'Carro passou radar 1 a {velocidade_do_carro} km e foi multado ' )

else:
    print('Carro passou radar 1')    


if local_carro == LOCAL_DO_RADAR_2 and (velocidade_do_carro > velocidade_permitida_radar_2):
    print(f'Carro passou radar 2 a {velocidade_do_carro} km e foi multado ' )

else:
    print('Carro passou radar 2')     


if local_carro == LOCAL_DO_RADAR_3 and (velocidade_do_carro > velocidade_permitida_radar_3):
    print(f'Carro passou radar 3 a {velocidade_do_carro} km e foi multado ' )

else:
    print('Carro passou radar 3') 