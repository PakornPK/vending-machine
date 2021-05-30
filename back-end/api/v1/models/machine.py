import mysql.connector
from api.v1.models import constance

class Machine(): 
    def __init__(self,id) -> None:
        self.id = id
    
