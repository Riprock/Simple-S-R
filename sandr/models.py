from sandr import db
from datetime import datetime
from sandr import app, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return  User.query.get(int(user_id))

class Delivery(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	manufacturer = db.Column(db.String, nullable=False, unique=False)
	model = db.Column(db.String, nullable=False, unique=False)
	quanity = db.Column(db.Integer, nullable=False, unique=False)
	po_num = db.Column(db.String, nullable=False, unique=False)
	tracking = db.Column(db.String, nullable=False, unique=False)
	date = db.Column(db.DateTime, nullable=True, unique=False)
	sig = db.Column(db.String(2), nullable=True, unique=False)
	tickprojnum = db.Column(db.String, nullable=False, unique=False)
	location = db.Column(db.String, nullable=True, unique=False)
	ship_co = db.Column(db.String, nullable=True, unique=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=True)
	
	def __repr__(self):
		return f"Delivery(ID: {self.id},Product: {self.product}, Quantity: {self.quanity})"

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first = db.Column(db.String, unique=False, nullable=False)
	last = db.Column(db.String, unique=False, nullable=False)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	deliveries = db.relationship('Delivery', backref="engineer", lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"

class Client(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tag = db.Column(db.String(4), nullable=False, unique=True) 
	name = db.Column(db.String, nullable=False, unique=True)
	deliveries = db.relationship('Delivery', backref="client", lazy=True)
	
	def __repr__(self):
		return f"Client('{self.tag}', '{self.name}', '{self.id}')"