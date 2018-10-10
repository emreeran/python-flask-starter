from flask import redirect, url_for
from flask_login import logout_user

from app import application
from app.routes.helper import render, login_required


@application.route('/login', methods=['GET'])
def login():
    return render('login.html')


@application.route('/logout', methods=['GET', 'POST'])
@login_required()
def logout():
    logout_user()
    return redirect(url_for('login'))
