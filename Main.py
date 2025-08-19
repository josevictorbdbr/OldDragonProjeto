import random

class Atributos:
    def __init__(self, forca=0, destreza=0, constituicao=0, inteligencia=0, sabedoria=0, carisma=0):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
    
    def __str__(self):
        return (f"FORÇA: {self.forca} / DESTREZA: {self.destreza} / CONSTITUIÇÃO: {self.constituicao}\n"
                f"INTELIGENCIA: {self.inteligencia} / SABEDORIA: {self.sabedoria} / CARISMA: {self.carisma}" )

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


class Personagem:
    def __init__(self, nome, estiloDist, estiloRaca, distribuidor: distribuidorAtributos):
        self.nome = nome
        self.estiloDist = estiloDist
        self.estiloRaca = estiloRaca
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
        print(f"\n ==== Personagem: {self.nome} / {self.estiloRaca} ==== ")
        print(f" =Modo: {self.estiloDist}= ")
        print(self.atributos)

def main():
    distribuidor = distribuidorAtributos()
    
    nome = input("Digite o nome do personagem: ")

    #Pergunta ao usuario e transforma a escolha que foi usado numeros para uma string
    print("Escolha uma raça para esse personagem: ")
    print("(1) Humano / (2) Elfo / (3) Halfling / (4) Anão")
    escolhaRaca = input("Opção: ")
    estiloRaca = { "1": "Humano", "2": "Elfo", "3": "Halfling", "4": "Anão" }.get(escolhaRaca, "Humano")

    print("Escolha o estilo de distribuição: (1) Clássico | (2) Aventureiro | (3) Heroico")
    escolhaDis = input("Opção: ")
    estiloDist = { "1": "classico", "2": "aventureiro", "3": "heroico" }.get(escolhaDis, "classico")

    #Cria o personagem com base nas escolhas do usuario e exibe a ficha
    personagem = Personagem(nome, estiloDist, estiloRaca, distribuidor)
    personagem.exibirFicha()

main()
