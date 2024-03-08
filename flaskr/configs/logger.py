import logging
import logging.config
from flaskr import app_name
from flaskr.configs.env import get_env

log_config = {
    'version': 1,
    'formatters': {
        'system': {
            '()': 'logging.Formatter',
            'fmt': f'[%(asctime)s] [%(levelname)s] [SYSTEM:{app_name}] %(message)s \n'
        },
        'sql': {
            '()': 'logging.Formatter',
            'fmt': '[%(asctime)s] [%(levelname)s] [SQL:%(name)s] %(message)s \n'
        },
        'develop': {
            '()': 'logging.Formatter',
            'fmt': '[%(asctime)s] [%(levelname)s] [%(pathname)s:%(lineno)d] %(message)s \n'
        },
        'http-request': {
            '()': 'logging.Formatter',
            'fmt': f'[%(asctime)s] [%(levelname)s] [{app_name}] ' +
            '[%(trace_id)s|%(span_id)s|%(parent_span_id)s] %(message)s \n'
        },
    },
    'handlers': {
        'system-logger': {
            'formatter': 'system',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
        'develop-logger': {
            'formatter': 'develop',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
        'http-logger': {
            'formatter': 'http-request',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
        'sql-logger': {
            'formatter': 'sql',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        }
    },
    'loggers': {
        # werkzeug和flaskr.app是框架的log配置，使用system-logger覆写
        'werkzeug': {'handlers': ['system-logger'], 'level': 'DEBUG' if get_env('ENV') == 'development' else 'ERROR'},
        # 数据库执行语句的打印
        'sqlalchemy.engine': {'handlers': ['sql-logger'], 'level': 'INFO'},
        'system': {'handlers': ['system-logger'], 'level': 'DEBUG'},
        'code-debug': {'handlers': ['develop-logger'], 'level': 'DEBUG'},
        'http-request': {'handlers': ['http-logger'], 'level': 'INFO'}
    }
}

# 配置日志
logging.config.dictConfig(log_config)

log = logging.getLogger('code-debug')
log_api = logging.getLogger('http-request')
log_system = logging.getLogger('system')
