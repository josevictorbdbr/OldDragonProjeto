from models.racas.humano import Humano
from models.racas.elfo import Elfo
from models.racas.anao import Anao
from models.racas.gnomo import Gnomo
from models.racas.halfling import Halfling
from models.racas.meio_elfo import MeioElfo

#função para escolher as habilidades de acordo com a raça escolhida
def raca_escolha(escolha: str):
        if escolha == "1":
            return Humano()
        elif escolha == "2":
            return Elfo()
        elif escolha == "3":
            return Halfling()
        elif escolha == "4":
            return Anao()
        elif escolha == "5":
            return Gnomo()
        elif escolha == "6":
            return MeioElfo()
        else:
            print("Numero sem raca definida, escolhendo humano por padrão")
            return Humano()