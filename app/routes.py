from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm
from app.models import User
from app.email import send_reset_email

main_routes = Blueprint('main', __name__)
auth_routes = Blueprint('auth', __name__)

@main_routes.route('/')
def home():
    return render_template('home.html')

@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        
    return render_template('register.html', form=form)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

    return render_template('login.html', form=form)

@auth_routes.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)
        return redirect(url_for('auth.login'))
    return render_template('reset_request.html', form=form)

@auth_routes.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.verify_reset_token(token)
    if user is None:
        return redirect(url_for('main.home'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
    return render_template('reset_password.html', form=form)
