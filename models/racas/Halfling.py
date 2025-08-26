from models.racas.RacaBase import Raca

class Halfling(Raca):
    def __init__(self):
        super().__init__(
            nome= "Halfling",
            movimento= 6, 
            infravisao= 0, 
            alinhamento= "Neutro",
            habilidades= [" Destemidos", "Bons de Mira", "Pequenos", "Furtivo", "Restriçoes"]
        )