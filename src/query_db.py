import pymongo


MONGO_SERVER = "localhost"
MONGO_PORT = 27017
DB_NAME = "ai-db"
COLLECTION_NAME = "model-data"


if __name__ == "__main__":
    with pymongo.MongoClient(f"mongodb://{MONGO_SERVER}:{MONGO_PORT}/") as client:

        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        print("$AND QUERY (tags.color = violet, tags.size = big):")
        for x in collection.find(
            {"$and": [{"tags.color": "violet"}, {"tags.size": "big"}]}, {"_id": 0}
        ):
            print(x)
        print()

        print("QUERY FIND IN SUBARRAY (everyone who has a label 1):")
        for x in collection.find({"labels.labels": 1}):
            print(x)
        print()

        print("QUERY ALL:")
        for x in collection.find():
            print(x)
        print()
