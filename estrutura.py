import os
from pessoa import Pessoa
from caixas_texto import *
from util import *

# ESTRUTURA INICIAL
def inicio():
    os.system('cls')
    running = True
    while running:
        print()
        print('- - - - - - - - - - - - INÍCIO - - - - - - - - - - - -')
        print()
        print(' 1 - Novo Jogo')
        print(' 2 - Carregar Jogo')
        print()
        print(' 3 - Sair')
        print()
        answer = input('Escolha uma opção: ')
        os.system('cls')
        try:
            num = int(answer)
            match num:
                case 1:
                    if not escolhendo_nick():
                        running = False
                case 2:
                    if not load_game():
                        running = False
                case 3:
                    running = False
                case _:
                    caixa_erro_int_errado()

        except ValueError:
            caixa_erro_esperava_int()

def load_game():
    running = True
    while running:
        set_with_nicks = get_nicks()
        num_nick = 1

        print()
        print(' - - - - - - - - - - - - SAVES - - - - - - - - - - - -')
        print()
        print("Players:")
        print()
        for nick in set_with_nicks:
            print(f"{num_nick} - {nick}")
            num_nick += 1
        print()
        print('                 digite * para voltar                 ')
        print()
        print()
        answer = input('Digite o nick do player escolhido: ')
        os.system('cls')
        try:
            num = int(answer)
            caixa_erro_nick()

        except ValueError:
            if answer == '*':
                return 'voltar'
            #* Testa se o input está de acordo com o esperado
            elif answer not in set_with_nicks:
                caixa_erro_nick()
            else:
                #* Se a função retornar False, retorna False também e retorna para @inicio
                if not escolha_save(answer, False):
                    return False

#* param: tipo referente a load, delete e overwrite
def escolha_save(nickname, veio_das_opcoes_de_save:bool, tipo=""):
    running = True
    while running:
        #* Seleciona as informações do banco de dados que possuem esse nick
        saves = get_saves_by_nick(nick=nickname)

        print()
        print(' - - - - - - - - - - - - SAVES - - - - - - - - - - - -')
        print()
        print()
        #* Criando lista para guardar os id's dos saves do jogador
        lista_id = []
        #* Iterando pelos saves para mostra-los
        for save in saves:
            lista_id.append(save[0])
            player_info = desempacotar_json(save[1], save[3])
            print("--------------------------------------------------")
            print(f"                            {save[2]}")
            print(f"ID: {save[0]}")
            print(f"Nick: {player_info.nome} | Nível: {player_info.nivel}/{player_info.nivel_cap}")
            print(f"Dinheiro: R${player_info.currency}")
        print("--------------------------------------------------")
        print()
        print('                 digite * para voltar                 ')
        print()
        print()
        answer = input('Escolha um save pelo ID: ')
        os.system('cls')
        try:
            num = int(answer)
            #* Verifica se o número digitado está na lista de id's
            if num in lista_id:
                #* Pega as informações do save escolhido (dados, tipo FROM player_info)
                infos = get_save_by_id(num)

                #* Iterando pelas informações do save
                for info in infos:
                    #* Transforma os dados JSON em um objeto da classe 
                    #* especificada pela informação vinda do banco de dados
                    player = desempacotar_json(info[0], info[1])

                #* Verifica se o player veio de @opcoes_de_save ou de @load_game
                if veio_das_opcoes_de_save:
                    #* Verifica qual foi a opção escolhida em @opcoes_de_save
                    if tipo == 'load':
                        #* Envia o jogador para o menu, se o mesmo selecionar voltar
                        #* uma mensagem vai aparecer perguntando se ele deseja
                        #* salvar antes de sair ou voltar. Caso decida salvar ou não
                        #* o loop se encerrará e o jogo será salvo ou não, se decidir voltar
                        #* retornará então ao @menu. Se o @menu não retornasse os dados do
                        #* jogador provavelmente eles seriam desconsiderados e apagados,
                        #* como a variável player é atualizada isso não ocorre.
                        #* O caminho de retorno é: @menu -> @escolha_save -> @opcoes_de_save ->
                        #* @menu -> (@escolhendo_nick || @escolha_save -> @load_game) ->
                        #* @inicio -> @exit
                        while running:
                            player = menu(player, False)
                            running = salvar_ao_sair(player)
                        return False
                    elif tipo == 'overwrite':
                        #* Altera as informações de um save
                        player.save_overwrite(num)
                    elif tipo == 'delete':
                        #* Deleta um save, apenas se tiver mais de um
                        if len(lista_id) == 1:
                            caixa_deletar_save_invalido()
                        else:
                            player.deletar_save(num)
                
                else:
                    if not menu(player, False):
                        return False
                    
            else:
                caixa_erro_int_errado()

        except ValueError:
            if answer == '*':
                return 'voltar'
            else:
                caixa_erro_esperava_int()

def escolhendo_nick():
    running = True
    while running:
        print()
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        print()
        print('                 digite * para voltar                 ')
        print()
        answer = input('Digite seu nick: ')
        os.system('cls')
        try:
            num = int(answer)
            caixa_erro_nick()

        except ValueError:
            if answer == '*':
                return 'voltar'
            else:
                #* Cria um novo objeto Pessoa
                new_player = Pessoa(answer)
                #* Verifica se o nickname possui mais de 12 caracteres
                if len(new_player.nome)>12:
                        caixa_nick_muitos_caracteres()
                #* Verifica se já existe um player com o mesmo nome
                elif new_player.verify_nick:
                    if not menu(new_player, True):
                        return False
                else:
                    caixa_nick_ja_existe()

def menu(player:object, new_player:bool):
    running = True
    while running:
        nick = player.nome
        nivel = player.nivel
        energia = player.energia

        print()
        print(' - - - - - - - - - - - - MENU - - - - - - - - - - - - ')
        print(f"player: {nick}")
        print(f"                             nível: {nivel}  |  energia: {energia}")
        print()
        print(' 1 - Ver Status')
        print(' 2 - Ações')
        print(' 3 - Lojas/Mercados')
        print(' 4 - Itens')
        print(' 5 - Coleção')
        print()
        print(' 6 - Voltar')
        print(' 7 - Sair')
        print()
        print()
        print('              digite * para salvar / load             ')
        print()
        answer = input('Escolha uma opção: ')
        os.system('cls')
        try:
            num = int(answer)
            match num:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    return player
                case 7:
                    return False
                case _:
                    caixa_erro_int_errado()

        except ValueError:
            if answer == '*':
                if new_player:
                    if player.save:
                        #* Salva o jogo e seta a variável new_player para False,
                        #* sendo assim da próxima vez que este comendo for feito outras opções apareceram.
                        caixa_jogo_salvo()
                        new_player = False
                    else:
                        caixa_erro_ao_salvar()
                else:
                    #* Encaminha para as opções de save, se retornar False o programa fechará.
                    if not opcoes_de_save(player):
                        return False
            else:
                caixa_erro_esperava_int()

def opcoes_de_save(player:object):
    running = True
    while running:
        print()
        print()
        print("1 - Save Game")
        print("2 - Load Game")
        print("3 - Overwrite Save")
        print("4 - Delete Save")
        print("5 - Voltar")
        print()
        answer = input('Escolha uma opção: ')
        os.system('cls')
        try:
            num = int(answer)
            match num:
                case 1:
                    #* Salva o jogo
                    if player.save:
                        caixa_jogo_salvo()
                    else:
                        caixa_erro_ao_salvar()
                case 2:
                    #* Cerrega outro save, se voltar False o programa fechará
                    if not escolha_save(player.nome, True, "load"):
                        return False
                case 3:
                    #* Escreve os dados do save atual por cima de um save existente
                    escolha_save(player.nome, True, "overwrite")
                case 4:
                    #* Deleta um save (apenas se existir mais de um)
                    escolha_save(player.nome, True, "delete")
                case 5:
                    return 'voltar'
                case _:
                    caixa_erro_int_errado()

        except ValueError:
            caixa_erro_esperava_int()

def salvar_ao_sair(player:object):
    running = True
    while running:
        #* Caixa com as opções
        caixa_salvar_ao_sair()
        answer = input("Digite: ")
        os.system('cls')
        try:
            num = int(answer)
            caixa_resposta_invalida()
        except:
            if answer == 'sim' or answer == 's':
                #* Se desejar salvar antes de sair o jogo irá salvar e o sistema vai fechar
                if player.save:
                    caixa_jogo_salvo()
                else:
                    caixa_erro_ao_salvar()
                return False
            elif answer == 'não' or answer == 'n':
                #* Se desejar sair sem salvar o sistema fechará e os dados serão perdidos
                return False
            elif answer == '*':
                #* Vai voltar para o @menu caso a opção voltar seja escolhida
                return True
            else:
                caixa_resposta_invalida()