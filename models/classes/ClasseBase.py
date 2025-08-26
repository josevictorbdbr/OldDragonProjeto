import random

class Classe:

    #Status que serão substituida por outras classes
    def __init__(self, nome, equipamento, habilidades, dado_dv):
        self.nome = nome
        self.dado_dv = dado_dv
        self.equipamento = equipamento
        self.habilidades = habilidades
        self.vida = self.rolar_dados() #Rola dados de vida dependendo da classe selecionada

    def rolar_dados(self, dado_dv):
        return random.randint(1, dado_dv)

    def __str__(self):
        return(
            f" ==== Classe: {self.nome} ====\n"
            f" ==== Vida: {self.vida} ====\n"
            f"-- Equipamento: {', '.join(self.equipamento)}\n"
            f"-- Habilidades: {', '.join(self.habilidades)}\n"
        )