import json
import os
import re

#Sanitiza nomes de arquivos
_filename_sanitize_re = re.compile(r"[^\w\-_. ]", re.UNICODE)

def _sanitize_filename(name: str) -> str:
    name = str(name).strip()
    name = _filename_sanitize_re.sub("_", name)
    return name or "personagem"

#Serialização recursiva simples
def _serialize(obj):
    if obj is None or isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, list):
        return [_serialize(i) for i in obj]
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    #Se tem to_dict, usa
    if hasattr(obj, "to_dict") and callable(getattr(obj, "to_dict")):
        return _serialize(obj.to_dict())
    #Se tem __dict__, converte recursivamente
    if hasattr(obj, "__dict__"):
        return {k: _serialize(v) for k, v in obj.__dict__.items()}
    return str(obj)

#Salva personagem em JSON, retorna caminho do arquivo gravado
def save_personagem(personagem, path=None):
    if path is None:
        nome = getattr(personagem, "nome", "personagem")
        filename = f"{_sanitize_filename(nome)}.json"
        path = os.path.join("saves", filename)

    #Cria pasta se preciso
    os.makedirs(os.path.dirname(path), exist_ok=True)

    #Usa to_dict se disponível
    data = personagem.to_dict() if hasattr(personagem, "to_dict") else _serialize(personagem)

    #Grava JSON 
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return path

#Carrega personagem
def load_personagem(cls, path="saves/personagem.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    #Se a classe implementar from_dict, usa
    if hasattr(cls, "from_dict") and callable(getattr(cls, "from_dict")):
        return cls.from_dict(data)

    #Tenta criar objeto diretamente
    try:
        return cls(**data)
    except Exception:
        #Cria objeto vazio e popula __dict__
        obj = cls.__new__(cls)
        if isinstance(data, dict):
            obj.__dict__.update(data)
        return obj