
import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='degraP@55w0rd', db='yt', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
from mergedeep import merge
import pandas as pd
import json

class CommonModel():
    def fetchSeasonalPrices(roomdata):
        cursor=connection.cursor()
        room_id=roomdata["room_id"]
        checkoutdate="2020-06-15"#roomdata["checkoutdate"]
        checkindate="2020-06-06"#roomdata["checkindate"]
        adults=1#roomdata["adults"]
        children=1#roomdata["children"]
        nyts=1#roomdata["nyts"]
        max_pass=adults+children
        nights=5
        room_price=float(roomdata["room_price"])
        #hotel_id=%s',(meal_hid,)
        query="""SELECT price_id,room_id,price,seasonal_days FROM (
            SELECT price_id,room_id,price,CASE WHEN 
            %(checkoutdate)s < checkout_date AND  %(checkoutdate)s > checkin_date THEN DATEDIFF(%(checkoutdate)s,checkin_date)
            WHEN %(checkindate)s >=checkin_date AND %(checkindate)s<=checkout_date
            THEN DATEDIFF(checkout_date,%(checkindate)s)
            ELSE DATEDIFF(checkout_date,checkin_date)
            END AS seasonal_days
            FROM priceTypes rs WHERE rs.checkin_date<=%(checkindate)s AND rs.checkout_date>=%(checkindate)s 
            OR rs.checkin_date>=%(checkindate)s AND rs.checkin_date<=%(checkoutdate)s OR rs.checkout_date>=%(checkindate)s 
            AND rs.checkout_date<=%(checkoutdate)s AND status='Active'
            AND room_id=%(room_id)s
            )ts WHERE room_id=%(room_id)s 
            
        """#AND min_stay>='nyts' min_stay,Adults childrens,maxi_pass
        params={'checkoutdate':checkoutdate,'checkindate':checkindate,'room_id':room_id}
        cursor.execute(query,params)
        
        #print(cursor)
        #print(query)
        #print(cursor.query.decode('utf-8'))
        total_seasonal_days=0;
        seasonal_price=0
        remaining_days=0
        #float(r_price)=0.0;
        r_price=0
        for seasons in cursor:            
            seasonal_price+=seasons["price"]*seasons["seasonal_days"]                  
            total_seasonal_days+=seasons["seasonal_days"]                                
                  
        remaining_days=abs((nights-total_seasonal_days));                  
        r_price=float((room_price*remaining_days))+float((seasonal_price))
        return r_price     




	
    def getMealPrice(mealsc,board):        
        adults=1#mealdata[""]
        nights=5#mealdata[""]
        childrenAges1=[]#mealdata[""]
        checkoutdate=0#mealdata[""]
        checkindate=''#mealdata[""]

        child_rage1=board["child_rage1"];
        child_rage2=board["child_rage2"];
        typeofcalculation=board["Type_of_calculation"];
        meal_price=float(board["meal_price"])
        meal_price=meal_price*nights;
        meal_peak_price=0;
        #mealid=board["id"];

        childtotalprice=0;
        childtotalprice1=0;
        childtotalprice2=0;
        childtotalprice3=0;
        childtotalprice4=0;
        child_price=0;
        minAge_range1=board["minAge_range1"]
        minAge_range2=board["minAge_range2"]
        minAge_range3=board["minAge_range3"]
        minAge_range4=board["minAge_range4"]
        maxAge_range1=board["maxAge_range1"]
        maxAge_range2=board["maxAge_range2"]
        maxAge_range3=board["maxAge_range3"]
        maxAge_range4=board["maxAge_range4"]       
        for age  in childrenAges1:
            #age=value           
            if age>=minAge_range1 and  age<=maxAge_range1:
                childtotalprice=board["child1_Fvalue"]               
            
            if age>=minAge_range2 and  age<=maxAge_range2:               
                childtotalprice2=board["child2_Fvalue"]              
            
            if age>=minAge_range3 and  age<=maxAge_range3:               
                childtotalprice3=board["child3_Fvalue"]               
            
            if age>=minAge_range4 and  age<=maxAge_range4:               
                childtotalprice4=board["child4_Fvalue"]               
            
        
        childtotalprice=childtotalprice+childtotalprice2+childtotalprice3+childtotalprice4;
       
        if  typeofcalculation=="PERSON":               
                mealprice=(meal_price*adults)+(childtotalprice*nights);
               
        elif typeofcalculation=="ROOM":
            mealprice=(meal_price)               
        else:
            mealprice=(meal_price*adults)+childtotalprice        
        #peakPrice=this->getMealPeakPrice(checkoutdate,checkindate,mealid,childrenAges1,board,nights,adults,childtotalprice);
        #if(!empty(peakPrice)){
           # mealprice=peakPrice;#mealprice+peakPrice;
            #var_dump(mealprice);
        #}              
        # var_dump(mealprice.' '.board->meal_plan.' '.board->id);
        return mealprice
   
  
    def getExtraSupplements(hotel_id,checkindate,checkoutdate,adults):        
        query="""SELECT price,mealname,child1_price,child2_price,child3_price,child4_price,Type_of_calculation,options,
                    CASE
                        WHEN  %(checkoutdate)s < checkout_date AND  %(checkoutdate)s > checkin_date
                            "THEN DATEDIFF( %(checkoutdate)s,checkin_date)
                        WHEN  %(checkintdate)s >= checkin_date AND  %(checkindate)s <= checkout_date
                            "THEN DATEDIFF(checkout_date, %(checkindate)s)
                        ELSE
                            "DATEDIFF(checkout_date,checkin_date)
                        END AS seasonal_days
                        FROM  extra_supplement rs  WHERE  rs.checkin_date<= %(checkindate)s AND rs.checkout_date>= %(checkoutdate)s OR rs.checkin_date>='checkindate' AND rs.checkin_date<='checkoutdate' OR rs.checkout_date>='checkindate' AND rs.checkout_date<='checkoutdate' AND  options='compulsory' AND hotel_id='hotel_id'
                """
        params={'checkoutdate':checkoutdate,'checkindate':checkindate}
        cursor.execute(query,params)
        for supp in cursor:
            extra_price=supp["price"]                    
            #$board_price=$board_price+$extra_price;
        return extra_price
    
    