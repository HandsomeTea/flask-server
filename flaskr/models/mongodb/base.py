import json
from datetime import datetime
from mongoengine import Document
from mongoengine.queryset.base import BaseQuerySet
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

    def __deal_id__(query):
        if (type(query) is dict and '_id' in query):
            query['id'] = query.pop('_id')

        return query

    @classmethod
    def insert_one(self, data, to_dict=False):
        if (type(data) is not dict or type(data) is dict and len(data) <= 0):
            return
        result = self(**data).save()

        if (to_dict):
            return self.to_dict(result)
        return result

    @classmethod
    def insert_many(self, data, to_dict=False):
        if (type(data) is not list or type(data) is list and len(data) <= 0):
            return
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
    def find_one(self, query={}, to_dict=False):
        if (type(query) is not dict):
            return None

        query = self.__deal_id__(query)
        result = self.objects(**query).first()

        if (to_dict):
            return self.to_dict(result)

        return result

    @classmethod
    def find_by_id(self, id: str, to_dict=False):
        return self.find_one(query={'_id': id}, to_dict=to_dict)

    @classmethod
    def find_many(self, query={}, to_dict=False):
        if (type(query) is not dict):
            return []

        query = self.__deal_id__(query)
        result = self.objects(**query).all()

        if (to_dict):
            return self.to_dict(result)

        return result

    @classmethod
    def paginate(self, page, per_page, query={}, to_dict=False):
        if (type(query) is not dict):
            return {
                'items': [],
                'total': 0,
                'per': per_page,
                'page': page
            }

        query = self.__deal_id__(query)
        result = self.objects(**query).paginate(page, per_page)

        return {
            'items': self.to_dict(result.items) if to_dict is True else result.items,
            'total': result.total,
            'per': result.per_page,
            'page': result.page
        }

    @classmethod
    def count(self, query={}) -> int:
        if (type(query) is not dict):
            return 0

        query = self.__deal_id__(query)
        return self.objects(**query).count()

    @classmethod
    def to_dict(self, data):
        try:
            if isinstance(data, BaseQuerySet) or type(data) is list:
                return [item.to_mongo().to_dict() for item in data]
            else:
                return data.to_mongo().to_dict()
        except InvalidDocumentError:
            return data
