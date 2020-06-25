


#import mysql.connector
#from mysql.connector import Error
#from mysql.connector import pooling
#from DBUtils.PooledDB import PooledDB
import pymysql
from pymysqlpool.pool import Pool
class HotelDb():  
	
    
    def connection_pool():
        #pymysql.connect(host='localhost', port=3306, user='root', passwd='degraP@55w0rd', db='yt', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        DB="yt"
        PASSWORD="degraP@55w0rd"
        USER="root"
        PORT=3306
        HOST='localhost'
        pool = Pool(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DB)
        pool.init()
        connection = pool.get_conn()
        cur = connection.cursor()
        return cur 
        
    @classmethod
    def test(cls):
        cursor=cls.connection_pool()
        sql='SELECT * FROM members limit 3'
        cursor.execute(sql)
        cursor.fetchone()       
        for row in cursor:
            username=row["email"]			
            print(username)
        #pool.release(connection)
    
