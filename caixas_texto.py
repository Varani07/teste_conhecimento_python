def caixa_nick_muitos_caracteres():
    print()
    print('------------------------------')
    print('| NICK COM MUITOS CARACTERES |')
    print('------------------------------')
    print()

def caixa_salvar_ao_sair():
    print()
    print('--------------------------------')
    print('| DESEJA SALVAR ANTES DE SAIR? |')
    print('--------------------------------')
    print()
    print("Responda com 'sim'|'s' ou 'não'|'n'")
    print()
    print()
    print('      digite * para voltar      ')
    print()

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
    print('|- DIGITE UM NICK VÁLIDO! -|')
    print('----------------------------')
    print()

def caixa_nick_ja_existe():
    print()
    print('----------------------------')
    print('|-- NICK JÁ ESTÁ EM USO! --|')
    print('----------------------------')
    print()

def caixa_jogo_salvo():
    print()
    print('----------------------------')
    print('|------- JOGO SALVO -------|')
    print('----------------------------')
    print()

def caixa_erro_ao_salvar():
    print()
    print('----------------------------')
    print('|-- ERRO AO SALVAR JOGO! --|')
    print('----------------------------')
    print()

def caixa_resposta_invalida():
    print()
    print('----------------------------')
    print('|--- RESPOSTA INVÁLIDA! ---|')
    print('----------------------------')
    print()

def caixa_deletar_save_invalido():
    print()
    print('--------------------------------------------------------')
    print('| AÇÃO INVÁLIDA, NÃO É POSSÍVEL DELETAR SAVE ESCOLHIDO |')
    print('--------------------------------------------------------')
    print()

def caixa_save_deletado(deletou:bool):
    if deletou:
        print()
        print('----------------------------')
        print('|------ SAVE DELETADO ------|')
        print('----------------------------')
        print()
    else:
        print()
        print('----------------------------')
        print('|-- ERRO AO DELETAR SAVE --|')
        print('----------------------------')
        print()

def caixa_sobrescrever(sobrescreveu:bool):
    if sobrescreveu:
        print()
        print('----------------------------')
        print('|---- SAVE MODIFICADO! ----|')
        print('----------------------------')
        print()
    else:
        print()
        print('----------------------------')
        print('|-- ERRO AO ALTERAR SAVE --|')
        print('----------------------------')
        print()