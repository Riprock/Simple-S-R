from flask import Flask, render_template, url_for
from dataclasses import dataclass
app = Flask(__name__) #Sets the name of the flask program

@dataclass
class Shipping:
	cli_tag: str
	tracking_num: str
	manufacturer: str
	model: str
	delievered: bool


temp = [Shipping(cli_tag='ABCD', tracking_num='5IUJDDQ4QE0E6K64', manufacturer='Fortinet', model='100D', delievered=False), 
		Shipping(cli_tag='DEFG', tracking_num='1Q09IBK428BP20TO', manufacturer='Ruckus', model='ZoneCommander', delievered=True), 
		Shipping(cli_tag='YHFG', tracking_num='024UOGA631W66771', manufacturer='Dell', model='Optiplex 1050', delievered=False)]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', shpmnts=temp, title="Home")


if __name__ == "__main__":
	app.run(debug=True)