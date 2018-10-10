from app import login_manager, db
from app.database.dao.dao import Dao
from app.database.models.user import User


class UserDao(Dao):
    @staticmethod
    def find_by_id(user_id):
        """
        Find User with given id
        :param user_id: Id of user to find
        :return: User object if found, None otherwise
        """
        return User.query.get(user_id)

    @staticmethod
    def find_by_email(email):
        """
        Find User with given email
        :param email: String email to find
        :return: User object if found, None otherwise
        """
        return User.query.filter_by(email=email).first()

    @staticmethod
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == user_id).first()

    @staticmethod
    def delete_by_id(user_id):
        User.query.filter_by(id=user_id).delete()
        db.session.commit()
