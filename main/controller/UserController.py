

#user controller class handles all the incoming HTTP requests relating to the user .

"""
Resouce

"""
#import requests
from flask import Flask,jsonify,request,render_template
from flask_restful import Resource, reqparse
from model.User import UserModel


class Users(Resource):
	def get(self):
		item = UserModel.allUser()
		if item:
			 return jsonify(item) #item.json()
		return {'message': 'User not found'}, 404


			
        
        
           
        