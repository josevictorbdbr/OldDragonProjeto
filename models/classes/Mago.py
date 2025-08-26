from models.classes.ClasseBase import Classe

class Mago(Classe):
    def __init__(self):
        super().__init__(
            nome= "Mago",
            dado_dv= 4, 
            equipamento= ["APENAS armas pequenas", "NÃO pode usar armadura", "Qualquer Item Magico"],
            habilidades= ["Magias Arcanas", "Ler Magias", "Detectar Magias"]
        )