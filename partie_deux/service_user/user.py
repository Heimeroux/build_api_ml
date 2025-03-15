import uvicorn

from fastapi import FastAPI
from pymongo import MongoClient
"""
API pour requêter pour l'user
"""

app = FastAPI()

mongo_uri = 'mongodb://mongo_cc:27017/'
client = MongoClient(mongo_uri)
database = client["cc"]
collection = database["cc_items"]

@app.get("/get/{idx}")
async def get_data(idx: int):
    """
    Obtention d'une donnée à partir de son id
    """
    # Récupération de la collection mongoDB
    try:
        print(idx)
        data = list(
            collection.find(
                {"id": idx},
                {
                    "_id": 0,
                    "id": 1,
                    "value": 1,
                },
            )
        )
        return  {"res": data}
    except:
        return "Échec de la récupération"