import pymongo
from pymongo import MongoClient
client = MongoClient()

if __name__ == '__main__':
    print "inserting a document"
    db = client.csci2963
    collection = db.definitions
    definition = { "word":"crunk",
                "definition":"it's what you get when you party with lil jon"}
    def_id = collection.insert_one(definition).inserted_id
    print def_id
    raw_input()

    print "finding all"
    for page in collection.find():
        print page
    raw_input()

    print "finding one"
    print collection.find_one()
    raw_input()

    print "finding one by word"
    print collection.find_one({"word":"schwifty"})
    raw_input()

    print "finding one by id"
    print collection.find_one({"_id":def_id})
    raw_input()
