from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakeinterest import Usuario

class Form_Login():
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired])
    confirm_button= SubmitField("Fazer Login")



class Form_Criar_Conta():
    username = StringField("Usuário", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    confirmar_senha = PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo("senha")])
    confirm_button = SubmitField("Criar conta")

    def validate_email(self, email):

        usuario = Usuario.query.filter_by(email=email.data).first() # lista de usuários com email igual ao deste usuário

        if usuario:
            return ValidationError("E-mail já cadastrado.")
        

