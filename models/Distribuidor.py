import random

class DistribuidorAtributos:

    #Dados d6
    def rolar_3d6(self):
        return sum(random.randint(1, 6) for _ in range(3)) 
    def rolar_4d6_descartar_menor(self):
        dados = [random.randint(1, 6) for _ in range(4)]
        dados.remove(min(dados))
        return sum(dados)
    
    #Rolar dado no estilo escolhido, aventureiro e heroico
    def dado_classico(self):
        return [self.rolar_3d6() for _ in range(6)]
    
    def dado_heroico(self):
        return [self.rolar_4d6_descartar_menor() for _ in range(6)]
    
    def escolha_aventureiro(self):
        dados = self.dado_classico()
        escolha_atributos = input(
            f"\nVocê tirou os dados: {dados}\n"
            f"Ordem: [FORÇA, DESTREZA, CONSTITUIÇÃO, INTELIGENCIA, SABEDORIA, CARISMA]\n"
            f"Digite um dos numeros tirados para cada atributo, separados por virgula e baseando-se na ordem acima: ")
        valores = [int(x.strip()) for x in escolha_atributos.split(",")]
        return valores
    
    def escolha_heroico(self):
        dados = self.dado_heroico()
        escolha_atributos = input(
            f"\nVocê tirou os dados: {dados}\n"
            f"Ordem: [FORÇA, DESTREZA, CONSTITUIÇÃO, INTELIGENCIA, SABEDORIA, CARISMA]\n"
            f"Digite um dos numeros tirados para cada atributo, separados por virgula e baseando-se na ordem acima: ")
        valores = [int(x.strip()) for x in escolha_atributos.split(",")]
        return valores