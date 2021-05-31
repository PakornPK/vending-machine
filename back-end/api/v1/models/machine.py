import mysql.connector
from api.v1.models import constance

class Machine(): 
    def get_all(self): 
        db = constance.ConstanceDb()
        with mysql.connector.connect(host=db.host, user=db.uername, password=db.password, database=db.db_name, port=db.port) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM machines")
            sqlQuery = cur.fetchall()
            conn.close()

        result = []
        for val in sqlQuery:
            result.append({
                "id": val[0],
                "location": val[1],
                "balance": val[2],
                "src": val[3],
                "reload": val[4]
            })
        return result

        
