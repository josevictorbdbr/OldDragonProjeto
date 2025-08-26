from models.Atributos import Atributos


class Personagem:

    def __init__(self, nome, estilo_dist, raca, distribuidor):
        self.nome = nome
        self.estilo_dist = estilo_dist
        self.raca = raca
        self.atributos = self.definir_atributos(distribuidor)

    #Usa a escolha de estilo para a distribuicao de atributos
    def definir_atributos(self, distribuidor):
        if self.estilo_dist == "classico":
            valores = distribuidor.dado_classico()
            return Atributos(*valores)
        elif self.estilo_dist == "aventureiro":
            valores = distribuidor.escolha_aventureiro()
            return Atributos(*valores)
        elif self.estilo_dist == "heroico":
            valores = distribuidor.escolha_heroico()
            return Atributos(*valores)
    
    def exibir_ficha(self):
        print(f"\n ==== Personagem: {self.nome} ==== ")
        print(f"==== Estilo de jogo: {self.estilo_dist} ==== ")
        print(self.raca)
        print(self.atributos)
        print("\n===============================")