from flaskr import app_name
from flaskr.app import application
from flaskr.configs import get_env, log_system
import flaskr.db  # noqa: F401
import flaskr.middlewares  # noqa: F401

__run_config__ = {
    'port': 5001,
    'debug': False
}

if (get_env('ENV') == 'development'):
    __run_config__.update({
        'debug': True
    })

if __name__ == '__main__':
    log_system.info(f'{app_name} is running on port {__run_config__.get("port")}')
    application.run(**__run_config__)
