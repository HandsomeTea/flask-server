from flask import request
from flaskr.app import application
from flaskr.configs import HttpError, ErrorCode, log
from flaskr.models import Users


@application.post('/list')
def login():
    body = request.get_json()
    log.debug(body)
    log.debug(type(body))
    if ('account' not in body or 'password' not in body):
        raise HttpError('Invalid username or password', ErrorCode.UNAUTHORIZED)
    return {
        'user_id': '123456789'
    }


@application.get('/list')
def get_user_list():
    # return 'success'
    # return {
    #     'result': 'test 123'
    # }
    # raise HttpError('Invalid username or password', ErrorCode.UNAUTHORIZED)
    # users = Users.find_one({'_id': '65e97c2c6d4f228352ffe02b', 'name': 'lhf'}, to_dict=True)
    # Users.update_by_id('65e97c2c6d4f228352ffe02b', {
    #     'name': 'lhf'
    # })
    users = Users.insert_many([{
        'name': 'lhf',
        'age': 18,
        'enable': False,
        'data': {'a': 1, 'b': 2},
        'role': ['admin', 'user']
    }], to_dict=True)

    return users
