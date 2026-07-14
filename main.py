from flask import Flask, render_template, request, redirect, url_for
from operacoes import (
    criar_nova_nota,
    listar_todas_as_notas,
    atualizar_nota,
    deletar_nota,
    buscar_nota_por_id,
)

app = Flask(__name__)


# Rota principal: lista todas as notas na tela inicial
@app.route("/")
def index():
    notas = listar_todas_as_notas()
    return render_template("index.html", notas=notas)


# Rota para receber os dados do formulário e criar uma nova nota
@app.route("/criar", methods=["POST"])
def criar():
    titulo = request.form["titulo"]
    conteudo = request.form["conteudo"]
    criar_nova_nota(titulo, conteudo)
    return redirect(url_for("index"))


# Rota para deletar uma nota pelo ID
@app.route("/deletar/<int:id_nota>")
def deletar(id_nota):
    deletar_nota(id_nota)
    return redirect(url_for("index"))


# Rota para abrir a página de edição: busca o ID e carrega o formulário preenchido
@app.route("/editar/<int:id_nota>")
def editar(id_nota):
    nota = buscar_nota_por_id(id_nota)
    if nota:
        return render_template("editar.html", nota=nota)
    return redirect(url_for("index"))


# Rota para salvar a atualização: processa o envio do formulário de edição
@app.route("/atualizar/<int:id_nota>", methods=["POST"])
def atualizar(id_nota):
    novo_titulo = request.form["titulo"]
    novo_conteudo = request.form["conteudo"]
    atualizar_nota(id_nota, novo_titulo, novo_conteudo)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)