from celery import Celery
from flaskr.configs.env import get_env

# 第一个参数celery是当前模块的名称。这只是为了在__main__模块中定义任务时可以自动生成名称。
app = Celery(
    'flaskr',
    broker=get_env('CELERY_BROKER_URL'),
    # 后端可以使用mongodb，https://docs.celeryq.dev/en/stable/userguide/configuration.html#mongodb-backend-settings
    backend=get_env('CELERY_BACKEND_URL')
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    enable_utc=False,  # celery默认使用UTC时间，这里改为使用服务器本地时间
)
