from main import ligar_lampada, porcentagem, ligar_carro
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
        """
        Tabela verdade
        _M_|_T_|
         F | F |
         T | T |
         F | T |
         T | F |
        """
        self.assertFalse(ligar_carro(motor=False, trancado=False))
        self.assertFalse(ligar_carro(motor=True, trancado=True))
        self.assertFalse(ligar_carro(motor=False, trancado=True))
        # Caso onde o carro deve ligar, pois está destrancado e o motor já ligado
        self.assertTrue(ligar_carro(motor=True, trancado=False))

        for test in range(0, 3 + 1):
            self.assertFalse(ligar_carro(rodas=test))

        self.assertFalse(
            ligar_carro(
                rodas=True,
                motor=True,
                trancado=False,
            )
        )

        self.assertFalse(ligar_carro(motor="4"))


if __name__ == "__main__":
    unittest.main()
