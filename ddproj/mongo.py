from pymongo import MongoClient

class DDMongoClient(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DDMongoClient, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.mgdb = MongoClient()

    def getMongoClient(self):
        return self.mgdb

