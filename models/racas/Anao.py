from models.racas.raca_base import Raca

class Anao(Raca):
    def __init__(self):
        super().__init__(
            nome= "Anáo",
            movimento= 6, 
            infravisao= 18, 
            alinhamento= "Ordem",
            habilidades= ["Mineradores", "Vigoroso", "Armas grandes", "Inimigos"]
        )
