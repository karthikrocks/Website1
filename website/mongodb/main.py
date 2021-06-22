import pymongo

client = pymongo.MongoClient('mongodb+srv://Karthik:rishi@cluster0.uj94w.mongodb.net/DB?retryWrites=true&w=majority')
db = client["DB"]
mycol = db["users"]
print(db.list_collection_names())

mycol.insert_one({"_id": 2, "username": "test", "email": "test@test.com", "password": "test1234"})




