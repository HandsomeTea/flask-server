from flask import Flask
from flaskr.json_encoder import JsonEncoder
import flaskr.controllers  # noqa: F401
from flaskr import v1_public_api, v1_user_api, v1_admin_api, v1_service_api


application = Flask(__name__, instance_relative_config=True)
application.json = JsonEncoder(application)

application.register_blueprint(blueprint=v1_public_api)
application.register_blueprint(blueprint=v1_user_api)
application.register_blueprint(blueprint=v1_admin_api)
application.register_blueprint(blueprint=v1_service_api)
