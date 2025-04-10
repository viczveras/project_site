from flask import render_template,url_for,redirect
from fakeinterest import app, database, bcrypt
from flask_login import login_required,login_user,logout_user, current_user
from flask_bcrypt import Bcrypt
from fakeinterest.models import Usuarios, Posts
from fakeinterest.forms import Form_Login, Form_Criar_Conta



@app.route('/', methods=['GET', 'POST'])
def home():
    formlogin = Form_Login()
    if formlogin.validate_on_submit():
         usuario = Usuarios.query.filter_by(email=formlogin.email.data).first()
         if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
             login_user(usuario)
             return redirect(url_for("perfil", id_usuario=usuario.id))
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
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html", form=formcriarconta)

    


@app.route('/perfil/<id_usuario>')
@login_required
def perfil(id_usuario):
    if int(id_usuario) == current_user.id:
        usuario = current_user
    else:
        usuario = Usuarios.query.get(int(id_usuario))
        if usuario is None:
            return "Usuário não encontrado", 404  # Tratamento de erro
    return render_template('perfil.html', usuario=usuario)

@app.route('/logout')
@login_required
def logout():

    logout_user()
    return redirect(url_for("home"))