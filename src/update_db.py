import pymongo


MONGO_SERVER = "localhost"
MONGO_PORT = 27017
DB_NAME = "ai-db"
COLLECTION_NAME = "model-data"


if __name__ == "__main__":
    with pymongo.MongoClient(f"mongodb://{MONGO_SERVER}:{MONGO_PORT}/") as client:
        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        query = {"name": "mDMBD8gB.jpg"}
        additional_labels = {
            "category": "model",
            "uuid": "model_5Qawtszn",
            "labels": [5],
        }

        x = collection.update_one(
            query, {"$push": {"labels": additional_labels}}, upsert=True
        )

        for x in collection.find():
            print(x)
