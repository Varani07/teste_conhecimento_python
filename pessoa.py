import random
from dao import DAO
from itens import Computador
import json
from datetime import datetime
from caixas_texto import *

class Pessoa():
    """Essa classe cria uma Pessoa"""
    def __init__(self, nome:str):
        #* Nome, energia, dinheiro, vida, criatividade, conhecimento sobre culinária,
        #* sorte, higiene, fome, nivel, nivel_cap, carrinho de compras, itens e coleção.
        #TODO Melhorar
        #TODO Implementar:
        #TODO self.current_exp
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
        #* Retorna o nome como valor do objeto
        return self.nome

    def dormir(self):
        #TODO Implementar
        pass

    def beber_algo(self, tipo:object):
        #TODO Implementar
        pass

    def descansar(self):
        #TODO Implementar
        pass

    @property
    def save(self):
        #* Salva as informações do player
        salvar = DAO()
        try:
            salvar.inserir('player_info', 'dados, nick, data_do_save, tipo', '%s, %s, %s, %s', (self.player_to_json, self.nome, datetime.now(), self.tipo))
            return True
        except:
            return False
        
    def deletar_save(self, id:int):
        #* Deleta o save do player
        delete_save = DAO()
        try:
            delete_save.deletar('player_info', 'id = %s', (id,))
            caixa_save_deletado(True)
        except:
            caixa_save_deletado(False)

    def save_overwrite(self, id:int):
            #* Altera o save do player
            overwrite_save = DAO()
            try:
                overwrite_save.atualizar('player_info', "dados = %s, data_do_save = %s", "id = %s", (self.player_to_json, datetime.now(), id))
                caixa_sobrescrever(True)
            except:
                caixa_sobrescrever(False)

    @property
    def verify_nick(self):
        #* Verifica se o nickname já existe
        verificar_se_nick_existe = DAO()
        if verificar_se_nick_existe.visualizar('nick', 'player_info', ' WHERE nick = %s', (self.nome,), True):
            return False
        else:
            return True

    @property
    def player_to_json(self):
        #* Transforma as informações do objeto em um dicionário
        #! Se os atributos da classe mudarem será necessária a manutenção dessa função
        #TODO Dinamizar os objetos presentes dentro do objeto
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
        #* Para objetos dentro do objeto é necessário fazer uso de list comprehension 
        #* para que assim sejam armazenados de forma dinâmica
        player_dict['carrinho_compras'] = [{'memoria': item.memoria, "fans": item.quantidade_fans, "armazenamento":item.armazenamento, "preço":item.preco, "jogos": []} for item in self.carrinho_de_compras if isinstance(item, Computador)]
        player_dict['itens'] = [{'memoria': item.memoria, "fans": item.quantidade_fans, "armazenamento":item.armazenamento, "preço":item.preco, "jogos": []} for item in self.carrinho_de_compras if isinstance(item, Computador)]
        #* As informações do dicionário são transformadas em JSON e então retornadas
        player_json = json.dumps(player_dict)

        return player_json

    @property
    def get_last_save(self):
        #* Retorna as informações do ultimo save do player
        get_id_last_save = DAO()
        id_save = get_id_last_save.visualizar('id', 'player_info', ' WHERE nick = %s ORDER BY data_do_save DESC LIMIT 1', self.nome, True)
        return id_save
        

    @property
    def currency(self):
        #* Retorna a quatia de dinheiro do player
        return self.dinheiro

    def adicionar_produtos_carrinho_de_compras(self, loja:object, num_serie:str):
        #* Adiciona o item especifícado pelo número de série e presente no objeto Loja 
        #* ao carrinho de compras do player
        produto = loja.adicionar_produtos_carrinho_de_compras(num_serie)
        if(produto != None):
            self.carrinho_de_compras.append(produto)

    @property
    def limpar_carrinho_de_compras(self):
        #* Reseta o carrinho de compras
        self.carrinho_de_compras = []

    @property
    def ver_carrinho_de_compras(self):
        #* Mostra os itens presentes no carrinho de compras do player 
        #* juto ao seu respectivo preço e valor total
        #? Verificar necessidade de melhoria do método
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

    #* Método Parse guardado, usar se necessário
    # @property
    # def parseGamer(self):
    #     #* Cria um objeto Gamer a partir de um objeto Pessoa
    #     #! Se os atributos da classe mudarem será necessária a manutenção dessa função
    #     new_obj = Gamer(nome=self.nome)

    #     new_obj.energia = self.energia
    #     new_obj.dinheiro = self.dinheiro
    #     new_obj.vida = self.vida
    #     new_obj.criatividade = self.criatividade
    #     new_obj.conhecimento_culinaria = self.conhecimento_culinaria
    #     new_obj.sorte = self.sorte
    #     new_obj.higiene = self.higiene
    #     new_obj.fome = self.fome

    #     new_obj.carrinho_de_compras = self.carrinho_de_compras
    #     new_obj.itens = self.itens
    #     return new_obj
    
    @property
    def tipo(self):
        #* Retorna o tipo do objeto
        return "Pessoa"

    @property
    def comprar(self):
        total = 0
        print()
        #* Verifica se o carrinho está vazio
        if len(self.carrinho_de_compras) != 0:
            #* Junta o valor de todos os itens presentes na lista, soma eles e armazena
            #* o resultado na variável total
            total = sum([item.preco for item in self.carrinho_de_compras])
            #* Verifica se o player possui dinheiro o suficiente
            if self.dinheiro >= total:
                self.dinheiro -= total
                #* Iterando pelos itens presentes no carrinho
                for item in self.carrinho_de_compras:
                    #* Adiciona item a lista de itens e altera o atributo dono 
                    #* para o nome deste objeto
                    self.itens.append(item)
                    item.dono = f" de {self.nome}"
                    #TODO Fazer uma caixa para compra bem sucedida
            else:
                print("DINHEIRO INSUFICIENTE!")
                #TODO Fazer uma caixa para saldo insuficiente
            # COMPLETAR FUNÇÃO PARA EFETIVAR A COMPRA

class Gamer(Pessoa):
    """Essa classe cria uma Pessoa que joga"""
    def __init__(self, nome:str):
        #* Nome, todos os atributos da classe Pessoa e uma lista de jogos.
        #? Verificar possibilidade de novas implementações
        super().__init__(nome)
        self.jogos = []

    @property
    def parsePessoa(self):
        #* Cria um objeto Pessoa a partir de um objeto Gamer
        #! Se os atributos da classe mudarem será necessária a manutenção dessa função
        new_obj = Pessoa(nome=self.nome)
        
        new_obj.energia = self.energia
        new_obj.dinheiro = self.dinheiro
        new_obj.vida = self.vida
        new_obj.criatividade = self.criatividade
        new_obj.conhecimento_culinaria = self.conhecimento_culinaria
        new_obj.sorte = self.sorte
        new_obj.higiene = self.higiene
        new_obj.fome = self.fome

        new_obj.carrinho_de_compras = self.carrinho_de_compras
        new_obj.itens = self.itens
        return new_obj

    def ver_jogos(self):
        #TODO Implementar
        pass

    def jogar(self):
        #TODO Implementar
        pass

    @property
    def tipo(self):
        #* Retorna o tipo do objeto
        return "Gamer"