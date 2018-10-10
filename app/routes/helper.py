from functools import wraps

from flask import render_template, current_app, request, jsonify
from flask_login import current_user

from app.database.models.user import UserRole

from config import Common as Config


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                if request.method == 'GET':
                    return current_app.login_manager.unauthorized()
                else:
                    return jsonify(success=False, message=Config.UNAUTHORIZED_MESSAGE)
            if (current_user.role != role) and (role != "ANY"):
                if request.method == 'GET':
                    return current_app.login_manager.unauthorized()
                else:
                    return jsonify(success=False, message=Config.UNAUTHORIZED_MESSAGE)

            return fn(*args, **kwargs)

        return decorated_view

    return wrapper


def render(name, **kwargs):
    return render_template(name, user=current_user, user_role=UserRole, **kwargs)
