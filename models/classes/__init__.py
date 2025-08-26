from models.classes.Guerreiro import Guerreiro
from models.classes.Mago import Mago
from models.classes.Ranger import Ranger

#função para escolher as habilidades de acordo com a classe escolhida
def classe_escolha(escolha: str):
        if escolha == "1":
            return Guerreiro()
        elif escolha == "2":
            return Mago()
        elif escolha == "3":
            return Ranger()
        else:
            print("Numero sem classe definida, escolhendo guerreiro por padrão")
            return Guerreiro()