from sandr import db
from sandr.models import Delivery, Client



def first():
	temp = [
	Delivery(manufacturer='Dell', model='Optiplex 1050', quanity=2, po_num='SomeNum', tracking='U118744K63QW45SW', sig=True, tickprojnum='T20201215.00054', location='In Shipping'), 
	Delivery(manufacturer='Ruckus', model='ZoneCommander', quanity=2, po_num='SomeNum', tracking='1I39F8W1F4JQ1V5T', sig=False, tickprojnum='T20190905', location='In Basement'), 
	Delivery(manufacturer='Dell', model='Optiplex 1050', quanity=2, po_num='SomeNum', tracking='TT47N6SSZIE65I51', sig=False, tickprojnum='T20201215.00054', location='In Shipping'), 
	Delivery(manufacturer='Fortinet', model='100D', quanity=2, po_num='SomeNum', tracking='V9A55KV8Q389041B', sig=False, tickprojnum='T20200718.00012', location='Deploy Room'), 
	Delivery(manufacturer='Ruckus', model='ZoneCommander', quanity=2, po_num='SomeNum', tracking='YFWS8DNC7Z40N4OJ', sig=False, tickprojnum='T20190905', location='In Basement'), 
	Delivery(manufacturer='Ruckus', model='ZoneCommander', quanity=2, po_num='SomeNum', tracking='VOT207H1BTY573AV', sig=False, tickprojnum='T20190905', location='In Basement'), 
	Delivery(manufacturer='Ruckus', model='ZoneCommander', quanity=2, po_num='SomeNum', tracking='1155OLEPM6BJ3X0S', sig=False, tickprojnum='T20190905', location='In Basement'), 
	Delivery(manufacturer='Fortinet', model='100D', quanity=2, po_num='SomeNum', tracking='B64728Z3ILF69DZY', sig=False, tickprojnum='T20200718.00012', location='Deploy Room'), 
	Delivery(manufacturer='Fortinet', model='100D', quanity=2, po_num='SomeNum', tracking='0YDI8462CY97OLR3', sig=True, tickprojnum='T20200718.00012', location='Deploy Room'), 
	Delivery(manufacturer='Dell', model='Optiplex 1050', quanity=2, po_num='SomeNum', tracking='KD0297Q12K1PWI9B', sig=False, tickprojnum='T20201215.00054', location='In Shipping'),
	Delivery(manufacturer='Ruckus', model='ZoneCommander', quanity=2, po_num='SomeNum', tracking='V1GV27G0966HI1R8', sig=True, tickprojnum='T20190905', location='In Basement'), 
	Delivery(manufacturer='Fortinet', model='100D', quanity=2, po_num='SomeNum', tracking='2W9CH98AXYB0N38D', sig=False, tickprojnum='T20200718.00012', location='Deploy Room'), 
	Delivery(manufacturer='Fortinet', model='100D', quanity=2, po_num='SomeNum', tracking='O84SS8BYY24L0L47', sig=True, tickprojnum='T20200718.00012', location='Deploy Room'),
	Delivery(manufacturer='Dell', model='Optiplex 1050', quanity=2, po_num='SomeNum', tracking='84W9EE8TIF9PVD1C', sig=True, tickprojnum='T20201215.00054', location='In Shipping'), 
	Delivery(manufacturer='Fortinet', model='100D', quanity=2, po_num='SomeNum', tracking='H7QDQYQ1RBP25XR7', sig=True, tickprojnum='T20200718.00012', location='Deploy Room'), 
	Delivery(manufacturer='Dell', model='Optiplex 1050', quanity=2, po_num='SomeNum', tracking='27J6B4960F2W9EYA', sig=False, tickprojnum='T20201215.00054', location='In Shipping')
	]
	Clients = [Client(name="Walmart",tag="WLMT"),Client(name="Amazon",tag="AMZN"),Client(name="Tesla",tag="TSLA"),Client(name="Life Alert",tag="ALRT")]
	for i in temp:
		db.session.add(i)
	for i in Clients:
		db.session.add(i)
	db.session.commit()

def second():
	counter = 1
	for i in Delivery.query.all():
		i.client_id = counter
		db.session.commit()
		counter += 1
		if counter > 4:
			counter = 1

first()
second()