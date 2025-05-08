from flask import Flask
from flaskr.configs.env import get_env
from flaskr.json_encoder import JsonEncoder
from opentelemetry.instrumentation.flask import FlaskInstrumentor
import flaskr.controllers  # noqa: F401
from flaskr import v1_public_api, v1_user_api, v1_admin_api, v1_service_api


application = Flask(__name__, instance_relative_config=True)

if get_env('OTEL_ENABLED') == 'yes':
    FlaskInstrumentor().instrument_app(application)  # 自动追踪所有请求

application.json = JsonEncoder(application)

application.register_blueprint(blueprint=v1_public_api)
application.register_blueprint(blueprint=v1_user_api)
application.register_blueprint(blueprint=v1_admin_api)
application.register_blueprint(blueprint=v1_service_api)
