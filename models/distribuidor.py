import random

class DistribuidorAtributos:

    #Dados
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
    
    #Pega a escolha de estilo para os dados
    def escolha_aventureiro(self):
        return self.dado_classico()

    def escolha_heroico(self):
        return self.dado_heroico()
    
    #Usuario faz a escolha de onde colocar os atributos
    def escolha_personalizada(self, dados, escolha):
        valores = [
            int(escolha["forca"]),
            int(escolha["destreza"]),
            int(escolha["constituicao"]),
            int(escolha["inteligencia"]),
            int(escolha["sabedoria"]),
            int(escolha["carisma"])
        ]
        return valores
