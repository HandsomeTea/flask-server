from flask import Flask
from flaskr.json_encoder import JsonEncoder

application = Flask(__name__, instance_relative_config=True)
application.json = JsonEncoder(application)
