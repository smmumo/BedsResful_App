

from flask import Flask
from flask_restful import Resource,Api, reqparse
from flask import Flask,jsonify,request,render_template,g
from model.Hotel import HotelModel
from model.User import UserModel
from werkzeug.security import generate_password_hash, check_password_hash


from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from flask_httpauth import HTTPBasicAuth,HTTPTokenAuth
auth = HTTPBasicAuth()

#auth = HTTPTokenAuth(scheme='Bearer')
import jwt


class Hotels(Resource):
	tokens = {
    "secret-token-1": "john",
	"secret-token-2": "susan"
	}
	"""
	parser = reqparse.RequestParser()	
	parser.add_argument('username',
		type=str,
		required=True,
		help="This field cannot be blank."
	)
	parser.add_argument('password',
		type=str,
		required=True,
		help="This field cannot be blank."
	)
	parser.add_argument('Nights',
		type=int,
		required=True,
		help="night is required."
	)
	parser.add_argument('Checkin_Date',
		type=str,
		required=True,
		help="checkin cannot be blank."
	)
	parser.add_argument('Rooms',
		type=str,
		required=True,
		help="Rooms cannot be blank."
	)
	parser.add_argument('ADLTS_1',
		type=str,
		required=True,
		help="ADLTS_1 cannot be blank."
	)
	parser.add_argument('ADLTS_2',
		type=str,
		required=True,
		help="ADLTS_2 cannot be blank."
	)
	parser.add_argument('ADLTS_2',
		type=str,
		required=True,
		help="ADLTS_2 cannot be blank."
	)
	"""	
	

	#@jwt_required()
	#@auth.login_required
	def get(self):
		#data = Hotels.parser.parse_args()
		
		#print(data)
		#hotel=HotelModel.hotellist()
		req_data=''
		#req_data = request.get_json()
		hotel=HotelModel.Offers(req_data)
		if hotel:
			return hotel #jsonify(hotel)
		return {"message":"Note hotel found"}


	@auth.verify_password
	def verify_password(username, password):
		users={
		"simon": generate_password_hash("simon"),
		"susan": generate_password_hash("bye")
		}
		if username in users and \
				check_password_hash(users.get(username), password):
			return username

	

		
        	

	
	

