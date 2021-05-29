from flask import Flask
from api.v1 import api as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/v1')
app.run(host='0.0.0.0')
