from app import application, db

db.create_all()

if __name__ == '__main__':
    application.run()
