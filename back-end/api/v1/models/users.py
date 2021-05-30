import mysql.connector
from api.v1.models import constance

class Users(): 
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password
    
    def authunLogin(self) -> bool: 
        db = constance.ConstanceDb()
        with mysql.connector.connect(host=db.host,user=db.uername,password=db.password,database=db.db_name,port=db.port) as conn: 
            cur = conn.cursor()
            cur.execute("SELECT username,user_password FROM users")
            sqlQuery = cur.fetchall()
            conn.close()   
        
        for qr in sqlQuery: 
            if self.username in qr[0] and self.password in qr[1]:
                return True
            else: 
                return False