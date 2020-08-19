from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.fields.html5 import DateField
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
	tag = SelectField("Client Tag")
	manufacturer = SelectField("Manufacturer", coerce=str)#StringField("Manufacturer",validators=[DataRequired()])
	model = StringField("Model",validators=[DataRequired()])
	quanity = IntegerField("Quanity",validators=[DataRequired()])
	po_num = StringField("PO #",validators=[DataRequired()])
	tracking = StringField("Tracking #",validators=[DataRequired()])
	date = DateField("Delivery Date")
	sig = BooleanField("Signed for?")
	tickprojnum = StringField("Ticket/Project #",validators=[DataRequired()])
	location = StringField("location",validators=[DataRequired()])
	ship_co = StringField("Shipping Company", validators=[DataRequired()])
	engineer = SelectField("Engineer", coerce=str)
	submit = SubmitField("Create Delivery")

			
class UpdateAccountForm(FlaskForm):
	first = StringField("First Name", validators=[DataRequired()])
	last = StringField("Last Name", validators=[DataRequired()])
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField("Email", validators=[DataRequired(), Email()])
	submit = SubmitField('Update!')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is taken')

	def validate_email(self, email):
		if email.data != current_user.email:
			email = User.query.filter_by(email=email.data).first()
			if email:
				raise ValidationError('That email is in use')

class UpdateDelivery(FlaskForm):
	tag = StringField("Client Tag",validators=[DataRequired()])
	product = StringField("Product",validators=[DataRequired()])
	quanity = StringField("Quanity",validators=[DataRequired()])
	po_num = StringField("PO #",validators=[DataRequired()])
	tracking = StringField("Tracking #",validators=[DataRequired()])
	date = DateField("Delivery Date", format='%m-%d-%Y')
	signed = BooleanField("Signed for?")
	tickprojnum = StringField("Ticket/Project #",validators=[DataRequired()])
	location = StringField("location",validators=[DataRequired()])
	submit = SubmitField("Create Delivery")

class CreateClient(FlaskForm):
	name = StringField("Client Name", validators=[DataRequired()])
	tag = StringField("Client Tag", validators=[DataRequired()])
	submit = SubmitField("Add Client")

class Search(FlaskForm):
	search_field = StringField("Search", validators=[DataRequired()])
	submit = SubmitField("Search")