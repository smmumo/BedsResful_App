
#from db import db
#import sqlite3
#import mysql.connector as mariadb
#connection = mariadb.connect(user='root', password='degraP@55w0rd', database='yt')
#cursor = connection.cursor()
import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='degraP@55w0rd', db='yt', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
from mergedeep import merge
from service.CommonService import CommonModel
import pandas as pd
import json
from datetime import timedelta,date,datetime
from model.Db import HotelDb
class HotelModel():	
	def __init__(self):
	    pass

	
	@classmethod
	def hotellist(cls):
		cursor=connection.cursor()
		query="SELECT * FROM Liyana_Hotels  WHERE hotel_id='979179' OR hotel_id='26384' " #WHERE hotel_id='979179' OR hotel_id='26384'
		
		cursor.execute(query)
		#record=cursor.fetchall()
		hotel={}
		hotellist={}
		rows=[]
		for row in cursor:
			hotelid=int(row["hotel_id"])
			#rows+=[row]
			hotel={
			"hotel_name":row["hotel_name"],
			"hotel_id":hotelid,
			"tticode":row["tticode"],
			"destination_name":row["destination_name"],
			"country_name":row["country_name"],
			"resort_name":row["resort_name"],
			"classification":row["classification"],
			"iconId":row["iconId"],
			}
			hotellist[row["hotel_id"]]=hotel #[row["hotel_id"]]

		#rooms=cls.Offers()#cls.RoomsList()
		#available_hotel=cls.Arraymerge(hotellist,rooms)#cls.array_merge_recursive(hotellist,rooms)

		#available_hotel={**hotellist,**rooms}
		return hotellist
		#print(json.dumps(rows, sort_keys=False, indent=4, separators=(',', ': ')))
	@classmethod
	def Offers(cls,params):
		HotelDb.test();
		Search_Criteria={}
		session={}	
		"""
		Checkout_Date = params["Checkin_Date"]#"2020-05-20"#date.today()#+ timedelta(days=5)
		c_date=cls.validate_date(params["Checkin_Date"])
		if c_date==False:
			return {"message":"Invalid date format"}

		Checkout_Date=datetime.strptime(Checkout_Date,"%Y-%m-%d")
		Checkout_Date=Checkout_Date+timedelta(days=5)
		Checkout_Date=datetime.strftime(Checkout_Date,"%Y-%m-%d")
		#date_1 = datetime.datetime.strptime(start_date, "%m/%d/%y")
		
			
	
		
		Search_Criteria["Search_Criteria"] = {
        'Rooms' :params["Rooms"],
        'Checkin_Date' :params["Checkin_Date"] ,
        'CheckOut_Date' :Checkout_Date ,
        'Adlts_1' : params["ADLTS_1"],
        'Child_1' : params["CHILD_1"] ,
        'Infant_1' : "0",
        'Infant_2' : "0",
        'Infant_3' : "0",
        'Adlts_2' : params["ADLTS_2"],
        'Child_2' : params["CHILD_2"],
        'Adlts_3' : params["ADLTS_3"],
        'Child_3' : params["CHILD_3"],
        }
		"""	
		Search_Criteria["Search_Criteria"] = {}	
		session["Session"] = {}	
		offers={}
		hotel_room2_data={}
		hotel_room3_data={}
		hotel_room1_data={}
		No_of_rooms=1#int(params["Rooms"])
		#print(No_of_rooms)
		hotel_available={}
		#if No_of_rooms<=3:
		
		if No_of_rooms==1:
			Rooms =f'Room_{No_of_rooms}'
			availablerooms=cls.AvailableRooms()				
			offers=cls.fetchRoomOffers(availablerooms,Rooms)
			#return offers
		if No_of_rooms>=2:
			Rooms =f'Room_{1}'
			availablerooms=cls.AvailableRooms()				
			hotel_room1_data=cls.fetchRoomOffers(availablerooms,Rooms)			

			Rooms =f'Room_{2}'							
			hotel_room2_data=cls.fetchRoomOffers(availablerooms,Rooms)
			#if hotel_room2_data :
			#print(offers)
			offers=cls.combineDicts(hotel_room1_data,hotel_room2_data)
			
			if No_of_rooms==3:		

				Rooms =f'Room_{3}'
				availablerooms=cls.AvailableRooms()			
				hotel_room3_data=cls.fetchRoomOffers(availablerooms,Rooms)	
	
						

		avalable_hotels=cls.hotellist()
		
		hotel_available=offers#cls.combineDicts(avalable_hotels,offers)
		#float_dict = {inner_k: {inner_v for (inner_k, inner_v) in avalable_hotels.items()}}
		#print(hotel_available)
		session["Session"] = {
            'id':"",
            'Currency': 'GBP',
			'Hotel':hotel_available
		}			
		hotel_available={**Search_Criteria,**session}	
		return hotel_available


	def combineDicts(dictionary1, dictionary2):
		output = {}
		for item, value in dictionary1.items():
			if dictionary2.keys():
				if isinstance(dictionary2[item], dict):
					output[item] ={**value,**dictionary2.pop(item)} #combineDicts(value, dictionary2.pop(item))
			else:
				output[item] = value
		for item, value in dictionary2.items():
			output[item] = value
		return output



	def merge(obj_1, obj_2):
		if type(obj_1) == dict and type(obj_2) == dict:
			result = {}
			for outer_key, value in obj_1.items():
				for inner_key, value2 in obj_2.items():
					print(inner_key)
					if outer_key in obj_2.keys():
						#print("is there")
						#print(obj_2[inner_key])	
						result[inner_key]={**value,**value2}					
						#result[outer_key]=merge(value, obj_2[inner_key])
					#print(obj_1.keys())
					#if value.get("hotel_id")== value2.get("hotel_id"):
					#if key not in obj_2:
						#print(key)
						#result[key] = {**value,**value2}
						#result[key]=merge(value, obj_2[key])
					#else:
						#result[key] ='' #merge(value, obj_2[key])
			#for key, value in obj_2.items():
				#if key not in obj_1:
					#result[key] = value
			return result #get("hotel_id")

	@classmethod
	def validate_date(cls,date_text):
		try:
			if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
				raise ValueError
			return True
		except ValueError:
			return False
		
			
		

	@classmethod
	def AvailableRooms(cls):		
		cursor=connection.cursor()
		query="SELECT room_id,hotel_id,tticode,room_price FROM  roomsitravel WHERE hotel_id='979179' OR hotel_id='26384'    " 
		cursor.execute(query)	#where hotel_id='979179' OR hotel_id='26384'
		
		return cursor		
	
	@classmethod
	def RoomsList(cls):
		cursor=connection.cursor()
		query="SELECT * FROM  roomsitravel " 	#where hotel_id='979179'	
		cursor.execute(query)
		rows=[]
		rooms={}
		roomlist={}
		for row in cursor:
			tticode=int(row["tticode"])			
			rooms[tticode]={			
			"room_id":row["room_id"],
			"hotel_id":row["hotel_id"],
			"tticode":tticode,
			"room_price":row["room_price"]
			
			}
			roomlist=cls.checkRoomOffers(rooms)
			#roomlist[row["hotel_id"]]=rooms
			#rows+=row
			#print(roomlist)
		return roomlist

	def array_merge_recursive(array1,*arrays):
		for array in arrays:
			#print(array)
			for key, value in array.items(): #sorted(array.items()): #array.items():
				#print(key)
				#for key2 ,val in array1.items():
					#print(array1.keys())
					#print(value.keys())
					if key in array1.keys():
					#if key==key2:
						#print(key)
						if isinstance(value, dict):
							array[key] = array_merge_recursive(array1[key], value)
							if isinstance(value, (list, tuple)):
								array[key] += array1[key]
								print(array)
			array1.update(array)
		return array

	def mergeDict(dict1, dict2):
		''' Merge dictionaries and keep values of common keys in list'''
		dict3 = {**dict2, **dict1}
		for key, value in dict2.items():
			#print(value)
			if key in dict1 and key in dict2:
				#print(key)
				dict3[key] = [value , dict1[key]]
		return dict3



	@classmethod
	def fetchRoomOffers(cls,Rooms,rooms):
		cursor=connection.cursor()
		meal_cursor=connection.cursor()	
		#hotellist=[979179,26384]
		#lst = [10, 50, 75, 83, 98, 84, 32]
		hotel_id=''
		#hotelid='979179'		
		#mealOffer={}	
		#for x,res in enumerate(hotellist):
		#print(x,":",res)
		hotelid=''#res				
		#print(hotelid)
		room_array={}
		#query="SELECT room_id,hotel_id,tticode,room_price,room_type FROM  roomsitravel WHERE hotel_id='979179' "#OR hotel_id='26384'
		#'SELECT room_id,hotel_id,tticode,room_price,room_type FROM  roomsitravel WHERE hotel_id=%s',(hotelid,)
		cursor.execute('SELECT room_id,hotel_id,tticode,room_price,room_type FROM  roomsitravel WHERE hotel_id=%s',(hotelid,))			
		requested_Rooms=1		
		i=0
		room_array=cursor		
		#ofer=cls.Mealslist(hotel_id,rooms,rooms_avail,roomsid)	
		#print(hotelid)	
		Avaloffers={}
		Avaloffers=cls.Mealslist(hotel_id,rooms,room_array,hotelid)	
		#print(Avaloffers)					
		return Avaloffers
		
	@classmethod
	def Mealslist(cls,hotel_id,Rooms,room_array,hid):	
		cursor=connection.cursor()
		hotellist=[979179,26384]
		mealOffer={}
		for x,res in enumerate(hotellist):
			hid=res
			#print(hid)
			cursor.execute('SELECT room_id,hotel_id,tticode,room_price,room_type FROM  roomsitravel WHERE hotel_id=%s',(hid,))
			room_array=cursor							
			i=0		
			ofer={}
			meal_cursor=connection.cursor()			
			room_data={}
			roomoffer={}
			mealdata={}		
			for items in room_array:									
				meal_hid=items["hotel_id"]							
				rid=items["room_id"]			
				room_type=items["room_type"]
				room_price=items["room_price"]
				tticode=items["tticode"]
				room_data={
				'room_id':rid,
				'room_type':'',	
				'room_price':room_price,
				'hotel_id':meal_hid,
				'tticode':tticode,						
				}
				seasonal_price=CommonModel.fetchSeasonalPrices(room_data);
				total_price=seasonal_price+float(room_price)	
				meal_cursor.execute('SELECT meal_plan,id,meal_price,hotel_id FROM Meal_Plan WHERE hotel_id=%s',(meal_hid,))
				for boards in meal_cursor:
					mealdata["minAge_range1"]=0
					mealdata["minAge_range2"]=0
					mealdata["minAge_range3"]=0
					mealdata["minAge_range4"]=0
					mealdata["maxAge_range1"]=0
					mealdata["maxAge_range2"]=0
					mealdata["maxAge_range3"]=0
					mealdata["maxAge_range4"]=0 
					mealdata["child_rage1"]=0
					mealdata["child_rage2"]=0
					mealdata["Type_of_calculation"]="ROOM"
					mealdata["meal_price"]=boards["meal_price"]
					m_price=CommonModel.getMealPrice(meal_cursor,mealdata)
					#print(m_price)
					total_meal_price=total_price+m_price+float(boards["meal_price"])					
					
					mealid=boards["id"]	
					boardiddd=f'{rid}_{mealid}'
					meal=boards["meal_plan"]
					roomoffer[boardiddd]={					
					'tticode':tticode,#rooms['tticode'],
					'room_id':rid,#rid,#rid,#rooms['room_id'],		
					'roomtype_Name':room_type,#rooms['room_type'],
					'Meal_plan':meal,#meals_plan,
					'Meal_Id':mealid,
					'Refundable': '',
					'price':total_meal_price,#''price,					
					'room_type':'',	
					'room_price':room_price,
					'hotel_id':meal_hid,
					'tticode':tticode,						
					}
					mealOffer[hid]={}
					mealOffer[hid][Rooms]={}
					mealOffer[hid][Rooms]['rooms']=roomoffer
		return mealOffer
		
			
	def offers_meals(rid,hid,roomdata,Rooms,hotel_id,seasonal_price):		
		i=0		
		mealOfferd={}
		mealOffer={}
		mealdata={}
		meal_cursor=connection.cursor()	
		innerlist=[]
		newlist = []
		meal_cursor.execute('SELECT meal_plan,id,meal_price,hotel_id FROM Meal_Plan WHERE hotel_id=%s',(hid,) )		
		for boards in meal_cursor:
			#print(rid)	
			mealdata["minAge_range1"]=0
			mealdata["minAge_range2"]=0
			mealdata["minAge_range3"]=0
			mealdata["minAge_range4"]=0
			mealdata["maxAge_range1"]=0
			mealdata["maxAge_range2"]=0
			mealdata["maxAge_range3"]=0
			mealdata["maxAge_range4"]=0 
			mealdata["child_rage1"]=0
			mealdata["child_rage2"]=0
			mealdata["Type_of_calculation"]="ROOM"
			mealdata["meal_price"]=boards["meal_price"]
			m_price=CommonModel.getMealPrice(meal_cursor,mealdata)
			#print(m_price)
			total_meal_price=m_price+float(boards["meal_price"])
			room_price=float(roomdata["room_price"])
			total_price=seasonal_price+float(roomdata['room_price'])			
			#print(rid)
			i+=1			
			meal=boards["meal_plan"]
			mealid=boards["id"]
			price=room_price+float(boards["meal_price"])			
			boardiddd=f'{rid}_{mealid}'			
			#print(boardiddd)
			mealOfferd[boardiddd]={	  
			'hotel_id':hid,
			'tticode':roomdata['tticode'],
			'room_price':float(roomdata['room_price']),
			'meal_price':total_meal_price,
			'total_price':total_price,
			'room_id':rid,	
			'roomtype_Name':'',
			'Meal_plan':meal,
			'Meal_Id':mealid,			
			'price':price,										       
			}
			mOffer={}
			#mOffer[i]=mealOfferd			
			#mealOffer[i][boardiddd]=mealOfferd			
			
			#mealOffer[Rooms]={}
			#mealOffer[hotel_id][Rooms]['rooms']=mealOfferd
			#mealOffer[Rooms]['rooms']=mealOfferd
			#mealOffer[Rooms]['rooms']=mealOfferd			
			#mealsso[i]={}
			#mealsso[i]=mealOfferd
			#print(mealOffer)
		mealOffer[hid]=mealOfferd
		#print(mealOffer)
		#print(mealOffer)
		innerlist.append(mealOffer)
		#innerlist.append(mealOfferd)	
		newlist.append(innerlist)
		#print(mealOffer)	
		return newlist

	
	
		

			
				
			

		

		        
		

	


	@classmethod
	def getMeals(cls,hid):	
		query="SELECT * FROM Meal_Plan where hotel_id='hid' limit 1"
		cursor=connection.cursor()
		cursor.execute(query)
		return cursor
		
			


		
						
            
            	
                
            	
		    	



		
            


       
           
        









	


    
    

    

               
           
        
    




       
            
               
                    
                
                   
            
    


class RoomModel():
	def __init__(self):
		pass

	def getHotelRooms(self):
		cursor=connection.cursor()
		query="SELECT * FROM roomsx  " 		
		cursor.execute(query)
		rows=[]
		for row in cursor:
			rows+=row
		return rows

	


	

			






		


	

	