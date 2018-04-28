from flask import Flask
from flask_bootstrap import Bootstrap
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
login_manger=LoginManager()
login_manger.init_app(app)
login_manger.login_view = 'login'

from app import views, models
