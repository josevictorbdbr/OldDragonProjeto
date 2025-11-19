from models.Atributos import Atributos

class Personagem:
    
    def __init__(self, nome, estilo_dist, raca, classe, distribuidor, atributos=None):
        self.nome = nome
        self.estilo_dist = estilo_dist
        self.raca = raca
        self.classe = classe

        if atributos is None:
            self.atributos = self.definir_atributos(distribuidor)
        else:
            #Garante que atributos seja um objeto Atributos
            if isinstance(atributos, Atributos):
                self.atributos = atributos
            else:
                self.atributos = Atributos(*atributos)

    #Define os atributos do personagem conforme o estilo de distribuição escolhido
    def definir_atributos(self, distribuidor):
        if self.estilo_dist == "classico":
            valores = distribuidor.dado_classico()
            return Atributos(*valores)
        elif self.estilo_dist == "aventureiro":
            return Atributos(*distribuidor.escolha_aventureiro())
        elif self.estilo_dist == "heroico":
            return Atributos(*distribuidor.escolha_heroico())
    
    def exibir_ficha(self):
        return (
            f"\n ==== Personagem: {self.nome} ==== \n"
            f"==== Estilo de jogo: {self.estilo_dist} ====\n"
            f"{self.raca}\n"
            f"{self.classe}\n"
            f"{self.atributos}\n"
            "===============================\n"
        )

    #Converte o objeto em dicionário pronto para JSON
    def to_dict(self) -> dict:
        def conv(v):
            #Se o objeto tem to_dict, usa
            if hasattr(v, "to_dict") and callable(getattr(v, "to_dict")):
                return v.to_dict()
            #Se tem __dict__, converte recursivamente e marca a classe
            if hasattr(v, "__dict__"):
                d = {k: conv(val) for k, val in v.__dict__.items()}
                d["__class_name__"] = v.__class__.__name__
                return d
            #Listas e dicionários
            if isinstance(v, list):
                return [conv(i) for i in v]
            if isinstance(v, dict):
                return {k: conv(val) for k, val in v.items()}
            return v

        return {k: conv(v) for k, v in self.__dict__.items()}

    #Reconstrói Personagem 
    @classmethod
    def from_dict(cls, data: dict):
        #Reconstruir atributos
        attrs = data.get("atributos")
        if isinstance(attrs, dict):
            atributos = Atributos(
                forca=attrs.get("forca", 0),
                destreza=attrs.get("destreza", 0),
                constituicao=attrs.get("constituicao", 0),
                inteligencia=attrs.get("inteligencia", 0),
                sabedoria=attrs.get("sabedoria", 0),
                carisma=attrs.get("carisma", 0),
            )
        else:
            atributos = attrs

        #Reconstruir raca
        raca_data = data.get("raca")
        raca_obj = raca_data
        if isinstance(raca_data, dict):
            try:
                from models.racas.Humano import Humano
                from models.racas.Elfo import Elfo
                from models.racas.Anao import Anao
                from models.racas.Gnomo import Gnomo
                from models.racas.Halfling import Halfling
                from models.racas.MeioElfo import MeioElfo

                raca_map = {
                    "Humano": Humano,
                    "Elfo": Elfo,
                    "Anao": Anao,
                    "Gnomo": Gnomo,
                    "Halfling": Halfling,
                    "MeioElfo": MeioElfo,
                }
                raca_cls_name = raca_data.get("__class_name__")
                if raca_cls_name and raca_cls_name in raca_map:
                    raca_obj = raca_map[raca_cls_name]()
                    raca_obj.__dict__.update({k: v for k, v in raca_data.items() if k != "__class_name__"})
                else:
                    raca_obj = raca_data
            except Exception:
                raca_obj = raca_data

        #Reconstruir classe
        classe_data = data.get("classe")
        classe_obj = classe_data
        if isinstance(classe_data, dict):
            try:
                from models.classes.Guerreiro import Guerreiro
                from models.classes.Mago import Mago
                from models.classes.Ranger import Ranger

                classe_map = {
                    "Guerreiro": Guerreiro,
                    "Mago": Mago,
                    "Ranger": Ranger,
                }
                classe_cls_name = classe_data.get("__class_name__")
                if classe_cls_name and classe_cls_name in classe_map:
                    classe_obj = classe_map[classe_cls_name]()
                    classe_obj.__dict__.update({k: v for k, v in classe_data.items() if k != "__class_name__"})
                else:
                    classe_obj = classe_data
            except Exception:
                classe_obj = classe_data

        #Cria instância final
        personagem = cls(
            data.get("nome"),
            data.get("estilo_dist"),
            raca_obj,
            classe_obj,
            distribuidor=None,
            atributos=atributos
        )
        return personagem