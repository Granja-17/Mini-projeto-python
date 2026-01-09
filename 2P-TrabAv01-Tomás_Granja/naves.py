class NaveModelo:
    """
    Classe base que representa uma nave genérica.
    Esta classe contém os atributos e funcionalidades comuns a todas as naves.
    """

    def __init__(self, nome: str, cor: str, perda_energia: int, simbolo: str):
        # Nome da nave
        self.nome = nome
        # Cor da nave (texto que será usado para apresentar informações coloridas)
        self.cor = cor
        # Energia inicial fixa de 100 (não pode começar com outro valor)
        self.energia = 100
        # A quantidade de energia que a nave perde num evento
        self.perda_energia = perda_energia      
        # O símbolo que representa a nave (ex.: letra, emoji, etc.)
        self.simbolo = simbolo

    def energia_atual(self): # Método que devolve a energia atual da nave após perdas.
        return self.energia

    def sofrer_dano(self): #Reduz a energia da nave de acordo com a perda de energia definida. A energia nunca pode ser inferior a 0.
        self.energia -= self.perda_energia
        if self.energia < 0:
            self.energia = 0

class NaveEspecial(NaveModelo): #Classe que herda da NaveModelo e adiciona um novo atributo: energia extra.
    def __init__(self, nome: str, cor: str, perda_energia: int, simbolo: str, energia_extra: int):
        # Aproveita o construtor da classe pai (NaveModelo)
        super().__init__(nome, cor, perda_energia, simbolo)
        # Novo atributo exclusivo desta classe
        self.energia_extra = energia_extra

    # Para mostrar texto com cor no terminal (cores ANSI)
    CORES = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "magenta": "\033[95m",
        "ciano": "\033[96m",
        "reset": "\033[0m"
    }

    def mostrar_dados(self):
        """
        Mostra os dados da nave:
        - Nome
        - Energia atual
        - Símbolo
        O texto deve aparecer na cor definida na nave.
        """
        cor = self.CORES.get(self.cor.lower(), self.CORES["reset"])

        print(cor + f"Nave: {self.nome}")
        print(f"Energia atual: {self.energia}")
        print(f"Símbolo: {self.simbolo}" + self.CORES["reset"])

    def adicionar_energia(self):
        """
        Adiciona a energia extra à energia atual.
        Deve garantir que a energia nunca ultrapassa o máximo (100).
        """

        self.energia += self.energia_extra
        # Garante que não ultrapassa o limite máximo
        if self.energia > 100:
            self.energia = 100

def criar_naves_iniciais():
    # Nomes
    nave1 = NaveEspecial("Mister.Colhão", "vermelho", perda_energia=12, simbolo="M", energia_extra=25)
    nave2 = NaveEspecial("Senhor.Ratão", "azul", perda_energia=15, simbolo="S", energia_extra=20)
    nave3 = NaveEspecial("Capitão Fofinho", "verde", perda_energia=10, simbolo="C", energia_extra=30)
    
    return [nave1, nave2, nave3]
