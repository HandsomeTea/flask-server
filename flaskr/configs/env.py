import os
from typing import Dict, Optional, Literal

__env_type__ = Literal[
    'ENV',
    'DB_URL'
]
__default_env__ = {
    'ENV': 'development',
    'DB_URL': 'mongodb://admin:admin@localhost:27017/flask-test?authSource=admin'
}


def get_env(key: Optional[Dict[__env_type__, str]]):
    return os.getenv(key, __default_env__.get(key))
