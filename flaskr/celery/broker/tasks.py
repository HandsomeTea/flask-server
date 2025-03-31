from flaskr.celery.celery import app as celery


@celery.task
def add(*args, **kwargs):
    pass

# 使用示例
# from flaskr.celery.broker.tasks import add
# add.apply_async(
#     args=(1, 2),
#     kwargs={},
#     # task_id='',  # 为任务分配唯一id，默认是uuid;
#     queue='my_queue',
#     countdown=10,  # 10秒后执行
#     priority=5,    # 优先级（0-9，数字越大优先级越高）
#     retry=True,    # 是否重试
#     shadow='test-task',  # 重新指定任务的名字str，覆盖其在日志中使用的任务名称；
#     retry_policy={
#         'max_retries': 3,  # 最大重试次数
#         'interval_start': 0,  # 第一次重试间隔时间
#         'interval_step': 1,  # 每次重试间隔时间增加的秒数
#         'interval_max': 10,  # 最大重试间隔时间
#     },
#     link=None,  # 任务执行成功后要执行的回调函数，是一个signature对象，是另一个任务的签名；可以用作关联任务；
#     # 如add.apply_async((1, 2), link=add.s(3, 4).set(queue='my_queue1'))，意为add任务执行成功后，执行add(3, 4)任务；
#     # add.apply_async((1, 2), link=add.s(3).set(queue='my_queue1'))，意为add任务执行成功后，执行add(3, 3)任务；
#     link_error=None  # 任务执行失败后要执行的回调函数，是一个signature对象，是另一个任务的签名；可以用作关联任务；
# )
