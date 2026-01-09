import json
from naves import criar_naves_iniciais  # Função que cria as 3 naves javardas
from tabuleiro import mostrar_tabuleiro

# Ficheiro onde vamos guardar/carregar o estado do jogo
SAVE_FILE = "save.json"

# Lista global que vai armazenar todas as naves do jogo
naves_jogo = []

# ===================== FUNÇÃO CAPA =====================
def mostrar_capa():
    """
    Mostra uma capa criativa do jogo no terminal com cores e ASCII art.
    """
    # Cores ANSI para texto
    vermelho = "\033[91m"
    verde = "\033[92m"
    azul = "\033[94m"
    amarelo = "\033[93m"
    reset = "\033[0m"

    # ASCII art da nave e título
    print(f"{vermelho}          __/___{reset}")
    print(f"{vermelho}     _____/_______|{reset}")
    print(f"{vermelho} _____/_______|_____|_____{reset}")
    print(f"{vermelho} \\                   < < <{reset}")
    print(f"{azul}  \\      JOGO DE NAVES{reset}")
    print(f"{amarelo}   \\________________________{reset}")

    # Texto de boas-vindas
    print(f"{verde}  ================================================{reset}")
    print(f"{verde}        BEM-VINDO AO JOGO DE NAVES{reset}")
    print(f"{verde}          Crie a sua nave e lute no espaço!{reset}")
    print(f"{verde}  ================================================{reset}\n")
    print(f"{azul}  Use o menu para iniciar, carregar ou guardar o jogo.{reset}\n")

# ===================== FUNÇÃO MENU =====================
def menu():
    """
    Mostra o menu principal do jogo.
    Devolve a opção escolhida pelo utilizador como string.
    """
    print("\nMENU PRINCIPAL:")
    print("1 - Iniciar Jogo")
    print("2 - Carregar Jogo")
    print("3 - Guardar Jogo")
    print("4 - Sair")
    return input("Escolha uma opção: ")

# ===================== FUNÇÃO INICIAR =====================
def iniciar_jogo():
    global naves_jogo
    print("\nA criar novas naves...")

    # Criar as três naves javardas
    naves_jogo = criar_naves_iniciais()

    print("Naves criadas com sucesso!\n")

    # Mostrar dados de cada nave (nome, energia, símbolo) com cores
    for nave in naves_jogo:
        nave.mostrar_dados()
        
    # Mostrar o tabuleiro com as naves
    mostrar_tabuleiro(naves_jogo)

# ===================== FUNÇÃO GUARDAR =====================

def guardar_jogo():
    """
    Guarda todas as naves e atributos num ficheiro JSON.
    Permite carregar o jogo mais tarde no mesmo estado.
    """
    global naves_jogo

    save_data = []
    for nave in naves_jogo:
        save_data.append({
            "nome": nave.nome,
            "cor": nave.cor,
            "energia": nave.energia,
            "perda_energia": nave.perda_energia,
            "simbolo": nave.simbolo,
            "energia_extra": getattr(nave, "energia_extra", 0)
        })

    # Escreve os dados no ficheiro JSON
    with open(SAVE_FILE, "w") as f:
        json.dump(save_data, f, indent=2)

    print("Jogo guardado com sucesso!")

# ===================== FUNÇÃO CARREGAR =====================
def carregar_jogo():
    """
    Carrega o estado do jogo a partir do ficheiro JSON.
    Se o ficheiro não existir, avisa o utilizador.
    """
    global naves_jogo
    try:
        # Lê os dados do ficheiro
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        naves_jogo = []

        # Recria as naves a partir dos dados guardados
        for n in data:
            # Criar nave com base em NaveEspecial
            from naves import NaveEspecial
            nave = NaveEspecial(
                nome=n["nome"],
                cor=n["cor"],
                perda_energia=n["perda_energia"],
                simbolo=n["simbolo"],
                energia_extra=n.get("energia_extra", 0)
            )
            # Mantém a energia atual
            nave.energia = n["energia"]

            naves_jogo.append(nave)

        print("Jogo carregado com sucesso!\n")

        # Mostra os dados das naves carregadas
        for nave in naves_jogo:
            nave.mostrar_dados()

    except FileNotFoundError:
        print("Nenhum jogo guardado encontrado.")

    # Mostrar o tabuleiro com as naves carregadas
        mostrar_tabuleiro(naves_jogo)

def jogar():
    """
    Loop principal do jogo.
    Permite disparar até uma nave ficar sem energia.
    """
    global naves_jogo

    if not naves_jogo:
        print("Não existem naves. Inicia o jogo primeiro!")
        return

    tiros = 0

    while True:
        print("\n--- AÇÃO DO JOGO ---")
        print("1 - Disparar")
        print("2 - Voltar ao menu")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Nave 0 ataca nave 1 (simples e aceitável para trabalho)
            atacante = naves_jogo[0]
            alvo = naves_jogo[1]

            print(f"\n{atacante.nome} disparou contra {alvo.nome}!")
            alvo.sofrer_dano()
            tiros += 1

            # Mostrar estado das naves
            for nave in naves_jogo:
                nave.mostrar_dados()

            # Verificar fim de jogo
            if alvo.energia == 0:
                print(f"\n💥 {alvo.nome} foi destruída!")
                print(f"Tiros efetuados: {tiros}")
                break

        elif opcao == "2":
            print("A voltar ao menu principal...")
            break
        else:
            print("Opção inválida!")

# ===================== FUNÇÃO MAIN =====================
def main():
    """
    Função principal do jogo.
    Mostra a capa e entra no ciclo do menu principal.
    """
    mostrar_capa()

    while True:
        opcao = menu()
        
        if opcao == "1":
        iniciar_jogo()
        jogar()
        elif opcao == "2":
            carregar_jogo()
        elif opcao == "3":
            guardar_jogo()
        elif opcao == "4":
            print("A sair do jogo. Até à próxima!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# ===================== EXECUÇÃO =====================
if __name__ == "__main__":
    main()