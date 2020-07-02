from flask_mail import Message
from sandr import mail
from sandr.models import Delivery

def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request',
					sender='noreply@demo.com',
					recipients=[user.email])
	msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
	mail.send(msg)

def shipment_rec_email(delivery):
	msg = Message('New Delivery recieved', sender='sandr@test.com', recipients=[user.username + "@test.com"])
	msg.body =f'A new Delvery has arrived for {delivery.client} '


def order_placed(delivery):
msg = Message(f'An Order has been placed for {delivery.tag}')