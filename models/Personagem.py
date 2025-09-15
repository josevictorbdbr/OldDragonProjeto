from models.Atributos import Atributos

class Personagem:
    
    def __init__(self, nome, estilo_dist, raca, classe, distribuidor, atributos=None):
        self.nome = nome
        self.estilo_dist = estilo_dist
        self.raca = raca
        self.classe = classe

        if atributos is None:
            self.atributos = self.definir_atributos(distribuidor)
        else:
            #Garante que atributos seja um objeto Atributos
            if isinstance(atributos, Atributos):
                self.atributos = atributos
            else:
                self.atributos = Atributos(*atributos)

    # Define os atributos do personagem conforme o estilo de distribuição escolhido
    def definir_atributos(self, distribuidor):
        if self.estilo_dist == "classico":
            valores = distribuidor.dado_classico()
            return Atributos(*valores)
        elif self.estilo_dist == "aventureiro":
            return Atributos(*distribuidor.escolha_aventureiro())
        elif self.estilo_dist == "heroico":
            return Atributos(*distribuidor.escolha_heroico())
    
    def exibir_ficha(self):
        return (
            f"\n ==== Personagem: {self.nome} ==== \n"
            f"==== Estilo de jogo: {self.estilo_dist} ====\n"
            f"{self.raca}\n"
            f"{self.classe}\n"
            f"{self.atributos}\n"
            "===============================\n"
        )
