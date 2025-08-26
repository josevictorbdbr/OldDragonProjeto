from models.classes.ClasseBase import Classe

class Guerreiro(Classe):
    def __init__(self):
        super().__init__(
            nome= "Guerreiro",
            dado_dv= 10, 
            equipamento= ["Qualquer arma", "Qualquer armadura", "NÃO pode usar Cajados, Varinhas e Pergaminhos"],
            habilidades= ["Aparar", "Ataque Extra", "Maestria em Arma"]
        )