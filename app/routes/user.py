import bcrypt
from flask import request

from app import application
from app.database.dao.user_dao import UserDao
from app.database.models.user import User, UserRole


@application.route('/user/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        args = request.json
        password = args["password"]
        hashed_password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        user = User(name=args["name"], email=args["email"], password=hashed_password, role=UserRole.USER)
        UserDao.insert(user)
        return "OK"


@application.route('/user/find-by-email', methods=['POST'])
def find_user_by_email():
    if request.method == 'POST':
        args = request.json
        user = UserDao.find_by_email(args["email"])
        return user.email + " pass: " + user.password
