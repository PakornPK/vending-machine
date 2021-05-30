import json
import hashlib
from flask import Blueprint, request, jsonify
from flask.wrappers import Response
from flask_cors import CORS
from api.v1 import models



api = Blueprint('api', __name__)
CORS(api, support_credentials=True)

@api.route('/product', methods=['GET'])
def getProducts():
    productData = [
        {
          "src":
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075425/51021628_P.jpg",
          "name": "นกพิราบผักกาดดองเค็มฝาดึง 230 กรัม",
          "price": 32.00,
          "stock": 20 
        },
        {
          "src":
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2018/03/06112105/51009434_P.jpg",
          "name": "ซีเล็คทูน่าสเต็กในน้ำเกลือ 165 กรัม",
          "price": 49.00,
          "stock": 20 
        },
        {
          "src":
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075341/51011628_P.jpg",
          "name": "อะยัมซาร์ดีนในซอสมะเขือเทศ 155 กรัม",
          "price": 36.00,
          "stock": 20 
        },
        {
          "src":
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12075429/51021847_P.jpg",
          "name": "ยูเอฟซี เงาะในน้ำเชื่อม 565 กรัม",
          "price": 82.00,
          "stock": 20 
        },
        {
          "src":
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222505/51010586_P.jpg",
          "name": "เอ็ม-150 150 มิลลิลิตร",
          "price": 10.00,
          "stock": 20 
        },
        {
          "src":
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222438/51008429_P.jpg",
          "name": "สปอนเซอร์ 250 มิลลิลิตร",
          "price": 10.00,
          "stock": 20 
        },
        {
          "src":
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222756/51033939_P.jpg",
          "name": "ลิปตัน เลมอนขวด 445 มิลลิลิตร",
          "price": 20.00,
          "stock": 20 
        },
        {
          "src":
            "https://cpfmcdn.bygodigit.net/wp-content/uploads/2020/02/12222141/51037887_P.jpg",
          "name": "จับใจ สูตรจับเลี้ยง 500 มิลลิลิตร",
          "price": 15.00,
          "stock": 20 
        },
      ]
    return jsonify(productData)


@api.route('/machine', methods=['GET'])
def getMachines():
    machineData = [
        {
            "location": "หน้าโรงงาน",
            "src":
            "https://www.scg.com/images/th/05sustainability_development/develop/env2.jpg",
        },
        {
            "location": "หน้าโรงเรียน",
            "src": "http://teen.mthai.com/app/uploads/2015/12/bbpschool-okkk.jpg",
        },
        {
            "location": "หน้าโรงพยบาล",
            "src":
            "https://ww2.bangkokhospital.com/assets/theme/bangkok/assets/images/corparate/thumb_xs.jpg",
        }
    ]
    data = json.dumps(machineData, ensure_ascii=False).encode('utf8')
    response = Response(data, status=200, mimetype="application/json")
    return response

@api.route('/adimmachine', methods=['GET'])
def getAdminMachines():
    adminMachineData = [
        {
          "id": 1,
          "location": "หน้าโรงงาน",
          "balance": 0,
          "reload": False
        },
        {
          "id": 2,
          "location": "หน้าโรงเรียน",
          "balance": 0,
          "reload": False
        },
        {
          "id": 3,
          "location": "หน้าโรงพยบาล",
          "balance": 0,
          "reload": False
        },
      ]
    data = json.dumps(adminMachineData, ensure_ascii=False).encode('utf8')
    response = Response(data, status=200, mimetype="application/json")
    return response

@api.route('/fillproduct', methods=['GET'])
def getFillProduct():
    fillData = [
        {
          "id": 1,
          "name": "นกพิราบผักกาดดองเค็มฝาดึง 230 กรัม",
          "categorie": "อาหารกระป๋อง",
          "price": 32.00,
          "qty": 20,
          "reload": False,
        },
        {
          "id": 2,
          "name": "ซีเล็คทูน่าสเต็กในน้ำเกลือ 165 กรัม",
          "categorie": "อาหารกระป๋อง",
          "price": 49.00,
          "qty": 20,
          "reload": False,
        },
        {
          "id": 3,
          "name": "อะยัมซาร์ดีนในซอสมะเขือเทศ 155 กรัม",
          "categorie": "อาหารกระป๋อง",
          "price": 36.00,
          "qty": 20,
          "reload": False,
        },
        {
          "id": 4,
          "name": "ยูเอฟซี เงาะในน้ำเชื่อม 565 กรัม",
          "categorie": "อาหารกระป๋อง",
          "price": 82.00,
          "qty": 20,
          "reload": False,
        },
        {
          "id": 5,
          "name": "เอ็ม-150 150 มิลลิลิตร",
          "categorie": "เครื่องดื่ม",
          "price": 10.00,
          "qty": 20,
          "reload": False,
        },
        {
          "id": 6,
          "name": "สปอนเซอร์ 250 มิลลิลิตร",
          "categorie": "เครื่องดื่ม",
          "price": 10.00,
          "qty": 20,
          "reload": False,
        },
        {
          "id": 7,
          "name": "ลิปตัน เลมอนขวด 445 มิลลิลิตร",
          "categorie": "เครื่องดื่ม",
          "price": 20.00,
          "qty": 20,
          "reload": False,
        },
        {
          "id": 7,
          "name": "จับใจ สูตรจับเลี้ยง 500 มิลลิลิตร",
          "categorie": "เครื่องดื่ม",
          "price": 15.00,
          "qty": 20,
          "reload": False,
        },
      ]
    
    data = json.dumps(fillData, ensure_ascii=False).encode('utf8')
    response = Response(data, status=200, mimetype="application/json")
    return response


@api.route('/login', methods=['POST'])
def doLogin():
  data = request.json
  username = data['username'] 
  raw_pass = data['password'] 
  password = (hashlib.sha512(raw_pass.encode())).hexdigest()
  ur = models.Users(username,password)

  if ur.authunLogin() :
    return jsonify({"result" : "Ok"})
  else: 
    return jsonify({"result" : "username or password is wrong"})
