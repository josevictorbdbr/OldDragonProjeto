class Atributos:
    def __init__(self, forca=0, destreza=0, constituicao=0, inteligencia=0, sabedoria=0, carisma=0):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
    
    def __str__(self):
        return (f"FORÇA: {self.forca} / DESTREZA: {self.destreza} / CONSTITUIÇÃO: {self.constituicao}\n"
                f"INTELIGENCIA: {self.inteligencia} / SABEDORIA: {self.sabedoria} / CARISMA: {self.carisma}" )