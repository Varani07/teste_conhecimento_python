import random

class Loja():
    #TODO 
    def __init__(self, nome:str):
        #* Nome, lista com os produtos da loja
        #TODO Melhorar!
        self.nome = nome
        self.produtos = []

    def adicionar_a_loja(self, item:object):
        #* Adiciona um item a loja
        self.produtos.append(item)

    @property
    def ver_produtos(self):
        #* Mostra os produtos da loja
        #TODO Melhorar e implementar formatação para outros itens
        id = 1
        print()
        print(f"- - - - {self.nome} - - - -")
        for item in self.produtos:
            if item.tipo == "Computador":
                print(f"{id}: {item} por R${item.preco} | especificacoes: Armazenamento ({item.armazenamento}GB), Memoria ({item.memoria}GB), Fans (un.{item.quantidade_fans}) | num.serie: {item.num_de_serie}")
                print()
            id += 1
        print("- - - - - - - - - - - - - - - -")

    def adicionar_produtos_carrinho_de_compras(self, num_serie:str):
        #* Adiciona um item da loja ao carrinho de compras se o número de série for encontrado
        for item in self.produtos:
            if item.num_de_serie == num_serie:
                print()
                print("Item adicionado ao carrinho de compras!")
                print()
                return item
        print("Item nao encontrado!")
        return None

    def definir_codigo_de_serie(self, item):
        #* Gera um número de série para os produtos da loja
        #! Testar
        if item.tipo == "Computador":
            num_serie = "C"
            for volta in range(1, 6):
                num_serie += str(random.randint(1, 9))
                if volta == 4:
                    num_serie += "-"
        return num_serie