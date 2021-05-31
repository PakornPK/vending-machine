import mysql.connector
from api.v1.models import constance

class Product(): 
    def get_by_mc(self,mc_id): 
        db = constance.ConstanceDb()
        with mysql.connector.connect(host=db.host, user=db.uername, password=db.password, database=db.db_name, port=db.port) as conn:
            cur = conn.cursor()
            cur.execute("select products.id,machine_product.machine_id,products.name,products.unit_price,products.path_img,machine_product.product_qty from machine_product left join products on machine_product.product_id = products.id where machine_product.machine_id =" + str(mc_id))
            sqlQuery = cur.fetchall()
            conn.close()

        result = []
        for val in sqlQuery:
            result.append({
                "id": val[0],
                "machine_id": val[1],
                "name": val[2],
                "unit_price": val[3],
                "scr": val[4],
                "stock" : val[5],
                "reload" : True if val[5] < 10 else False
            })
        return result

    def fill(self,mc_id,pd_id): 
        db = constance.ConstanceDb()
        with mysql.connector.connect(host=db.host, user=db.uername, password=db.password, database=db.db_name, port=db.port) as conn:
            cur = conn.cursor()
            cur.execute("update machine_product set product_qty = 20 where product_id = "+ str(pd_id) +" and machine_id = " + str(mc_id))
            conn.commit()
            conn.close()

    def buy(self,mc_id,pd_id): 
        db = constance.ConstanceDb()
        with mysql.connector.connect(host=db.host, user=db.uername, password=db.password, database=db.db_name, port=db.port) as conn:
            cur = conn.cursor()
            cur.execute("update machine_product set product_qty = (product_qty-1) where product_id = "+ str(pd_id) +" and machine_id = " + str(mc_id))
            conn.commit()
            conn.close()

        