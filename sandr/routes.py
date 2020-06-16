from flask import Flask, render_template, url_for, flash, redirect, request
from sandr import app, db, bcrypt
from sandr.models import User, Delievery
from sandr.forms import LoginForm
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
Shipping(cli_tag='YHFG', manufacturer='Dell', model='Optiplex 1050', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='L40NKBW24T1CHDM8', deliver_date='4/20/20202', signed=True), 
Shipping(cli_tag='ABCD', manufacturer='Fortinet', model='100D', quantity=2, PO_num='SOmeNum', tick_proj='P3234.234', tracking_num='NSM930P7SPXGBT58', deliver_date='4/20/20202', signed=True), 
Shipping(cli_tag='DEFG', manufacturer='Ruckus', model='ZoneCommander', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='TA0Z0VFNI694JZ45', deliver_date='4/20/20202', signed=False)]


@app.route("/home")
def home():
	return render_template('home.html', shpmnts=temp, title="Home")

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route("/", methods=['POST', 'GET'])
@app.route("/login", methods=['POST', 'GET'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)
