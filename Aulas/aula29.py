"""
Clouser e Funções que retornam outras funções
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome} ! '
    return 


s1 = criar_saudacao('Bom dia', 'Gabriel')
print(s1)