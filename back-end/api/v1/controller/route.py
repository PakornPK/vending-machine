from api.v1.models import machine, products
import json
import hashlib
from flask import Blueprint, request, jsonify
from flask.wrappers import Response
from flask_cors import CORS
from api.v1 import models



api = Blueprint('api', __name__)
CORS(api, support_credentials=True)

@api.route('/product/<mc_id>', methods=['GET'])
def getProducts(mc_id):
    productData = models.products.Product()
    return jsonify(productData.get_by_mc(mc_id))


@api.route('/machine', methods=['GET'])
def getMachines():
    machineData = models.Machine()
    data = json.dumps(machineData.get_all(), ensure_ascii=False).encode('utf8')
    response = Response(data, status=200, mimetype="application/json")
    return response

@api.route('/fillproduct/<mc_id>', methods=['GET'])
def getFillProduct(mc_id):
    productData = models.products.Product()
    data = json.dumps(productData.get_by_mc(mc_id), ensure_ascii=False).encode('utf8')
    response = Response(data, status=200, mimetype="application/json")
    return response

@api.route('/fill/<mc_id>/<pd_id>', methods=['POST'])
def FillProduct(mc_id,pd_id):
    try:
      productData = models.products.Product()
      productData.fill(mc_id,pd_id)
      return jsonify({"result" : "Ok"})
    except:
      return jsonify({"result" : "Error fill product"})

@api.route('/buy/<mc_id>/<pd_id>', methods=['POST'])
def buyItem(mc_id,pd_id):
  try:
      productData = models.products.Product()
      productData.buy(mc_id,pd_id)
      return jsonify({"result" : "Ok"})
  except:
    return jsonify({"result" : "Error buy product"})

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
