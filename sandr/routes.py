from flask import Flask, render_template, url_for, flash, redirect, request
from sandr import app, db, bcrypt
from sandr.models import User, Delivery, Client
from sandr.forms import LoginForm, RegistrationForm, CreateDelivery, UpdateAccountForm
from flask_login import login_user, current_user, logout_user, login_required
from dataclasses import dataclass

@app.route("/home")
def home():
	shpmnts = Delivery.query.all()
	return render_template('home.html', title="Home", shpmnts=shpmnts)

@app.route("/thome")
def thome():
	return render_template('thome.html', shpmnts=temp, title="Test")


@app.route("/register", methods = ['POST', 'GET'])
def register():
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
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Failed check username and pass')
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route("/account", methods=['GET', 'POST'])
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Accoount has been updated')
		return redirect(url_for('account'))
	elif request.method == "GET":
		form.first.data = current_user.first
		form.last.data = current_user.last
		form.username.data = current_user.username
		form.email.data = current_user.email
	return render_template('account.html', title="Account", form=form)

@app.route("/create", methods=['GET', 'POST'])
def create():
	form = CreateDelivery()
	if form.validate_on_submit():
		delivery = Delivery(
			tag = form.tag.data,
			product = form.product.data,
			quanity = form.quanity.data,
			po_num = form.po_num.data,
			tracking = form.tracking.data,
			#date = form.date.data,
			sig = form.sig.data,
			tickprojnum = form.tickprojnum.data,
			location = form.location.data
		)
		db.session.add(delivery)
		db.session.commit()
		flash("New Delivery has been added")
		return redirect(url_for('home'))
	return render_template('create.html', title="Create", form=form)

@app.route("/client/<tag>")
def client(tag):
	id = Client.id
	client_shp = Client.query.filter_by(tag=tag).all()
	return render_template("client.html", title="ClientName", shpmts=client_shp)