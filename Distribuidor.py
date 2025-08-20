import random
from Atributos import Atributos

class distribuidorAtributos:
    #dados
    def rolar_3d6(self):
        return sum(random.randint(1, 6) for _ in range(3))  
    def rolar_4d6_descartar_menor(self):
        dados = [random.randint(1, 6) for _ in range(4)]
        dados.remove(min(dados))
        return sum(dados)
    
    #Rolar dado no estilo escolhido, aventureiro e heroico
    def DadoClassico(self):
        return [self.rolar_3d6() for _ in range(6)]
    def DadoHeroico(self):
        return [self.rolar_4d6_descartar_menor() for _ in range(6)]
    
    def EscolhaAventureiro(self):
        dados = self.DadoClassico()
        escolhaAtributos = input(f"\nVocê tirou os dados: {dados}\nEscolha a ordem separada por virgula: " \
        "\nOrdem: [FORÇA, DESTREZA, CONSTITUIÇÃO, INTELIGENCIA, SABEDORIA, CARISMA]\n ")
        valores = [int(x.strip()) for x in escolhaAtributos.split(",")]
        return valores
    def EscolhaHeroico(self):
        dados = self.DadoHeroico()
        escolhaAtributos = input(f"\nVocê tirou os dados: {dados}\nEscolha a ordem separada por virgula: " \
        "\nOrdem: [FORÇA, DESTREZA, CONSTITUIÇÃO, INTELIGENCIA, SABEDORIA, CARISMA]\n ")
        valores = [int(x.strip()) for x in escolhaAtributos.split(",")]
        return valores