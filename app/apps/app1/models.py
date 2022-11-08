# from database.database import db
# from flask_login import UserMixin

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150))
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))

# def __init__(self, name, email):
#     self.name = name
#     self.email = email