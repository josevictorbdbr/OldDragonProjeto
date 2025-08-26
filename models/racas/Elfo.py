from models.racas.RacaBase import Raca

class Elfo(Raca):
    def __init__(self):
        super().__init__(
            nome= "Elfo",
            movimento= 9, 
            infravisao= 18,
            alinhamento= "Neutro",
            habilidades= ["Graciosos", "Arma Racial", "Treinamento Racial", "Imunidades"]
        )