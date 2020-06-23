
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
	Shipping(tag='ASDF', product='Ruckus ZoneCommander', quantity=2, po_num='SOmeNum', tracking_num='74FW1B24V0R33234', signed=True, tickprojnum='T3234.234', location="Basement"), 
	Shipping(cli_tag='DEFG', manufacturer='Ruckus', model='ZoneCommander', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='G8J87GH2488SNDZ8', deliver_date='4/20/20202', signed=False), 
	Shipping(cli_tag='YHFG', manufacturer='Dell', model='Optiplex 1050', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='C32019MW8S95RT6T', deliver_date='4/20/20202', signed=False), 
	Shipping(cli_tag='QWER', manufacturer='Apple', model='Iphne 7', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='T87HJHouih(*&)(kjbik', deliver_date='4/20/20202', signed=True), 
	Shipping(cli_tag='YHJS', manufacturer='Cisco', model='Phone', quantity=2, PO_num='SOmeNum', tick_proj='T3234.234', tracking_num='HTIH707070GVUYV876', deliver_date='4/20/20202', signed=True)
	]