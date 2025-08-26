from models.Personagem import Personagem
from models.Distribuidor import DistribuidorAtributos
from models.racas import raca_escolha
from models.classes import classe_escolha

def exibir_menu():
    distribuidor = DistribuidorAtributos()

    nome = input("Digite o nome do personagem: ")

    #escolha de raca
    print("Escolha uma raça: (1) Humano / (2) Elfo / (3) Halfling / (4) Anão / (5) Gnomo / (6) Meio-Elfo")
    raca = raca_escolha(input("Opção: "))

    print("Escolha uma classe: (1) Guerreiro / (2) Mago / (3) Ranger")
    classe = classe_escolha(input("Opção: "))

    #escolha de estilo
    print("Escolha o estilo: (1) Clássico | (2) Aventureiro | (3) Heroico")
    escolha_estilo = input("Opção: ")
    estilo = { "1": "classico", "2": "aventureiro", "3": "heroico" }.get(escolha_estilo, "classico")

    return Personagem(nome, estilo, raca, classe, distribuidor)
