from flask import Flask, render_template, request, session
from models.Personagem import Personagem
from models.Distribuidor import DistribuidorAtributos
from models.racas import raca_escolha
from models.classes import classe_escolha

app = Flask(__name__)
app.secret_key = "segredo" 


@app.route("/", methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        nome = request.form["nome"]
        estilo = request.form["estilo"]

        #Armazena os dados basicos do personagem na sessão
        session["personagem_base"] = {
            "nome": nome,
            "raca_id": request.form["raca"],
            "classe_id": request.form["classe"],
            "estilo": estilo,
        }

        distribuidor = DistribuidorAtributos()

        if estilo == "classico":
            raca = raca_escolha(session["personagem_base"]["raca_id"])
            classe = classe_escolha(session["personagem_base"]["classe_id"])
            personagem = Personagem(nome, estilo, raca, classe, distribuidor)
            return render_template("Ficha.html", personagem=personagem)

        elif estilo in ["aventureiro", "heroico"]:
            dados = distribuidor.escolha_aventureiro() if estilo == "aventureiro" else distribuidor.escolha_heroico()
            session["dados"] = dados
            return render_template("Distruibuir.html", dados=dados)

    return render_template("Menu.html")


@app.route("/distribuir", methods=["POST"])
def distribuir():
    distribuidor = DistribuidorAtributos()
    dados = session.get("dados")
    personagem_base = session.get("personagem_base")

    #Pega raça e classe escolhidas pelo usuario
    raca = raca_escolha(personagem_base["raca_id"])
    classe = classe_escolha(personagem_base["classe_id"])

    #Pega atributos escolhidos pelo usuario
    escolha = request.form
    valores = distribuidor.escolha_personalizada(dados, escolha)

    personagem = Personagem(
        personagem_base["nome"],
        personagem_base["estilo"],
        raca,
        classe,
        distribuidor,
        atributos=valores
    )

    return render_template("Ficha.html", personagem=personagem)


if __name__ == "__main__":
    app.run(debug=True)
