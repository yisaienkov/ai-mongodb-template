from typing import List, Dict, Any

import pymongo


MONGO_SERVER = "localhost"
MONGO_PORT = 27017
DB_NAME = "ai-db"
COLLECTION_NAME = "model-data"


def insert_data(data: List[Dict[str, Any]]) -> List:
    with pymongo.MongoClient(f"mongodb://{MONGO_SERVER}:{MONGO_PORT}/") as client:

        db = client[DB_NAME]
        collection = db[COLLECTION_NAME]

        x = collection.insert_many(data)

        return x.inserted_ids


if __name__ == "__main__":
    test_data = [
        {
            "name": "BEyyyhmn.jpg",
            "width": 1024,
            "height": 512,
            "tags": {
                "color": "green",
                "size": "small",
            },
            "labels": [
                {
                    "category": "labeler",
                    "uuid": "labeler_WWE997ZB",
                    "labels": [1, 4],
                },
                {
                    "category": "model",
                    "uuid": "model_UWg9tMGy",
                    "labels": [0, 1, 4],
                },
            ],
        },
        {
            "name": "JKsoXiGM.jpg",
            "width": 2048,
            "height": 512,
            "tags": {
                "color": "violet",
                "size": "small",
            },
            "labels": [
                {
                    "category": "labeler",
                    "uuid": "labeler_WWE997ZB",
                    "labels": [1],
                },
                {
                    "category": "labeler",
                    "uuid": "labeler_Drjw2krT",
                    "labels": [1, 2],
                },
                {
                    "category": "model",
                    "uuid": "model_UWg9tMGy",
                    "labels": [1],
                },
            ],
        },
        {
            "name": "mDMBD8gB.jpg",
            "width": 1024,
            "height": 512,
            "tags": {
                "color": "violet",
                "size": "big",
            },
            "labels": [
                {
                    "category": "labeler",
                    "uuid": "labeler_WWE997ZB",
                    "labels": [2, 4],
                },
                {
                    "category": "model",
                    "uuid": "model_UWg9tMGy",
                    "labels": [2, 4],
                },
                {
                    "category": "model",
                    "uuid": "model_4NYLS4cL",
                    "labels": [2, 4],
                },
            ],
        },
    ]

    print(insert_data(test_data))
