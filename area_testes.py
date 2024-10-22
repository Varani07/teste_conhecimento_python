
item1 = {
    "tipo": 'dano',
    "nome": 'faca',
    "dano": 1
}
item2 = {
    "tipo": 'dano',
    "nome": 'espada',
    "dano": 10
}
item3 = {
    "tipo": 'magia',
    "nome": 'bastão',
    "dano": 10,
    "dano mágico": 100
}


lista_itens = [item1, item2, item3]

dicionario = {
    "Nome": 'math',
    "itens": []
}
print(dicionario)
dicionario["itens"] = [{"tipo":item["tipo"], "nome":item["nome"]} for item in lista_itens if item["tipo"] == 'dano']
dicionario["itens"] += [{"tipo":item["tipo"], "nome":item["nome"]} for item in lista_itens if item["tipo"] == 'magia']
# for item in lista_itens:
#     if item["tipo"] == 'dano':
#         dicionario["itens"] = 


print(dicionario)