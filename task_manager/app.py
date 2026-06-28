from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

tarefas = []
proximo_id = 1

ARQUIVO_DADOS = "tarefas.json"


def salvar_dados():
    global tarefas, proximo_id

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
    global tarefas, proximo_id

    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            try:
                dados = json.load(arquivo)

                tarefas = dados.get("tarefas", [])
                proximo_id = dados.get("proximo_id", 1)

            except Exception:
                tarefas = []
                proximo_id = 1
    else:
        tarefas = []
        proximo_id = 1


def adicionar_tarefa(texto, prioridade):
    global proximo_id

    tarefas.append(
        {
            "id": proximo_id,
            "texto": texto,
            "feito": False,
            "prioridade": prioridade,
            "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M")
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

    carregar_dados()

    pendentes = [t for t in tarefas if not t["feito"]]
    concluidas = [t for t in tarefas if t["feito"]]

    total = len(tarefas)

    total_pendentes = len(pendentes)
    total_concluidas = len(concluidas)

    percentual = 0

    if total > 0:
        percentual = round((total_concluidas / total) * 100)

    return render_template(
        "index.html",
        pendentes=pendentes,
        concluidas=concluidas,
        total=total,
        total_pendentes=total_pendentes,
        total_concluidas=total_concluidas,
        percentual=percentual
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():

    texto = request.form.get("texto_tarefa", "").strip()
    prioridade = request.form.get("prioridade", "Baixa")

    if texto:
        adicionar_tarefa(texto, prioridade)

    return redirect(url_for("index"))


@app.route("/completar/<int:id>")
def completar(id):

    completar_tarefa(id)

    return redirect(url_for("index"))


@app.route("/excluir/<int:id>")
def excluir(id):

    excluir_tarefa(id)

    return redirect(url_for("index"))


carregar_dados()

if __name__ == "__main__":
    app.run(debug=True)