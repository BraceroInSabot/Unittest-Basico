from main import ligar_lampada, porcentagem, ligar_carro
import unittest


class LigarLampada(unittest.TestCase):
    def teste_lampada(self):
        """
        Testa a função importada "ligar_lampada" de 3 maneiras diferentes
        """
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


class Porcentagem(unittest.TestCase):
    """
    Testa a função importada "porcentagem" de 3 maneiras diferentes
    """

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


class LigarCarro(unittest.TestCase):
    def teste_carro(self):
        """
        Testa a função importada "ligar_carro" em 10 vezes diferentes. Por conta de haver dois parametros de valores booleanos, foi necessário fazer a Tabela Verdade

        TABELA VERDADE

        _M_|_T_|_!(M_->_T)_|
         F | F |___F____|
         T | T |___F____|
         F | T |___F____|
         T | F |___T____|
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
