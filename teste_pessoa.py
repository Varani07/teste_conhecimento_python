import unittest
from unittest.mock import MagicMock
from objetos_para_teste import ObjPessoa

class TestePessoa(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.pessoa_padrao = ObjPessoa.pessoa_padrao()
        self.pessoa_nome_errado = ObjPessoa.pessoa_nome_errado()
        self.pessoa_dinheiro_errado = ObjPessoa.pessoa_dinheiro_errado()
        self.pessoa_energia_errada = ObjPessoa.pessoa_energia_errada()

    @classmethod
    def tearDownClass(cls):
        pass
    
    def tearDown(self):
        pass
    
    def teste_nome_certo(self):
        self.assertIsInstance(self.pessoa_padrao.nome, str)

    def teste_nome_errado(self):
        self.assertNotIsInstance(self.pessoa_nome_errado.nome, str)

    def teste_dinheiro_certo(self):
        self.assertIsInstance(self.pessoa_padrao.dinheiro, float)

    def teste_dinheiro_errado(self):
        self.assertNotIsInstance(self.pessoa_dinheiro_errado.dinheiro, float)

    def teste_energia_certa(self):
        self.assertIsInstance(self.pessoa_padrao.energia, int)

    def teste_energia_errada(self):
        self.assertNotIsInstance(self.pessoa_energia_errada.energia, int)

if __name__ == "__main__":
    unittest.main()