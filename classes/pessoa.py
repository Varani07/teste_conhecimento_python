class Pessoa():
    """Essa classe cria uma Pessoa"""
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    @property
    def aniversario(self):
        self._idade += 1
    @property
    def mostrar_info(self):
        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")

class Gamer(Pessoa):
    """Essa classe cria uma Pessoa que joga"""
    def __init__(self, nome, idade, periferico):
        super.__init__(nome, idade)
        self._periferico = periferico
        self._jogos = []

    def comprar_jogo(self):
        pass