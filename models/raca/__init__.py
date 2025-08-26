from models.raca.Humano import Humano
from models.raca.Elfo import Elfo
from models.raca.Anao import Anao
from models.raca.Gnomo import Gnomo
from models.raca.Halfling import Halfling
from models.raca.MeioElfo import MeioElfo

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
            print("Numero sem classe, escolhendo humano por padrão")
            return Humano()