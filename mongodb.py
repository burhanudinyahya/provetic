import pymongo, os

class Mongo:

    @staticmethod
    def connect():
        try:
            mongo_url = os.environ['MONGODB_URL']
        except KeyError as e:
            mongo_url = 'mongodb://localhost:27017/'

        client = pymongo.MongoClient(mongo_url)
        return client['twitter']