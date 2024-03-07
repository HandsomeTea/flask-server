from flask import request
from flaskr.app import application
from flaskr.configs import HttpError, ErrorCode, log


@application.post('/list')
def login():
    body = request.get_json()
    log.debug(body)
    log.debug(type(body))
    # raise HttpError('Invalid username or password', ErrorCode.UNAUTHORIZED)
    return {
        'user_id': '123456789'
    }


@application.get('/list')
def get_user_list():
    # return 'success'
    # return {
    #     'result': 'test 123'
    # }
    raise HttpError('Invalid username or password', ErrorCode.UNAUTHORIZED)
