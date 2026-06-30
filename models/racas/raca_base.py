class Raca:

    #Status que serão substituidos em cada raça
    def __init__(self, nome, movimento, infravisao, alinhamento, habilidades):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = habilidades
    
    def __str__(self):
        return (
            f"==== Raça: {self.nome} ====\n"
            f"-- Movimento: {self.movimento}\n"
            f"-- Infravisão: {self.infravisao}\n"
            f"-- Alinhamento: {self.alinhamento}\n"
            f"-- Habilidades: {', '.join(self.habilidades)}\n"
        )