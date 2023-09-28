"""
CONSTANTES - "Variaveis" que não vão munda (Usar em maiuscula)
muitas condições no mesmo if ( Rim )
<-- Contagem de complexidade ( Rim )
"""

velocidade = 50 # velocidade atual do carro
local_carro  = 102 #local em que o carro esta na estrada

RADAR_1 = 60  #velocidade maxima do radar 1
LOCAL_1 = 100  #Local aonde o radar 1 esta  
RADAR_RANGE = 1  # A distancia aonde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_multador_radar_1 = local_carro (LOCAL_1 - RADAR_RANGE)