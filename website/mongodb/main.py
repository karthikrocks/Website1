import pymongo


client = pymongo.MongoClient("mongodb+srv://Karthik:rishi@cluster0.uj94w.mongodb.net/DB?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true")
test = client.test
db = client["DB"]
mycol = db["users"]
# print(db.list_collection_names())

post = {
    "_id": 1,
    "username": "Rishith",
    "email": {
      "personal_email": "rishist@gmail.com",
      "company_email": "rishist@outlook.com"   
    },
    "password": "e264b8cb2ac2d087d67fb3c6e957bb9d0b47c486e81cc71c5f91c16407356b3e"
}

# result = mycol.find_one({"username": "Karthikeya Maanas"})
# result = mycol.find_one({"Question": "What is your Date of Birth?"}, {})
# result = mycol.find_one({"Question": 'What is your Date of Birth?'}, {})
result = mycol.find_one({}, {"_id": 0})
# mycol.delete_many({})
print(result)
