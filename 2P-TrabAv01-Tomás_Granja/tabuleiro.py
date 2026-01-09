# tabuleiro.py
# Responsável por mostrar o tabuleiro do jogo no ecrã

def mostrar_tabuleiro(naves):
    """
    Mostra um tabuleiro simples com as naves.
    Cada nave é representada pelo seu símbolo.
    """

    print("\nTABULEIRO DE JOGO")
    print("=================")

    # Criar um tabuleiro simples 3x3
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    # Colocar cada nave numa posição fixa
    for i, nave in enumerate(naves):
        if i < 3:
            tabuleiro[i][i] = nave.simbolo

    # Mostrar o tabuleiro no ecrã
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("---------")
