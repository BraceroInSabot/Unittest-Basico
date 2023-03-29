

def ligar_lampada(condicao: int) -> str:
    """Define o estado de uma lampada"""
    if condicao == 0:
        print("Luz apagada")
        return "Luz apagada"
    elif condicao == 1:
        print("Luz Acesa")
        return "Luz Acesa"


if __name__ == "__main__":
    user_input = int(input())
