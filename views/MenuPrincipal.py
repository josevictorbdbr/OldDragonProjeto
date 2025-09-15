from models.Personagem import Personagem
from models.Distribuidor import DistribuidorAtributos
from models.racas import raca_escolha
from models.classes import classe_escolha

def exibir_menu(nome, escolha_raca, escolha_classe, escolha_estilo):
    distribuidor = DistribuidorAtributos()

    raca = raca_escolha(escolha_raca)
    classe = classe_escolha(escolha_classe)
    estilo = { "1": "classico", "2": "aventureiro", "3": "heroico" }.get(escolha_estilo, "classico")

    return Personagem(nome, estilo, raca, classe, distribuidor)
