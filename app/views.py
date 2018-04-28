# -*- coding: utf-8 -*-

from flask import render_template,redirect,url_for,flash
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required
from app import app,db
from .form import Login_Form,Register_Form
from .models import Users
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    form=Login_Form()
    return render_template('login.html',form=form)

@app.route('/index')
def l_index():
    form = Login_Form()
    return render_template('login.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
        form=Login_Form()
        if form.validate_on_submit():
            user=Users.query.filter_by(name=form.name.data).first()
 	    if user is not None and user.check_password(form.password.data):
		login_user(user)
		flash('登录成功')
                return  render_template('success.html',name=form.name.data)
	    else:
		flash('用户或密码错误')
                return render_template('login.html',form=form)

#用户登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已退出登录')
    return redirect(url_for('index'))


@app.route('/register',methods=['GET','POST'])
def register():
    form=Register_Form()
    if form.validate_on_submit():
        user=Users(name=form.name.data,email=form.email.data)
	user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('index'))
    return render_template('register.html',form=form)
