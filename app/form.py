# -*- coding: utf-8 -*-

from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required,Email
from flask_wtf import FlaskForm

#登录表单
class Login_Form(FlaskForm):
    name=StringField('Name',validators=[Required()])
    password=PasswordField('Password',validators=[Required()])
    submit=SubmitField('Login in')


#注册表单
class Register_Form(FlaskForm):
    name=StringField('Name',validators=[Required()])
    password=PasswordField('Password',validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    submit=SubmitField('register')
