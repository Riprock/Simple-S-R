from flask import Flask, render_template, url_for, flash, redirect, request
from sandr import app, db, bcrypt
from sandr.models import User, Delievery
from sandr.forms import LoginForm, RegistrationForm
from flask_login import login_user, current_user, logout_user, login_required
from dataclasses import dataclass


@dataclass
class Shipping:
	cli_tag: str
	manufacturer: str
	model: str
	quantity: int
	PO_num: str
	tick_proj: str
	tracking_num: str
	deliver_date: str
	signed: bool

temp = [
	Shipping(cli_tag='ASDF', manufacturer='Ruckus', model='ZoneCommander', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='74FW1B24V0R33234', deliver_date='4/20/20202', signed=True), 
	Shipping(cli_tag='DEFG', manufacturer='Ruckus', model='ZoneCommander', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='G8J87GH2488SNDZ8', deliver_date='4/20/20202', signed=False), 
	Shipping(cli_tag='YHFG', manufacturer='Dell', model='Optiplex 1050', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='C32019MW8S95RT6T', deliver_date='4/20/20202', signed=False), 
	Shipping(cli_tag='QWER', manufacturer='Apple', model='Iphne 7', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='T87HJHouih(*&)(kjbik', deliver_date='4/20/20202', signed=True), 
	Shipping(cli_tag='YHJS', manufacturer='Cisco', model='Phone', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='HTIH707070GVUYV876', deliver_date='4/20/20202', signed=True)
	]

@app.route("/home")
def home():
	return render_template('home.html', shpmnts=temp, title="Home")

@app.route("/register")
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, password = hashed_pw, first = form.first.data, last = form.last.data, email = form.email.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been created. User {form.username.data} can now login')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/", methods=['POST', 'GET'])
@app.route("/login", methods=['POST', 'GET'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

@app.route("/account")
def account():
	return render_template('account.html', title="account")