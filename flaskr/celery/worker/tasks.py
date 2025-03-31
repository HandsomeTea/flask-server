from flaskr.celery.celery import app


@app.task(
    # 如果为true，任务的第一个参数将是任务实例本身
    bind=True,
    queue='my_queue',
    ignore_result=False,
    # 任务将在执行完成后才发送确认消息
    acks_late=True,
    # 设置在特定异常时重试任务
    # autoretry_for=(Exception,),
    # 引入抖动，避免重试任务集中执行
    retry_jitter=True
)
def add(self, x, y):
    return x + y
