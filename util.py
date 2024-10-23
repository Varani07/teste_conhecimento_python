from dao import DAO
import json
from pessoa import Pessoa
from caixas_texto import *
def get_nicks():
        get_nicks = DAO()
        nicks = get_nicks.visualizar('nick', 'player_info', "", "", False)
        nicks = {nick[0] for nick in nicks}
        
        return nicks

def get_saves_by_nick(nick):
        get_nicks = DAO()
        nicks = get_nicks.visualizar('id, dados, data_do_save, tipo', 'player_info', " WHERE nick = %s ORDER BY data_do_save DESC", (nick,), False)

        return nicks

def get_save_by_id(id):
        get_nicks = DAO()
        nicks = get_nicks.visualizar('dados, tipo', 'player_info', " WHERE id = %s", (id,), False)

        return nicks

def desempacotar_json(dados:json, tipo:str):
        info_player = json.loads(dados)
        if tipo == 'Pessoa':
                player = Pessoa(nome=info_player['nome'])

                player.energia = info_player['energia']
                player.dinheiro = info_player['dinheiro']
                player.vida = info_player['vida']
                player.criatividade = info_player['criatividade']
                player.conhecimento_culinaria = info_player['culinaria']
                player.sorte = info_player['sorte']
                player.higiene = info_player['higiene']
                player.fome = info_player['fome']
                player.nivel = info_player['nivel']
                player.nivel_cap = info_player['nivel_cap']
                player.carrinho_de_compras = info_player['carrinho_compras']
                player.itens = info_player['itens']
                player.colecao = info_player['colecao']

                return player