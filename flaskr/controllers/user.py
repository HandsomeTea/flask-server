from flask import request
from flaskr.app import application
from flaskr.configs import HttpError, ErrorCode, log
# from flaskr.models import Users


@application.post('/test')
def test():
    return 'success'
    return {
        'data': 123
    }
    raise HttpError('Invalid username or password', ErrorCode.UNAUTHORIZED)


@application.post('/dbtest')
def login():
    # 这个接口的数据库操作全部用的是mysql
    # Users.create({'name': '222', 'age': 12})

    # return 'success'
    # findone = Users.find_one({'id': 1})
    # print(findone)
    # print(findone.id)
    # return findone.to_dict()

    # findmany = Users.find_many({'name': '222'})
    # print(findmany)
    # print(findmany[0].id)
    # # return Users.find_many({'name': '222'}, to_dict=True)
    # return [item.to_dict() for item in findmany]
    # pages = Users.paginate(query={'name': '222'}, page=1, limit=5)
    # print(pages, pages['data'])
    # print(pages['data'][0]['id'])
    # return pages

    # Users.update_one(query={'id': '1'}, set={'name': '123123'})
    # return 'success'

    # Users.update_many(query={'id': '1'}, set={'name': '222'})
    # return 'success'

    # Users.delete_one({'id': '1'})
    # return 'success'

    # Users.delete_many({'name': '222'})
    # return 'success'

    # count = Users.count({'name': '222'})
    # print(count, type(count))
    # return {'count': count}

    body = request.get_json()
    log.debug(body)
    log.debug(type(body))

    return {'result': 'success'}


@application.get('/dbtest')
def get_user_list():
    # 这个接口的数据库操作全部用的是mongodb
    # insert = Users.insert_one({
    #     'name': 'test',
    #     'enable': True,
    #     'age': 18,
    #     'data': {'a': 1, 'b': 2},
    #     'role': ['a', 'b']
    # })
    # print(insert)
    # print(insert.name, insert.role[0], insert.data['a'], insert.enable, insert.id, insert.createdAt)

    # return insert.to_dict()

    # insertmany1 = Users.insert_many([{
    #     'name': 'test1',
    #     'enable': False,
    #     'age': 18,
    #     'data': {'a': 3, 'b': 4},
    #     'role': ['c']
    # }])
    # print(insertmany1)
    # print(
    #     insertmany1[0].name,
    #     insertmany1[0].role[0],
    #     insertmany1[0].data['a'],
    #     insertmany1[0].enable,
    #     insertmany1[0].id
    # )
    # return [item.to_dict() for item in insertmany1]

    # insertmany2 = Users.insert_many([{
    #     'name': 'test1',
    #     'enable': False,
    #     'age': 18,
    #     'data': {'a': 3, 'b': 4},
    #     'role': ['c']
    # }], to_dict=True)
    # print(insertmany2)
    # print(
    #     insertmany2[0]['name'],
    #     insertmany2[0]['role'][0],
    #     insertmany2[0]['enable'],
    #     insertmany2[0]['_id']
    # )
    # return insertmany2

    # findone = Users.find_one({'name': 'test1'})
    # print(findone)
    # print(findone.name, findone.role[0], findone.data['a'], findone.enable, findone.id)

    # return findone.to_dict()

    # findbyid = Users.find_by_id('65e97f0ed79c706e23fc9436')
    # print(findbyid)
    # print(findbyid.name, findbyid.role[0], findbyid.data['a'], findbyid.enable, findbyid.id)

    # return findbyid.to_dict()

    # findmany1 = Users.find_many({'name': 'lhf'})
    # print(findmany1)
    # print(
    #     findmany1[0].name,
    #     findmany1[0].role[0],
    #     findmany1[0].data['a'],
    #     findmany1[0].enable,
    #     findmany1[0].id
    # )
    # return [item.to_dict() for item in findmany1]

    # findmany2 = Users.find_many({'name': 'lhf'}, to_dict=True)
    # print(findmany2)
    # print(
    #     findmany2[0]['name'],
    #     findmany2[0]['role'][0],
    #     findmany2[0]['enable'],
    #     findmany2[0]['_id']
    # )
    # return findmany2

    # page = Users.paginate(query={'name': 'lhf'}, page=1, limit=5)
    # print(page)
    # print(page['data'][0]['_id'])

    # return page

    # Users.delete_one({'name': 'test1'})
    # return {'count': Users.count({'name': 'test1'})}

    # print(Users.find_by_id('65ea925ba161288a50777349').to_dict())
    # Users.delete_by_id('65ea925ba161288a50777349')
    # return {'count': Users.count({'_id': '65ea925ba161288a50777349'})}

    # Users.delete_many({'name': 'test'})
    # return {'count': Users.count({'name': 'test'})}

    # Users.update_one(query={'id': '65ea9238edbeeda5f5341d11'}, set={'name': '123123'})
    # return Users.find_by_id('65ea9238edbeeda5f5341d11').to_dict()

    # Users.update_by_id('65ea9238edbeeda5f5341d11', set={'name': 'ssssssssssss'})
    # return Users.find_by_id('65ea9238edbeeda5f5341d11').to_dict()

    # Users.update_many(query={'name': 'lhf'}, set={'name': 'lhf1'})
    # return {'count': Users.count({'name': 'lhf'})}

    # count = Users.count({'name': 'lhf1'})
    # print(count, type(count))
    # return {'count': count}

    query = request.args.to_dict()
    log.debug(query)
    log.debug(type(query))
    return 'success'
