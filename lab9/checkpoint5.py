from pymongo import MongoClient
import random
from time import gmtime, strftime
client = MongoClient()


def random_word_requester():
    db = client.csci2963
    collection = db.definitions
    i = random.randint(0, collection.count())
    count = 0
    for page in collection.find():
        if count == i:
            dates = []
            if 'time' in page:
                dates = page['time'].push(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            else:
                dates = [strftime("%Y-%m-%d %H:%M:%S", gmtime())]
            page.update({"time":dates})
            print page
            return
        count += 1


if __name__ == '__main__':
    random_word_requester()
