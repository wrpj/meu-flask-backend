from app import db
from datetime import datetime, timedelta

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_proxima_manutencao = db.Column(db.Date, nullable=False)
    equipamentos = db.relationship('Equipamento', backref='cliente', lazy=True)

class Equipamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    ultima_manutencao = db.Column(db.Date, nullable=False)
    proxima_manutencao = db.Column(db.Date, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

    @staticmethod
    def calcular_proxima_manutencao(ultima_manutencao, categoria):
        intervalo = {"bomba de recalque": 11, "bomba submersivel": 6}
        meses = intervalo.get(categoria.lower(), 12)  # Padrão: 12 meses
        return ultima_manutencao + timedelta(days=meses * 30)
