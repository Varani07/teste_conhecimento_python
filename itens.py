import random

class Itens():
    """Essa classe cria um Item"""

    def __init__(self, num_de_serie:str):
        self.dono = ""
        self.num_de_serie = num_de_serie
    
    def colocar_preco(self, valor:float):
        self.preco = valor

    def __ge__(self, dinheiro:float):
        self.preco >= dinheiro

    def __str__(self):
        return f"{self.tipo}{self.dono}"

    @property
    def tipo(self):
        return "Item"


class Computador(Itens):
    """Essa classe cria um Computador"""
    def __init__(self, memoria:int, quantidade_fans:int, armazenamento:int, num_de_serie:str):
        super().__init__(num_de_serie)
        self.quantidade_fans = quantidade_fans
        self.memoria = memoria
        self.armazenamento = armazenamento
        self.jogos = []
        self.preco = self.colocar_preco
    
    @property
    def colocar_preco(self):
        preco = (self.memoria * 2) + (self.quantidade_fans * 3) + (self.armazenamento * 3)
        if len(self.jogos) > 0:
            preco += sum([(jogo.preco)*0.25 for jogo in self.jogos])
        return preco
    
    def ver_jogos(self):
        pass

    @property
    def tipo(self):
        return "Computador"