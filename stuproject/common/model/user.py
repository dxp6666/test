'''
coding:utf-8
@Time:2023/3/14 11:16
@Author:dxp
'''
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(8), unique=True)
    user_pw = db.Column(db.String(8), unique=True)
    user_name = db.Column(db.String(12), unique=True)
    user_fullname = db.Column(db.String(12), unique=True)
    def __str__(self):
        return self.u_name







