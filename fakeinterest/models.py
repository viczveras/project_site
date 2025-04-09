from fakeinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin



# def que carrega o usuário
@login_manager.user_loader
def load_user(id_usuario):
    return Usuarios.query.get(int(id_usuario))

class Usuarios(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Posts", backref="usuario", lazy=True)

class Posts(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False)