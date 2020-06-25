
import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='degraP@55w0rd', db='yt', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
from mergedeep import merge
import pandas as pd
import json

class CommonModel():	
	def __init__(self):
	    pass
    
    @classmethod
    def fetchSeasonalPrices(roomdata):
        cursor=connection.cursor()
		#meal_cursor=connection.cursor()	
		#query="SELECT room_id,hotel_id,tticode,room_price,room_type FROM  roomsitravel WHERE  hotel_id='979179'  OR hotel_id='26384'    " 
		room_id=roomdata["room_id"]
        checkindate=roomdata["checkindate"]
        checkoutdate=roomdata["checkoutdate"]
        adults=roomdata["adults"]
        children=roomdata["children"]
        nyts=roomdata["nyts"]
        max_pass=adults+children
        query = "SELECT price_id,room_id,price,min_stay,Adults,childrens,maxi_pass,seasonal_days FROM (
                "SELECT price_id,room_id,price,min_stay,Adults,childrens,maxi_pass,
                "CASE
                "WHEN 'checkoutdate'<checkout_date AND 'checkoutdate'>checkin_date
                "THEN DATEDIFF('checkoutdate',checkin_date)
                "WHEN 'checkindate'>=checkin_date AND 'checkindate'<=checkout_date
                "THEN DATEDIFF(checkout_date,'checkindate')
                "ELSE DATEDIFF(checkout_date,checkin_date)
                "END AS seasonal_days
                "FROM priceTypes rs WHERE rs.checkin_date<='checkindate' AND rs.checkout_date>='checkoutdate' OR rs.checkin_date>='checkindate' AND rs.checkin_date<='$checkoutdate' OR rs.checkout_date>='checkindate' AND rs.checkout_date<='checkoutdate' AND status='Active'
                "AND room_id='room_id'
                ")ts WHERE room_id='room_id' AND min_stay>='nyts'
                 ";
        #AND Adults>='$adults' AND  childrens>='$children'  AND  maxi_pass>='$max_pass'
        #AND min_stay>='$nyts'
        cursor.execute(query)
        $q_result=''
        #var_dump($q_result);
        #return $q_result;
        return $q_result
     @classmethod
    def booking_discount($room_id,$checkindate,$checkoutdate,$booking_date,$nyts){
        #$booking_date='7/02/2020';
        $query = "SELECT price as discount,combined,room_id,seasonal_days,status,min_stay,offer_type FROM (
                    "SELECT price,combined,room_id,status,min_stay,offer_type,
                    "CASE
                    "WHEN '$checkoutdate'<checkout_date AND '$checkoutdate'>checkin_date
                    "THEN DATEDIFF('$checkoutdate',checkin_date)
                    "WHEN '$checkindate'>=checkin_date AND '$checkindate'<=checkout_date
                    "THEN DATEDIFF(checkout_date,'$checkindate')
                    "ELSE DATEDIFF(checkout_date,checkin_date)
                    "END AS seasonal_days
                    "From  booking_discount rs where rs.checkin_date<='$checkindate' AND rs.checkout_date>='$checkoutdate' OR rs.checkin_date>='$checkindate' AND rs.checkin_date<='$checkoutdate' OR rs.checkout_date>='$checkindate' AND rs.checkout_date<='$checkoutdate' AND '$booking_date'>=booking_date AND '$booking_date'<=expiry_date  AND
                    "room_id='$room_id' AND status='Active'
                    ")t1 WHERE  room_id='$room_id' AND status='Active' AND min_stay>='$nyts' AND offer_type='Special'
                     "; //AND min_stay='$nyts' GROUP BY status,room_id HAVING
        $q_result=$this->CI->generic_class->GenericQuery($query);
            #  echo "<pre>";
            #    print_r($q_result);
            # echo "</pre>";
            #var_dump($q_result);
        return $q_result

    @classmethod
    def getMealPrice(board,adults,nights,childrenAges1,checkoutdate,checkindate){

        child_rage1=$board->child_rage1;
        child_rage2=board->child_rage2;
        typeofcalculation=board->Type_of_calculation;
        meal_price=board->meal_price;
        meal_price=meal_price*nights;
        meal_peak_price=0;
        mealid=board->id;

        childtotalprice=0;
        childtotalprice1=0;
        childtotalprice2=0;
        childtotalprice3=0;
        childtotalprice4=0;
        child_price=0;
        minAge_range1=board->minAge_range1;
        minAge_range2=board->minAge_range2;
        minAge_range3=board->minAge_range3;
        minAge_range4=board->minAge_range4;
        maxAge_range1=board->maxAge_range1;
        maxAge_range2=board->maxAge_range2;
        maxAge_range3=board->maxAge_range3;
        maxAge_range4=board->maxAge_range4;
        #foreach (childrenAges1 as key => value){
        for childrenAges1 in value:
            age=value;
            # var_dump(value.' '.board->meal_plan.' '.board->id);
            #board->minAge_range1 board->minAge_range2
            if age>=minAge_range1 && age<=maxAge_range1):
                #child_price=board->child1_Fvalue;
                childtotalprice=board->child1_Fvalue;
                #var_dump(childtotalprice.' '.board->meal_plan.' '.board->id);
            
            if age>=minAge_range2 && age<=maxAge_range2:
                #child_price=board->child2_Fvalue;
                childtotalprice2=board->child2_Fvalue;
                #childtotalprice= childtotalprice1+childtotalprice2;
                #var_dump(childtotalprice2.' '.board->meal_plan.' '.board->id);
            
            if age>=minAge_range3 && age<=maxAge_range3:
                #child_price=board->child3_Fvalue;
                childtotalprice3=board->child3_Fvalue;
                #var_dump(age.' '.board->meal_plan.' '.board->id);
                #var_dump(childtotalprice3.' '.board->meal_plan.' '.board->id);
            
            if age>=minAge_range4 && age<=maxAge_range4:
                #child_price=board->child4_Fvalue;
                childtotalprice4=board->child4_Fvalue;
                #var_dump(childtotalprice3.' '.board->meal_plan.' '.board->id);
            
        
        childtotalprice=childtotalprice+childtotalprice2+childtotalprice3+childtotalprice4;
        #var_dump(childtotalprice.' '.board->meal_plan.' '.board->id);
        if typeofcalculation=="PERSON":
                #var_dump(childtotalprice);
                mealprice=(meal_price*adults)+(childtotalprice*nights);
                #var_dump(mealprice);
               #var_dump(mealprice.' '.board->meal_plan.' '.board->id.'.....meal per person,per nite');
                #var_dump(meal_price*nights*adults.' '.board->meal_plan.' '.board->id);
                #var_dump(childtotalprice.' '.board->meal_plan.' '.board->id);
        else if(typeofcalculation=="ROOM":
                mealprice=(meal_price);#+(childtotalprice*nights);
                #var_dump(mealprice.' '.board->meal_plan.' '.board->id);
        else:
                mealprice=(meal_price*adults)+childtotalprice;
        
        peakPrice=this->getMealPeakPrice(checkoutdate,checkindate,mealid,childrenAges1,board,nights,adults,childtotalprice);
        #if(!empty(peakPrice)){
           # mealprice=peakPrice;#mealprice+peakPrice;
            #var_dump(mealprice);
        #}              
        # var_dump(mealprice.' '.board->meal_plan.' '.board->id);
        return mealprice

    @classmethod
    def getExtraSupplements(hotel_id,checkindate,checkoutdate,adults):
        #var_dump(checkindate);
        query="SELECT price,mealname,child1_price,child2_price,child3_price,child4_price,Type_of_calculation,options,
                    "CASE
                        "WHEN 'checkoutdate'<checkout_date AND 'checkoutdate'>checkin_date
                            "THEN DATEDIFF('checkoutdate',checkin_date)
                        "WHEN 'checkindate'>=checkin_date AND 'checkindate'<=checkout_date
                            "THEN DATEDIFF(checkout_date,'checkindate')
                        "ELSE
                            "DATEDIFF(checkout_date,checkin_date)
                        "END AS seasonal_days
                        "FROM  extra_supplement rs  WHERE  rs.checkin_date<='checkindate' AND rs.checkout_date>='checkoutdate' OR rs.checkin_date>='checkindate' AND rs.checkin_date<='checkoutdate' OR rs.checkout_date>='checkindate' AND rs.checkout_date<='checkoutdate' AND  options='compulsory' AND hotel_id='hotel_id'
                "
        q_result=''
        #var_dump(q_result);
        return q_result;
    