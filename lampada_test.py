from main import ligar_lampada
import unittest


class LampadaTeste(unittest.TestCase):

    def teste_lampada(self):
        self.assertEqual(ligar_lampada(1), "Luz Acesa")


if __name__ == "__main__":
    unittest.main()