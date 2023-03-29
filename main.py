def ligar_lampada(condicao: int) -> str:
    """
    Define o estado de uma lampada

    :param:
    condicao: int -> estado da lampada (0 ou 1)
    """
    if condicao == 0:
        # print("Luz apagada")
        return "Luz apagada"
    elif condicao == 1:
        # print("Luz Acesa")
        return "Luz Acesa"


def porcentagem(num_max: float, num: float):
    """
    Retorna a o valor da porcentagem de num% de num_max (100%)

    num_max -- 100%
    num -- ?

    :param:
    num_max: float -> indica o 100% de um valor
    num: float -> indica a uma porcentagem
    """

    num = (num / 100) * num_max
    # print(float("{:.2f}".format(num)))
    return float("{:.2f}".format(num))


if __name__ == "__main__":
    ligar_lampada(1)
    porcentagem(num_max=100, num=10)
