

#from db import db
#from flask_mysqldb import MySQL
#import mysql.connector as mariadb
#connection = mariadb.connect(user='root', password='degraP@55w0rd', database='yt')
#cursor = connection.cursor()
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from flask_httpauth import HTTPBasicAuth,HTTPDigestAuth
auth = HTTPBasicAuth()
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='degraP@55w0rd', db='yt', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

class UserModel():
	#__tablename__="Users"
	#id=db.Column(db.Integer,primary_key=True)
	#username=db.Column(db.String(50))
	#password=db.Column(db.String(50))
	users_old = {
	"simon": generate_password_hash("simon"),
    "susan": generate_password_hash("bye")
	}
	users = {
    "simon": "simon",
    "susan": "bye"
	}

	
	

	"""
	@auth.verify_password
	def verify_password(username, password):
		if username in users:
			print(auth.current_user())
			return username #check_password_hash(users.get(username), password)

	"""	
	"""	
	@auth.get_password
	def get_pw(username):
		if username in users:
			return users.get(username)
		return None
	"""

		

    

	
	
	
	"""
	def hash_password(self):
  		self.password = generate_password_hash(self.password).decode('utf8')

 	def check_password(self, password):
		return check_password_hash(self.password, password)

	#@classmethod
	#def allUser(cls):
		#cursor=connection.cursor()
		#cursor.execute("SELECT * FROM members")
		#record=cursor.fetchall()
		#return record
		#print(record)
		#return cls.query.all()
		#return cls.query.filter_by(username=username).first()
		#cursor=connection.cursor()
		#query="SELECT * FROM Liyana_Hotels  WHERE hotel_id='979179' OR hotel_id='26384' " #WHERE hotel_id='979179' OR hotel_id='26384'
		
		#cursor.execute(query)
	"""
	"""
	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

	@auth.verify_password
	def verify_password(username, password):
		cursor=connection.cursor()
		#user = User.query.filter_by(username = username).first()
		q="SELECT FROM members where username=?"
		result=cursor.execute(q,(username,))
		user=result.fetchone()
		user='simon'#self(*user)
		if not user :#or not user.verify_password(password)
			return False
		g.user = user
		return True

	def generate_auth_token(self, expiration = 600):
		s=Serializer(app.config['SECRET_KEY'], expires_in = expiration)
		return s.dumps({ 'id': self.id })

	@staticmethod
	def verify_auth_token(token):
		s = Serializer(app.config['SECRET_KEY'])
		try:
			data=s.loads(token)
		except SignatureExpired:
			return None # valid token, but expired
		except BadSignature:
			 return None # invalid token
		return User.query.get(data['id'])
        #return user
	
	@auth.verify_password
	def verify_password(username_or_token, password):
		# first try to authenticate by token
		user = User.verify_auth_token(username_or_token)
		if not user:
			# try to authenticate with username/password
			user = User.query.filter_by(username = username_or_token).first()
			if not user or not user.verify_password(password):
				return False
		g.user = user
		return True
	"""

		


		
        

	
    
		
		



		




	"""
	

	

	@auth.login_required
	def get_auth_token():
		token = g.user.generate_auth_token()
		return jsonify({ 'token': token.decode('ascii') })

	@auth.verify_password
	def verify_password(username_or_token, password):
		# first try to authenticate by token
		user = User.verify_auth_token(username_or_token)
		if not user:
			# try to authenticate with username/password
			user = User.query.filter_by(username = username_or_token).first()
			if not user or not user.verify_password(password):
				return False
		g.user = user
		return True
	"""
	
		
