import pymongo
from sensor.constant.database import DATABASE_NAME

import certifi
ca=certifi.where()

class MongoDbClient:
    client=None
    def __init__(self,database_name=DATABASE_NAME):
        try:
            if MongoDbClient.client is None:
                mongo_db_url="mongodb+srv://Poonam:<password>@cluster0.g2gqd10.mongodb.net/test"
                MongoDbClient.client=pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
            self.client=MongoDbClient.client
            self.database=self.client[database_name]
            self.database_name=database_name
        except Exception as e:
            raise e
