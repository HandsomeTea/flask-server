from datetime import datetime
from mongoengine import StringField, IntField, BooleanField, DictField, ListField, DateTimeField
from flaskr.models.mongodb.base import BaseModel


class Users(BaseModel):
    _collection_name = 'users'
    meta = {'async': True}

    name = StringField()
    enable = BooleanField()
    age = IntField()
    data = DictField()
    role = ListField()
    createdAt = DateTimeField(default=datetime.now())
    updatedAt = DateTimeField(default=datetime.now())
