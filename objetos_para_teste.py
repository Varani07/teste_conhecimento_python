from pessoa import Pessoa

class ObjPessoa():
    def pessoa_padrao():
        pessoa = Pessoa("João", 18, 258.90, 25)
        return pessoa
    def pessoa_nome_errado():
        pessoa = Pessoa(19, 18, 258.90, 25)
        return pessoa
    def pessoa_dinheiro_errado():
        pessoa = Pessoa(19, 18, {258.90}, 25)
        return pessoa
    def pessoa_energia_errada():
        pessoa = Pessoa(19, 18, 258.90, [25])
        return pessoa