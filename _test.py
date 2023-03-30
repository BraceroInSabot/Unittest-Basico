from main import ligar_lampada, porcentagem, carro
import unittest


class Testes(unittest.TestCase):
    def teste_lampada(self):
        self.assertEqual(
            ligar_lampada(True),
            "Por favor, insira apenas 1 ou 0",
        )
        self.assertTrue(
            ligar_lampada(1),
        )
        self.assertFalse(
            ligar_lampada(0),
        )

    def teste_porcentagem(self):
        num_max = 3381
        num = 29

        self.assertEqual(
            porcentagem(
                num_max=num_max,
                num=num,
            ),
            980.49,
        )
        self.assertFalse(
            porcentagem(
                num_max=f"{num_max}",
                num=num,
            ),
        )
        self.assertTrue(
            porcentagem(
                num_max=100,
                num=10,
            )
        )

    def teste_carro(self):
        self.assertFalse(carro(motor=False, trancado=False))


if __name__ == "__main__":
    unittest.main()
