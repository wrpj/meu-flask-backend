from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Instanciar extensões
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes, auth
        app.register_blueprint(routes.bp)
        app.register_blueprint(auth.bp)

        db.create_all()  # Cria tabelas no banco de dados

    return app
