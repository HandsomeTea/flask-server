from bson import ObjectId
import datetime
from flask.json.provider import DefaultJSONProvider


class JsonEncoder(DefaultJSONProvider):

    def default(self, data):
        if isinstance(data, ObjectId):
            return str(data)
        if isinstance(data, datetime.datetime):
            # return data.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            # return str(data)
            # return data.isoformat()
            return data.timestamp()

        return super().default(data)
