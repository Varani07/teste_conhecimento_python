import os
from pessoa import Pessoa

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

def caixa_erro_esperava_int():
    print()
    print('----------------------------')
    print('|---- DIGITE UM NÚMERO ----|')
    print('----------------------------')
    print()

def caixa_erro_int_errado():
    print()
    print('----------------------------')
    print('| DIGITE UM NÚMERO VÁLIDO! |')
    print('----------------------------')
    print()

def caixa_erro_nick():
    print()
    print('----------------------------')
    print('|- DIGITE UM NOME VÁLIDO! -|')
    print('----------------------------')
    print()

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
                if not menu(new_player):
                    return False
                else:
                    return 'voltar'



def menu(jogador:object):
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
                jogador.save
            else:
                caixa_erro_esperava_int()