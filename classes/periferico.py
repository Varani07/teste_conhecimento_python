class Periferico():
    """Essa classe cria um Periférico"""
    def __init__(self, memoria, armazenamento):
        self._memoria = memoria
        self._armazenamento = armazenamento


class Computador(Periferico):
    """Essa classe cria um Computador"""
    def __init__(self, memoria, quantidade_fans, armazenamento):
        super.__init__(memoria, armazenamento)
        self._quantidade_fans = quantidade_fans
        self._jogos = {"God of War": True, "The Last of Us": True}
    
    def ver_jogos(self):
        pass