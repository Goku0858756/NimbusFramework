__author__ = 'N05F3R4TU'
import sys
from bson.dbref import DBRef
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class ModelTarget(object):

    def __init__(self, name):
        self.target_id = id(self)
        self.target_name = name
        self.target_ref = ""

    def target_connect(self):
        """Connect to the Database for Targets"""
        pass

    def target_put(self):
        """Put new Target into the Database"""
        pass



target_id = ObjectId("564f0990260caa1abd812262")

def main():
    """ Connect to MongoDB """
    try:
        c = MongoClient(host="localhost", port=27017)
        print("Connected successfully")
        print(c.server_info())
    except ConnectionFailure as e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    else:
        db = c["nmap"]
        print(db.collection_names())

        article = db.scan10.find_one({ '_id': { '$in': [ target_id ] } })
        print("##### {}".format(article))

        ob = DBRef("scan10", id=target_id, database=str(db))
        print(ob)
        print(ob.as_doc())

    finally:
        c.close()


if __name__ == "__main__":
    main()