from flask import render_template
from fakeinterest import app
from flask_login import login_required
from fakeinterest.forms import Form_Login, Form_Criar_Conta



@app.route('/', methods=['GET', 'POST'])
def home():
    formlogin = Form_Login()
    return render_template('index.html', form = formlogin)


#@app.route('/')
#def home():
#    return "Teste simples"

    


@app.route('/criarconta',  methods=['GET', 'POST'])
def criar_conta():
    formcriarconta = Form_Criar_Conta()
    return render_template("criarconta.html", form = formcriarconta)
    


@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
   return render_template('perfil.html', usuario=usuario)
   