from models.racas.RacaBase import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__(
            nome= "Humano",
            movimento= 9, 
            infravisao= 0, 
            alinhamento= "Qualquer",
            habilidades= ["Aprendizado", "Adaptabilidade"]
            )