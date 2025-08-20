from Distribuidor import distribuidorAtributos
from Personagem import Personagem


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