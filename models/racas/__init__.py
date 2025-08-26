from models.racas.Humano import Humano
from models.racas.Elfo import Elfo
from models.racas.Anao import Anao
from models.racas.Gnomo import Gnomo
from models.racas.Halfling import Halfling
from models.racas.MeioElfo import MeioElfo

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