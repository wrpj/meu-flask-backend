from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Cliente, Equipamento

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    clientes = Cliente.query.order_by(Cliente.data_proxima_manutencao).all()
    return render_template("index.html", clientes=clientes)

@bp.route("/cliente/<int:cliente_id>")
def cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    return render_template("cliente.html", cliente=cliente)

@bp.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        nome = request.form["nome"]
        cliente = Cliente(nome=nome, data_proxima_manutencao=datetime.utcnow())
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("adicionar.html")
