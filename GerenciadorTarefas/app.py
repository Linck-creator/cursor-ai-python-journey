from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

tarefas = []
proximo_id = 1

ARQUIVO_DADOS = "tarefas.json"


def salvar_dados():
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(
            {
                "proximo_id": proximo_id,
                "tarefas": tarefas
            },
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def carregar_dados():
    global tarefas
    global proximo_id

    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            try:
                dados = json.load(arquivo)
                tarefas = dados.get("tarefas", [])
                proximo_id = dados.get("proximo_id", 1)
            except:
                tarefas = []
                proximo_id = 1


def adicionar_tarefa(texto):
    global proximo_id

    tarefas.append(
        {
            "id": proximo_id,
            "texto": texto,
            "feito": False
        }
    )

    proximo_id += 1
    salvar_dados()


def completar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["feito"] = True
            break

    salvar_dados()


def excluir_tarefa(id):
    global tarefas

    tarefas = [t for t in tarefas if t["id"] != id]

    salvar_dados()


@app.route("/")
def index():
    pendentes = [t for t in tarefas if not t["feito"]]
    concluidas = [t for t in tarefas if t["feito"]]

    return render_template(
        "index.html",
        pendentes=pendentes,
        concluidas=concluidas,
        total=len(tarefas)
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():
    texto = request.form.get("texto_tarefa")

    if texto:
        adicionar_tarefa(texto)

    return redirect("/")


@app.route("/completar/<int:id>")
def completar(id):
    completar_tarefa(id)
    return redirect("/")


@app.route("/excluir/<int:id>")
def excluir(id):
    excluir_tarefa(id)
    return redirect("/")


carregar_dados()

if __name__ == "__main__":
    app.run(debug=True)