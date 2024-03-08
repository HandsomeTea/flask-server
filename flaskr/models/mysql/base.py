import json
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from flaskr.db.mysql import sql_engine

__base__ = declarative_base()
__session__ = Session(sql_engine)
Migrate = __base__


class BaseModel(__base__):
    __abstract__ = True
    model = __session__

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4, default=str, ensure_ascii=False)

    def __str__(self):
        return self.__repr__()

    def to_dict(dara):
        return {c.name: getattr(dara, c.name, None) for c in dara.__table__.columns}

    @classmethod
    def query(self):
        return __session__.query(self)

    @classmethod
    def create(self, data):
        if (type(data) is not dict or type(data) is dict and len(data) <= 0):
            return

        __session__.add(self(**data))
        __session__.commit()

    @classmethod
    def delete_one(self, query):
        if (type(query) is not dict or type(query) is dict and len(query) <= 0):
            return

        del_data = self.find_one(query)

        if (del_data is not None):
            __session__.delete(del_data)
            __session__.commit()

    @classmethod
    def delete_many(self, query):
        if (type(query) is not dict or type(query) is dict and len(query) <= 0):
            return

        __session__.query(self).filter_by(**query).delete(synchronize_session=False)
        __session__.commit()

    @classmethod
    def update_one(self, query, set):
        if (
            type(query) is not dict or
            type(set) is not dict or
            type(query) is dict and
            len(query) == 0 or
            type(set) is dict and
            len(set) == 0
        ):
            return
        update_data = self.find_one(query)

        if (update_data is not None):
            for key, value in set.items():
                setattr(update_data, key, value)
            __session__.commit()

    @classmethod
    def update_many(self, query, set):
        if (
            type(query) is not dict or
            type(set) is not dict or
            type(query) is dict and
            len(query) == 0 or
            type(set) is dict and
            len(set) == 0
        ):
            return
        __session__.query(self).filter_by(**query).update(set, synchronize_session=False)
        __session__.commit()

    @classmethod
    def find_one(self, query={}):
        if (type(query) is not dict):
            return None

        return __session__.query(self).filter_by(**query).first()

    @classmethod
    def find_many(self, query={}, to_dict=False):
        if (type(query) is not dict):
            return []
        result = __session__.query(self).filter_by(**query).all()
        if (to_dict):
            result = [item.to_dict() for item in result]
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

        result = __session__.query(self).filter_by(**query).limit(limit).offset((page - 1) * limit).all()

        return {
            'data': [item.to_dict() for item in result],
            'total': self.count(query),
            'limit': limit,
            'page': page
        }

    @classmethod
    def count(self, query={}):
        if (type(query) is not dict):
            return 0
        return __session__.query(self).filter_by(**query).count()
