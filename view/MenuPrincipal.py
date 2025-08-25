from models.Personagem import Personagem
from models.Distribuidor import distribuidorAtributos
from models.raca import RacaEscolha

def ExibirMenu():
    distribuidor = distribuidorAtributos()

    nome = input("Digite o nome do personagem: ")

    #escolha de raca
    print("Escolha uma raça: (1) Humano / (2) Elfo / (3) Halfling / (4) Anão / (5) Gnomo / (6) Meio-Elfo")
    raca = RacaEscolha(input("Opção: "))

    #escolha de estilo
    print("Escolha o estilo: (1) Clássico | (2) Aventureiro | (3) Heroico")
    escolhaEstilo = input("Opção: ")
    estilo = { "1": "classico", "2": "aventureiro", "3": "heroico" }.get(escolhaEstilo, "classico")

    return Personagem(nome, estilo, raca, distribuidor)
