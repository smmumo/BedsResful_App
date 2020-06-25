
import os

from flask import Flask
from flask_restful import Api
#from flask_jwt import JWT

#from security import aunthenticate,identity

#import controller or resources
from controller.HotelController import Hotels
from controller.UserController import Users

from flask_jwt import JWT,jwt_required

#from security import aunthenticate,identity
"""
from controller.PrebookController import Prebook
from controller.BookingController import Bookings
"""

app=Flask(__name__) 

app.config['DEBUG']=True

app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL', 'mysql+pymysql://root:degraP@55w0rd@localhost:8889/BEDS')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to know wehn object has changed,
app.secret_key = 'simon'

api = Api(app)

#jwt=JWT(app,aunthenticate,identity) #to aunthenticate

"""
set api routing 
eg 
api.add_resource(ItemList, '/items')
"""
api.add_resource(Users, '/userlist')
api.add_resource(Hotels, '/hotellist')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)
	
    
    