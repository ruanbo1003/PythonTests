
from pymongo import MongoClient


class CommJson():
    def __init__(self):
        self.path = "comm"
        self.path_name = "公共"

        self.item_name = "meeting_base"
        self.desp = "会议基本字段"
        self.json = {
            "uuid": {
                "type": "string",
                "dest": "UUID",
                "default": "1234567890abcd"
            },
            "title": {
                "type": "string",
                "dest": "会议名称",
                "default": "2018年第一次业绩会"
            },
        }

    def to_mongo(self):
        mongo_json = {
            "path": self.path,
            "item_name": self.item_name,
            "json": self.json
        }

        return mongo_json


class MeetingDetial():
    pass


client = MongoClient("127.0.0.1", 27017)
db = client.db

api_coll = db.api_test

cj = CommJson()
mongo_json = cj.to_mongo()

ret = api_coll.insert_one(mongo_json)

print(ret)
