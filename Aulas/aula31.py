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
del cadastro_pessoa['sobrenome']

if cadastro_pessoa.get('sobrenome', None):

    print(cadastro_pessoa['sobrenome'])

else:
    print(cadastro_pessoa)