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

class RegistrationForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired(), Email()])
	first = StringField("First Name", validators=[DataRequired()])
	last = StringField("Last Name", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	confirm_password = PasswordField("Confirm", validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Create Account')

	def validate_user(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That Username is taken')
	
	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('Email is already in use')


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