import random
from dao import DAO
from itens import Computador
import json

class Pessoa():
    """Essa classe cria uma Pessoa"""
    def __init__(self, nome:str):
        self.nome = nome
        self.energia = random.randint(5, 25)
        self.dinheiro = random.randint(50, 250)
        self.vida = random.randint(20, 25)
        self.criatividade = random.randint(1, 5)
        self.conhecimento_culinaria = random.randint(0, 5)
        self.sorte = random.randint(0, 3)
        self.higiene = random.randint(20, 25)
        self.fome = random.randint(20, 25)

        self.nivel = 0
        self.nivel_cap = 20

        self.carrinho_de_compras = []
        self.itens = []
        self.colecao = {}

    def __str__(self):
        return self.nome

    def dormir(self):
        pass

    def beber_algo(self, tipo:object):
        pass

    def descansar(self):
        pass

    @property
    def save(self):
        salvar = DAO()
        salvar.inserir('player_info', 'dados', '%s', self.player_to_json, "jogo salvo")

    @property
    def player_to_json(self):
        player_dict = {
            "nome": self.nome,
            "energia": self.energia,
            "dinheiro": self.dinheiro,
            "vida": self.vida,
            "criatividade": self.criatividade,
            "culinaria": self.conhecimento_culinaria,
            "sorte": self.sorte,
            "higiene": self.higiene,
            "fome": self.fome,
            "nivel": self.nivel,
            "nivel_cap": self.nivel_cap,
            "carrinho_compras": [],
            "itens": [],
            "colecao": []   
        }
        player_dict['carrinho_compras'] = [{'memoria': item.memoria, "fans": item.quantidade_fans, "armazenamento":item.armazenamento, "preço":item.preco, "jogos": []} for item in self.carrinho_de_compras if isinstance(item, Computador)]
        player_dict['itens'] = [{'memoria': item.memoria, "fans": item.quantidade_fans, "armazenamento":item.armazenamento, "preço":item.preco, "jogos": []} for item in self.carrinho_de_compras if isinstance(item, Computador)]
        player_json = json.dumps(player_dict)

        return player_json

    @property
    def currency(self):
        print(self.dinheiro)

    def adicionar_produtos_carrinho_de_compras(self, loja:object, num_serie:str):
        produto = loja.adicionar_produtos_carrinho_de_compras(num_serie)
        if(produto != None):
            self.carrinho_de_compras.append(produto)

    @property
    def limpar_carrinho_de_compras(self):
        self.carrinho_de_compras = []

    @property
    def ver_carrinho_de_compras(self):
        total = 0
        print()
        print("- - - - - - - - - - - - - - - - - - -")
        for item in self.carrinho_de_compras:
            total += item.preco
            print(f"Produto: {item}, Preco: R${item.preco}")
        print()
        print(f"Total: R${total}")
        print("- - - - - - - - - - - - - - - - - - -")
        print()

    @property
    def parseGamer(self):
        new_obj = Gamer(nome=self.nome)

        new_obj.energia = self.energia
        new_obj.dinheiro = self.dinheiro
        new_obj.vida = self.vida
        new_obj.criatividade = self.criatividade
        new_obj.conhecimento_culinaria = self.conhecimento_culinaria
        new_obj.sorte = self.sorte
        new_obj.higiene = self.higiene
        new_obj.fome = self.fome
        new_obj.hora = self.hora

        new_obj.carrinho_de_compras = self.carrinho_de_compras
        new_obj.itens = self.itens
        return new_obj

    @property
    def comprar(self):
        total = 0
        print()
        if len(self.carrinho_de_compras) != 0:
            total = sum([item.preco for item in self.carrinho_de_compras])
            if self.dinheiro >= total:
                self.dinheiro -= total
                for item in self.carrinho_de_compras:
                    self.itens.append(item)
                    item.dono = f" de {self.nome}"
            else:
                print("DINHEIRO INSUFICIENTE!")
            # COMPLETAR FUNÇÃO PARA EFETIVAR A COMPRA

class Gamer(Pessoa):
    """Essa classe cria uma Pessoa que joga"""
    def __init__(self, nome:str):
        super().__init__(nome)
        self.itens = []
        self.jogos = []

    @property
    def parsePessoa(self):
        new_obj = Pessoa(nome=self.nome)
        
        new_obj.energia = self.energia
        new_obj.dinheiro = self.dinheiro
        new_obj.vida = self.vida
        new_obj.criatividade = self.criatividade
        new_obj.conhecimento_culinaria = self.conhecimento_culinaria
        new_obj.sorte = self.sorte
        new_obj.higiene = self.higiene
        new_obj.fome = self.fome
        new_obj.hora = self.hora

        new_obj.carrinho_de_compras = self.carrinho_de_compras
        new_obj.itens = self.itens
        return new_obj

    def ver_jogos(self):
        pass

    def jogar(self):
        pass