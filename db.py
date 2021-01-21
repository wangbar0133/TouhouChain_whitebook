import pymongo
import json
import os
from bson import json_util

class db(object):

    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["BlockChain"]
        self.mycol = mydb["Chain"]

    def insert(self, blockJson):
        self.mycol.insert_one(blockJson)

    def getTopBlock(self):
        block = self.mycol.find().sort('_id', -1).limit(1)
        return json_util.dumps(block)

    def getChian(self):
        Chain = self.mycol.find().sort('_id')
        return json_util.dumps(Chain)

    def getChainLen(self):
        return self.mycol.count()

    def getHard(self):
        block = json_util.dumps(self.mycol.find().sort('_id', -1).limit(1))
        hard = block['headers']['hard']
        return hard

if __name__ == "__main__":
    print(db().getChainLen())



