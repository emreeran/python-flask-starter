from app import db


class Dao:
    @staticmethod
    def insert(item):
        db.session.add(item)
        db.session.commit()

    @staticmethod
    def insert_list(items):
        db.session.bulk_save_objects(items)
        db.session.commit()

    @staticmethod
    def update(item):
        db.session.merge(item)
        db.session.commit()
