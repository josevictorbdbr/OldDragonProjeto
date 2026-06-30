from models.racas.raca_base import Raca

class MeioElfo(Raca):
    def __init__(self):
        super().__init__(
            nome= "Meio Elfo",
            movimento= 9, 
            infravisao= 9, 
            alinhamento= "Caos",
            habilidades= ["Aprendizado", "Gracioso e Vigoroso", "idioma extra","Imunidades"]
        )