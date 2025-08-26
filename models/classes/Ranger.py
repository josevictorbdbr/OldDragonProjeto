from models.classes.ClasseBase import Classe

class Ranger(Classe):
    def __init__(self):
        super().__init__(
            nome= "Ranger",
            dado_dv= 6, 
            equipamento= ["APENAS armas leves ou medias", "APENAS armaduras leves", "Não pode usar Cajados, Varinhas e Pergaminhos"],
            habilidades= ["Inimigo Mortal", "Combativo", "Companheiro Animal"]
        )