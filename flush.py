from sandr import db
import os 

os.remove(".\sandr\sitedat.db")
print("Removed DB")

db.create_all()
print("cretaed DB")