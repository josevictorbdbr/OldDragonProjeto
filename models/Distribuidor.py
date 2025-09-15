import random

class DistribuidorAtributos:

    #Dados d6
    def rolar_3d6(self):
        return sum(random.randint(1, 6) for _ in range(3))
    def rolar_4d6_descartar_menor(self):
        dados = [random.randint(1, 6) for _ in range(4)]
        dados.remove(min(dados))
        return sum(dados)

    def dado_classico(self):
        return [self.rolar_3d6() for _ in range(6)]
    def dado_heroico(self):
        return [self.rolar_4d6_descartar_menor() for _ in range(6)]
    
    #Pega a escolha de estilo, roda os dados e manda para escolha personalizada
    def escolha_aventureiro(self):
        dados = self.dado_classico()
        return self.escolha_personalizada(dados)
    def escolha_heroico(self):
        dados = self.dado_heroico()
        return self.escolha_personalizada(dados)
    
    #Usuario faz a escolha de onde colocar atributos caso seja estilo heroico ou aventureiro
    def escolha_personalizada(self, dados, escolha):
        valores = [int(x.strip()) for x in escolha.split(",")]
        return valores
    