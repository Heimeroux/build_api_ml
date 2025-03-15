from pymongo import MongoClient
from fastapi import FastAPI
#from pymongo import MongoClient

app = FastAPI()

mongo_uri = 'mongodb://mongo_db_cc:27017/'
client = MongoClient(mongo_uri)
database = client["cc"]
collection = database["cc_items"]

@app.get("/data")
async def get_data():

    message = list(
        collection.find(
            {},
            {
                "_id": 0,
                "value": 1,
            }
        )
    )[0]
    
    return {"message": message}
    #return {"message": "message du service b"}
