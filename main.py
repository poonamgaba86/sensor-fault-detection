from sensor.configuration.mongo_db_connection import MongoDbClient

if __name__=='__main__':
    mongodb_client=MongoDbClient()
    print(mongodb_client.database.list_collection_names())