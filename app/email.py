from flask_mail import Message
from app import mail
from flask import url_for

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='fulano@gmail.com'
                  recipients=[user.email])
    msg.body = f'''Para redefinir sua senha, clique no link abaixo:
{url_for('auth.reset_token', token=token, _external=True)}

Se você não solicitou esta redefinição de senha, ignore este e-mail e nada será alterado.
'''
    mail.send(msg)
