
import sqlite3
from flask_restful import Resource,reqparse

class User:
	
	def __init__(self,_id,username,password):
		self.id=_id
		self.username=username
		self.password=password

	@classmethod
	def find_by_username(cls,username):
        user=''
		connection = sqlite3.connect('data.db')
		cursor=connection.cursor()
		q="SELECT FROM users where username=?"
		result=cursor.execute(q,(username,))
		row=result.fetchone()
		if row:
			#user=cls(row[0],row[1],row[2])
			user=cls(*row) #pass as arg of array
		else:
			user=None
		connection.close()
		return user

	@classmethod
	def find_by_id(cls,id):
        user=''
		connection = sqlite3.connect('data.db')
		cursor=connection.cursor()
		q="SELECT FROM users where id=?"
		result=cursor.execute(q,(_id,))
		row=result.fetchone()
		if row:
			#user=cls(row[0],row[1],row[2])
			user=cls(*row) #pass as arg of array
		else:
			user=None
		connection.close()
		return user

class UserRegister(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument(
		'username',
		type=str,
		required=True,
		help="This field cannot be empty"

		)

	def post(self):
		data=UserRegister.parse.parse_args()
		if  User.find_by_username(data['username']):
			return {"message":"A user with that username exist"},400

		connection=sqlite3.connect("data.db")
		cursor=connection.cursor()

		q="INSERT INTO user VALUES (NULL,?,?)"
		cursor.execute(q,(data['username'],data['password']))
		connection.commit()
		connection.close()
		return {"message":"User create successfully"},201


