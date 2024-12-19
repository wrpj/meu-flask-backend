import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "minha-chave-secreta")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///clientes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
