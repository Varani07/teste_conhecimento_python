import random

class Itens():
    """Essa classe cria um Item"""

    def __init__(self, num_de_serie:str):
        #* dono verifica qual o dono do item, alterado ao ser comprado ou vendido 
        #* e o número de série feito para identificar um item na loja.
        #? Verificar possibilidade de novas implementações
        self.dono = ""
        self.num_de_serie = num_de_serie
    
    def colocar_preco(self, valor:float):
        #* Método padrão para se definir o preço de um item
        self.preco = valor

    def __ge__(self, dinheiro:float):
        #* Método utilizado para verificar se o preço do item é maior ou igual ao valor
        #* em dinheiro
        #? Verificar necessidade
        self.preco >= dinheiro

    def __str__(self):
        #* Valor do objeto se torna igual ao seu tipo + nome do dono atual
        return f"{self.tipo}{self.dono}"

    @property
    def tipo(self):
        #* Retorna tipo do objeto
        return "Item"


class Computador(Itens):
    """Essa classe cria um Computador"""
    def __init__(self, memoria:int, quantidade_fans:int, armazenamento:int, num_de_serie:str):
        #* Possui todos os atributos da classe Itens, quantidade de fans, memória, armazenamento,
        #* lista de jogos e preço.
        super().__init__(num_de_serie)
        self.quantidade_fans = quantidade_fans
        self.memoria = memoria
        self.armazenamento = armazenamento
        self.jogos = []
        self.preco = self.colocar_preco
    
    @property
    def colocar_preco(self):
        #? Verificar possíveis melhorias
        preco = (self.memoria * 2) + (self.quantidade_fans * 3) + (self.armazenamento * 3)
        #* Verifica se objeto tem algum jogo em sua lista, se sim o preço vai aumentar
        #* equivalente a 25% do preço de cada jogo somado
        if len(self.jogos) > 0:
            preco += sum([(jogo.preco)*0.25 for jogo in self.jogos])
        return preco
    
    def ver_jogos(self):
        #TODO Implementar
        pass

    @property
    def tipo(self):
        #* Retorna tipo do objeto
        return "Computador"