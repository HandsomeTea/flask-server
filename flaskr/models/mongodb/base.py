import json
from datetime import datetime
from mongoengine import Document
from mongoengine.errors import InvalidDocumentError


class BaseModel(Document):
    meta = {'abstract': True}

    def __repr__(self):
        return json.dumps(
            json.loads(self.to_json()),
            ensure_ascii=False,
            indent=4
        )

    def __str__(self):
        return self.__repr__()

    def __validate_query_id__(query):
        if (type(query) is dict and '_id' in query):
            query['id'] = query.pop('_id')

        return query

    def to_dict(self):
        try:
            if type(self) is list:
                return [item.to_mongo().to_dict() for item in self]
            else:
                return self.to_mongo().to_dict()
        except InvalidDocumentError:
            return self

    @classmethod
    def insert_one(self, data):
        if (type(data) is not dict or type(data) is dict and len(data) <= 0):
            return
        return self(**data).save()

    @classmethod
    def insert_many(self, data, to_dict=False):
        if (type(data) is not list or type(data) is list and len(data) <= 0):
            return []
        result = self.objects.insert([self(**d) for d in data])

        if (to_dict):
            return self.to_dict(result)
        return result

    @classmethod
    def delete_one(self, query) -> None:
        if (
            type(query) is not dict or
            type(query) is dict and
            len(query) <= 0
        ):
            return

        data = self.find_one(query)

        if data is not None:
            data.delete()

    @classmethod
    def delete_by_id(self, id) -> None:
        self.delete_one({'_id': id})

    @classmethod
    def delete_many(self, query) -> None:
        if (
            type(query) is not dict or
            type(query) is dict and
            len(query) <= 0
        ):
            return

        datas = self.find_many(query)

        if (len(datas) > 0):
            datas.delete()

    @classmethod
    def update_one(self, query, set) -> None:
        if (
            type(query) is not dict or
            type(set) is not dict or
            type(query) is dict and
            len(query) == 0 or
            type(set) is dict and
            len(set) == 0
        ):
            return
        data = self.find_one(query)

        if data is not None:
            if 'updatedAt' in self._fields:
                set['updatedAt'] = datetime.now()
            data.update(**set)

    @classmethod
    def update_by_id(self, id, set) -> None:
        self.update_one({'_id': id}, set)

    @classmethod
    def update_many(self, query, set) -> None:
        if (
            type(query) is not dict or
            type(set) is not dict or
            type(query) is dict and
            len(query) == 0 or
            type(set) is dict and
            len(set) == 0
        ):
            return

        datas = self.find_many(query)

        if (len(datas) > 0):
            if 'updatedAt' in self._fields:
                set['updatedAt'] = datetime.now()
            datas.update(**set)

    @classmethod
    def find_one(self, query={}):
        if (type(query) is not dict):
            return None

        query = self.__validate_query_id__(query)
        return self.objects(**query).first()

    @classmethod
    def find_by_id(self, id: str):
        return self.objects(id=id).first()

    @classmethod
    def find_many(self, query={}, to_dict=False):
        if (type(query) is not dict):
            return []

        query = self.__validate_query_id__(query)
        result = self.objects(**query).all()

        if (to_dict):
            return self.to_dict(result)

        return result

    @classmethod
    def paginate(self, page, limit, query={}):
        if (type(query) is not dict):
            return {
                'data': [],
                'total': 0,
                'limit': limit,
                'page': page
            }

        query = self.__validate_query_id__(query)
        result = self.objects(**query).limit(limit).skip((page - 1) * limit)

        print('========', result)
        return {
            'data': [item.to_dict() for item in result],
            'total': self.count(query),
            'limit': limit,
            'page': page
        }

    @classmethod
    def count(self, query={}) -> int:
        if (type(query) is not dict):
            return 0

        query = self.__validate_query_id__(query)
        return self.objects(**query).count()
