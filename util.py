from dao import DAO
import json
from pessoa import Pessoa
from caixas_texto import *
def get_nicks():
        #* Seleciona o nome dos jogadores fazendo uso de set() para não repetir
        #* as informações, utilizado em @estrutura.py -> @load_game
        get_nicks = DAO()
        nicks = get_nicks.visualizar('nick', 'player_info', "", "", False)
        nicks = {nick[0] for nick in nicks}
        
        return nicks

def get_saves_by_nick(nick):
        #* Seleciona todos os saves de um jogador em ordem data>data, utilizado
        #* em @estrutura.py -> @escolha_save
        get_nicks = DAO()
        nicks = get_nicks.visualizar('id, dados, data_do_save, tipo', 'player_info', " WHERE nick = %s ORDER BY data_do_save DESC", (nick,), False)

        return nicks

def get_save_by_id(id):
        #* Seleciona os dados do save escolhido, utilizado em
        #* @estrutura.py -> @escolha_save
        get_nicks = DAO()
        nicks = get_nicks.visualizar('dados, tipo', 'player_info', " WHERE id = %s", (id,), False)

        return nicks

def desempacotar_json(dados:json, tipo:str):
        #* Recebe do banco de dados as informações do player em JSON,
        #* transforma as mesmas em um dict() e após isso transfere seus
        #* valores para um objeto de sua respectiva classe.
        #! Se os atributos de alguma classe mudar será necessária a manutenção dessa função
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