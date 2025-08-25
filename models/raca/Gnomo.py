from models.raca.Base import Raca

class Gnomo(Raca):
    def __init__(self):
        super().__init__(
            nome= "Gnomo",
            movimento= 6, 
            infravisao= 18, 
            alinhamento= "Neutro",
            habilidades= ["Avaliadores", "Sagazes e Vigorosos", "Restrições"]
        )