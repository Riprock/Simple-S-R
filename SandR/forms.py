from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from sandr.models import User
from flask_login import current_user

class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Passowrd", validators=[DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField('Login')

class CreateDelivery(FlaskForm):
	tag = StringField("Client Tag",validators=[DataRequired()])
	product = StringField("Product",validators=[DataRequired()])
	quanity = StringField("Quanity",validators=[DataRequired()])
	po_num = StringField("PO #",validators=[DataRequired()])
	tracking = StringField("Tracking #",validators=[DataRequired()])
	date = 1
	signed = 1
	tickprojnum = StringField("Ticket/Project #",validators=[DataRequired()])
	location = StringField("location",validators=[DataRequired()])