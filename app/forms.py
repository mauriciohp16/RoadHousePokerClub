from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    confirm_email = StringField('Confirmar Email', validators=[DataRequired(), Email(), EqualTo('email')])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    birth_date = StringField('Data de Nascimento', validators=[DataRequired()])
    phone = StringField('Telefone', validators=[DataRequired()])
    confirm_phone = StringField('Confirmar Telefone', validators=[DataRequired(), EqualTo('phone')])
    cpf = StringField('CPF', validators=[DataRequired()])
    cep = StringField('CEP', validators=[DataRequired()])
    address = StringField('Endereço', validators=[DataRequired()])
    number = StringField('Número', validators=[DataRequired()])
    complement = StringField('Complemento')
    neighborhood = StringField('Bairro', validators=[DataRequired()])
    city = StringField('Cidade', validators=[DataRequired()])
    state = StringField('Estado', validators=[DataRequired()])
    country = StringField('País', validators=[DataRequired()])
    accept_terms = BooleanField('Aceito os termos e condições', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Solicitar Redefinição')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Nova Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Nova Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Atualizar Senha')
