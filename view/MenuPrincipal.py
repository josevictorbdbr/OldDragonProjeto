from models.Personagem import Personagem
from models.Distribuidor import distribuidorAtributos

def ExibirMenu():
    distribuidor = distribuidorAtributos()

    nome = input("Digite o nome do personagem: ")

    print("Escolha uma raça: (1) Humano / (2) Elfo / (3) Halfling / (4) Anão")
    escolhaRaca = input("Opção: ")
    raca = { "1": "Humano", "2": "Elfo", "3": "Halfling", "4": "Anão" }.get(escolhaRaca, "Humano")

    print("Escolha o estilo: (1) Clássico | (2) Aventureiro | (3) Heroico")
    escolhaEstilo = input("Opção: ")
    estilo = { "1": "classico", "2": "aventureiro", "3": "heroico" }.get(escolhaEstilo, "classico")

    return Personagem(nome, estilo, raca, distribuidor)
