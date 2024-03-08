import sys
import json
from urllib.parse import urlparse
from sqlalchemy import create_engine
from flaskr.configs import get_env, log_system

__db_address__ = get_env('DB_URL')
__db_info__ = urlparse(__db_address__)

sql_engine = None

if __db_info__.scheme in ['mysql', 'sqlite', 'postgres']:
    connect_option = {
        'url': __db_address__,
        # 关闭echo打印，系统配置了sqlalchemy的日志打印
        'echo': False
    }
    db_type = __db_info__.scheme

    if (__db_info__.scheme == 'mysql'):
        __db_info__ = __db_info__._replace(scheme='mysql+pymysql')
    elif (__db_info__.scheme == 'sqlite'):
        __db_info__ = __db_info__._replace(scheme='sqlite+pysqlite')
    elif (__db_info__.scheme == 'postgres'):
        __db_info__ = __db_info__._replace(scheme='postgresql+psycopg2')
    else:
        log_system.error(f'{__db_info__.scheme} is not supported')
        sys.exit(1)

    try:
        connect_option['url'] = __db_info__.geturl()

        sql_engine = create_engine(**connect_option)
        sql_engine.connect()

        log_system.info(
            f'{db_type} connected by option: ' +
            json.dumps(connect_option, indent=4, ensure_ascii=False)
        )
    except Exception as e:
        log_system.error(str(e))
        sys.exit(1)
