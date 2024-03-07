from urllib.parse import urlparse, parse_qs
from mongoengine import connect
from flaskr.configs import get_env


__db_info__ = urlparse(get_env('DB_URL'))

if __db_info__.scheme == 'mongodb':
    connect_option = {
        'db': __db_info__.path[1:],
        'host': __db_info__.hostname,
        'port': __db_info__.port,
        'username': __db_info__.username,
        'password': __db_info__.password,
        'authentication_source': ','.join(parse_qs(__db_info__.query).get('authSource', ['admin'])),
    }
    connect(**connect_option)
