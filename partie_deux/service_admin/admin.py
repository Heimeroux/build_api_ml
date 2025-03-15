import uvicorn
from fastapi import FastAPI
from pymongo import MongoClient
"""
Api pour l'admin
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


@app.get("/insert/{idx}/{value}")
async def insert_data(idx: int, value: str):
    """
    Insérer une donnée en fonction 
    """
    try:
        collection.insert_one(
            {
                "id": idx,
                "value": value
            },
        )
        return "Insertion réussie"
    except:   
        return "Échec de l'insertion"
        
@app.get("/update/{idx}/{value}")
async def update_data(idx: int, value: str):
    """
    Mettre à jour une donnée en fonction de son id et d'une nouvelle valeur
    """
    try:
        collection.update_one(
            {"id": idx},
            {
                "$set": {
                    "value": value,
                }
            },
            upsert=True
        )
        return "Update réussie"
    except:
        return "Échec de l'update"

#if __name__ == "__main__":
    #print(list(collection.find()))
print("Api pour le rôle admin mise à disposition sur le port 8000")
    #uvicorn.run(app, host="0.0.0.0", port=8000)
    