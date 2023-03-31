from typing import Union


def ligar_lampada(condicao: int) -> Union[str, bool]:
    """
    Define o estado de uma lampada

    OBS. ACEITA APENAS 1 E 0 (int)

    :param:
    condicao: int -> estado da lampada (0 ou 1)
    """
    if type(condicao) != int or condicao not in [0, 1]:
        return "Por favor, insira apenas 1 ou 0"

    if condicao == 0:
        # print("Luz apagada")
        return False
    elif condicao == 1:
        # print("Luz Acesa")
        return True


def porcentagem(
    num_max: Union[float, int],
    num: Union[float, int],
) -> Union[float, int]:
    """
    Retorna a o valor da porcentagem de num% de num_max (100%)

    num_max -- 100%
    num -- ?

    :param:
    num_max: float -> indica o 100% de um valor
    num: float -> indica a uma porcentagem
    """
    if type(num) not in [float, int] or type(num_max) not in [float, int]:
        print(
            f"Erro, por favor passe um valor válido. \nnum_max: {num_max} - {type(num_max)}\nnum: {num} - {type(num)}"
        )
        return False

    num = (num / 100) * num_max
    # print(float("{:.2f}".format(num)))
    return float("{:.2f}".format(num))


def ligar_carro(rodas: int = 4, motor: bool = False, trancado: bool = True) -> bool:
    """
    Simula uma pessoa ao entrar em um carro, ele precisa estar destrancado e com o motor ligado para dar partida.

    :param:
    rodas: int -> quantas rodas o carro possui
    motor: bool -> estado do motor, ligado ou desligado
    trancado: bool -> estado das fechaduras do carro, trancadas ou destrancadas
    """
    if (
        rodas >= 4
        and type(rodas) in [int]
        and type(motor) in [bool]
        and type(trancado) in [bool]
    ):
        if not trancado and motor:
            print("vrum vrum")
            return True
        elif trancado and motor:
            print("precisa destrancar")
            return False
        elif trancado or motor:
            print("onde estão as chaves? na ignição ou no seu bolso?")
            return False
    elif type(rodas) in [float]:
        print("O valor de rodas precisa ser decimal")
        return False

    print("O carro precisa das suas rodas para andar")
    return False


if __name__ == "__main__":
    ligar_lampada(1)
    porcentagem(num_max=100, num=10)
    ligar_carro(motor=True, trancado=False)
