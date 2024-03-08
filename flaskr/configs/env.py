import os
from typing import Dict, Optional, Literal

__env_type__ = Literal[
    'ENV',
    'DB_URL'
]
__default_env__ = {
    'ENV': 'development',
    'DB_URL': 'mongodb://admin:admin@localhost:27017/flask-test?authSource=admin'
    # 'DB_URL': 'mysql://root:root@0.0.0.0:3306/flask-test'
}


def get_env(key: Optional[Dict[__env_type__, str]]):
    return os.getenv(key, __default_env__.get(key))
