from datetime import datetime
from SandR import app, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return  User.query.get(int(user_id))

class Delievery(db.model):
	id = db.Column(db.Integer, primary_key=True)
	tag = db.Column(db.String(4), nullable=False, unique=False)
	product = db.Column(db.String, nullable=False, unique=False)
	quanity = db.Column(db.Integer, nullable=False, unique=False)
	po_num = db.Column(db.String, nullable=False, unique=False)
	tracking = db.Column(db.String, nullable=True, unique=False)
	date = db.Column(db.DateTime, nullable=True, unique=False)
	signed = db.column(db.String(2), nullable=True, unique=False)
	tickprojnum = db.Column(db.String, nullable=True, unique=False)
	location = db.Column(db.String, nullable=True, unique=False)
	
	def __repr(self):
		return f"Delievery(client: {self.tag}, Product: {self.product}, Quantity: {self.quanity})"

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first = db.Column(db.String, unique=False, nullable=False)
	last = db.Column(db.String, unique=False, nullable=False)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}','{self.image_file}')"
