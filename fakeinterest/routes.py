from flask import render_template
from fakeinterest import app
from flask_login import login_required



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/criarconta')
def criar_conta():
    return render_template("criarconta.html")



@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)