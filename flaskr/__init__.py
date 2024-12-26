from flask import Blueprint

# 当前服务器名称
app_name = 'user-manager'

v1_public_api = Blueprint('v1-public-api', __name__, url_prefix='/api/projectpub/usermanager/v1')
v1_admin_api = Blueprint('v1-admin-api', __name__, url_prefix='/api/projectadm/usermanager/v1')
v1_service_api = Blueprint('v1-service-api', __name__, url_prefix='/api/projectsvc/usermanager/v1')
v1_user_api = Blueprint('v1-user-api', __name__, url_prefix='/api/project/usermanager/v1')
