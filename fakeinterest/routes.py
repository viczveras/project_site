from flask import render_template
from fakeinterest import app, database, bcrypt
from flask_login import login_required
from flask_bcrypt import Bcrypt
from fakeinterest.models import Usuarios, Posts
from fakeinterest.forms import Form_Login, Form_Criar_Conta



@app.route('/', methods=['GET', 'POST'])
def home():
    formlogin = Form_Login()
    return render_template('index.html', form = formlogin)


#@app.route('/')
#def home():
#    return "Teste simples"

    


@app.route('/criarconta', methods=['GET', 'POST'])
def criar_conta():
    formcriarconta = Form_Criar_Conta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data).decode('utf-8')
        usuario = Usuarios(username=formcriarconta.username.data, senha=senha, email=formcriarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
    return render_template("criarconta.html", form=formcriarconta)

    


@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
   return render_template('perfil.html', usuario=usuario)
   