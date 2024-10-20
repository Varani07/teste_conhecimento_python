import random

class Loja():
    def __init__(self, nome:str):
        self.nome = nome
        self.produtos = []

    def adicionar_a_loja(self, item:object):
        self.produtos.append(item)

    @property
    def ver_produtos(self):
        id = 1
        print()
        print(f"- - - - {self._nome} - - - -")
        for item in self.produtos:
            if item.tipo == "Computador":
                print(f"{id}: {item} por R${item.preco} | especificacoes: Armazenamento ({item.armazenamento}GB), Memoria ({item.memoria}GB), Fans (un.{item.quantidade_fans}) | num.serie: {item.num_de_serie}")
                print()
            id += 1
        print("- - - - - - - - - - - - - - - -")

    def adicionar_produtos_carrinho_de_compras(self, num_serie:str):
        for item in self.produtos:
            if item.num_de_serie == num_serie:
                print()
                print("Item adicionado ao carrinho de compras!")
                print()
                return item
        print("Item nao encontrado!")
        return None

    # def definir_codigo_de_serie(self, item):
    #     if item.tipo == "Computador":
    #         num_serie = ""
    #         for _ in range(1, 11):
    #             num_serie += str(random.randint(1, 10))
    #     return num_serie