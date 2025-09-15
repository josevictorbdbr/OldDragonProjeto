from flask import Flask, render_template, request, redirect, url_for
from models.Personagem import Personagem
from models.Distribuidor import DistribuidorAtributos
from models.racas import raca_escolha
from models.classes import classe_escolha

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        nome = request.form["nome"]
        raca = raca_escolha(request.form["raca"])
        classe = classe_escolha(request.form["classe"])
        estilo = request.form["estilo"]
        distribuidor = DistribuidorAtributos()
        personagem = Personagem(nome, estilo, raca, classe, distribuidor)
        # Salva o personagem na sessão ou passa para o template
        return render_template("ficha.html", personagem=personagem)
    return render_template("menu.html")

if __name__ == "__main__":
    app.run(debug=True)