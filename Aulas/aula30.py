'''
Dicionários em Python (tipo dict)
 Dicionários são estruturas de dados do tipo
 par de "chave" e "valor".
 Chaves podem ser consideradas como o "índice"
 que vimos na lista e podem ser de tipos imutáveis
 como: str, int, float, bool, tuple, etc.
 O valor pode ser de qualquer tipo, incluindo outro
 dicionário.
 Usamos as chaves - {} - ou a classe dict para criar
 dicionários.
 Imutáveis: str, int, float, bool, tuple
 Mutável: dict, list

 '''

cadastro_pessoa = {
    'nome': 'Gabriel',
    'sobrenome': 'Dutra',
    'idade': 25,
    'altura': 1.85,
    'endereços': [
        {'rua': 'Rua tal tal tal', 'numero':100},
        {'rua': 'Estrada tal tal tal','numero': 5859},
    ]

}




for chave in cadastro_pessoa:
    print(chave, cadastro_pessoa[chave])