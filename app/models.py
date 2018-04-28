# -*- coding: utf-8 -*-

from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_script import Manager, Shell
from app import app,manager,db,login_manger

class Users(UserMixin,db.Model):
    __tablename__ = 'users'       #对应mysql数据库表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120))

    def __repr__(self):
        return '<User:{0}>' .format(self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manger.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.shell_context_processor
def make_shell_context():
        return dict(app=app, db=db, Users=Users)
manager.add_command("shell", Shell(make_context=make_shell_context))
