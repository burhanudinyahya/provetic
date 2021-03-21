import json, os, time, sys
from datetime import datetime
from helper import most_common as mc
from mongodb import Mongo as db

"""For consistent datetime format"""
os.environ['TZ'] = 'Asia/Jakarta'
time.tzset()

class Posts(object):


    def __init__(self):
        self._database = db.connect()
        self._collection = self._database['posts']


    def topwords(self):
        words = self._collection.find({}, {'text':1})

        words_list = []
        for word in words:
            words_list.append(word['text'])

        all_words = " ".join(words_list).split()
        return mc(all_words)


    def popular_users(self):
        users = self._collection.find({}, {'fromuser':1})

        users_list = []
        for user in users:
            users_list.append(user['fromuser'])

        return mc(users_list)


    def popular_mentions(self):
        users = self._collection.find({}, {'mentions':1})

        users_list = []
        for user in users:
            try:
                for mens in user['mentions']:
                    users_list.append(mens)
            
            except Exception as e:
                continue

        return mc(users_list)


    def hourly(self):
        time = self._collection.find({}, {'createdat':1})

        hours = []
        for h in range(24):
            h = '0' + str(h) if h < 10 else str(h)
            hours.append([h, 0])

        for t in time:
            dt_obj = datetime.fromtimestamp(t['createdat'])
            hour = datetime.strftime(dt_obj, '%H')
            hours[int(hour)] = [hour, hours[int(hour)][1] + 1]

        return json.dumps(dict(hours))


    def bulk_insert(self):
        try:
            with open("datasetfinal.json") as f:
                data = json.load(f)

            print("Read dataset")
        except Exception as e:
            print(e)
            sys.exit(1)

        try:
            self._collection.drop()  
            print("Drop collection, for not double data")
        except Exception as e:
            print(e)
            sys.exit(1)

        try: 
            result = self._collection.insert_many(data)
            print("Bulking data to collection")
        except Exception as e:
            print(e)
            sys.exit(1)
        else:
            inserted_count = len(result.inserted_ids)
            print("Inserted %d documents." %(inserted_count))

        results = self._collection.find()

        if results:    
            ids = []
            for x in results:
                ids.append(x["_id"])
            
            res = len(ids)
        else:
            res = "No documents found."

        return json.dumps(res)