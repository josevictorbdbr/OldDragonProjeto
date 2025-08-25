from models.Atributos import Atributos


class Personagem:
    def __init__(self, nome, estiloDist, raca, distribuidor):
        self.nome = nome
        self.estiloDist = estiloDist
        self.raca = raca
        self.atributos = self.definirAtributos(distribuidor)

    #Usa a escolha de estilo para a distribuicao de atributos
    def definirAtributos(self, distribuidor):
        if self.estiloDist == "classico":
            valores = distribuidor.DadoClassico()
            return Atributos(*valores)
        elif self.estiloDist == "aventureiro":
            valores = distribuidor.EscolhaAventureiro()
            return Atributos(*valores)
        elif self.estiloDist == "heroico":
            valores = distribuidor.EscolhaHeroico()
            return Atributos(*valores)
    
    def exibirFicha(self):
        print(f"\n ==== Personagem: {self.nome} ==== ")
        print(f"==== Estilo de jogo: {self.estiloDist} ==== ")
        print(self.raca)
        print(self.atributos)
        print("\n===============================")