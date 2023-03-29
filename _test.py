from main import ligar_lampada, porcentagem, carro
import unittest


class Testes(unittest.TestCase):
    def teste_lampada(self):
        self.assertEqual(ligar_lampada(1), "Luz Acesa")

    def teste_porcentagem(self):
        self.assertEqual(porcentagem(num_max=3381, num=29), 980.49)

    def teste_carro(self):
        self.assertFalse(carro(motor=False, trancado=False))


if __name__ == "__main__":
    unittest.main()
