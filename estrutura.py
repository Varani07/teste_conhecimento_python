import os
from pessoa import Pessoa
from caixas_texto import *

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
                    pass
                case 3:
                    running = False
                case _:
                    caixa_erro_int_errado()

        except ValueError:
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
                new_player = Pessoa(answer)
                if len(new_player.nome)>12:
                        caixa_nick_muitos_caracteres()
                elif new_player.verify_nick:
                    if not menu(new_player, True):
                        return False
                    else:
                        return 'voltar'
                else:
                    caixa_nick_ja_existe()

def menu(jogador:object, new_player:bool):
    running = True
    while running:
        nick = jogador.nome
        nivel = jogador.nivel
        energia = jogador.energia

        print()
        print('- - - - - - - - - - - - INÍCIO - - - - - - - - - - - -')
        print(f"player: {nick}")
        print(f"                             nível: {nivel}  |  energia: {energia}")
        print()
        print(' 1 - Ver Status')
        print(' 2 - Ações')
        print(' 3 - Lojas/Mercados')
        print(' 4 - Itens')
        print(' 5 - Coleção')
        print()
        print(' 6 - Início')
        print(' 7 - Sair')
        print()
        print()
        print('                 digite * para salvar                 ')
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
                    return 'voltar'
                case 7:
                    return False
                case _:
                    caixa_erro_int_errado()

        except ValueError:
            if answer == '*':
                if new_player:
                    if jogador.save:
                        caixa_jogo_salvo()
                        new_player = False
                    else:
                        caixa_erro_ao_salvar()
                else:
                    pass
            else:
                caixa_erro_esperava_int()

def opcoes_de_save():
    running = True
    while running:
        print()
        print("Deseja sobrescrever um save ou salvar em um novo slot?")
        print()
        print("1 - Sobrescrever")
        print("2 - Salvar")
        print("3 - Voltar")
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
                    return 'voltar'
                case _:
                    caixa_erro_int_errado()

        except ValueError:
            caixa_erro_esperava_int()