from flaskr.celery.celery import app


app.conf.update(
    include=['flaskr.celery.worker.tasks']
)

if __name__ == '__main__':
    app.start()

# 启动worker
# celery --app=flaskr.celery.worker.server worker --loglevel=info --queues=[自定义监听队列名称，多个逗号分隔，默认为celery]
