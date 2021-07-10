import pymongo
import uuid
import pytest
import json
client = pymongo.MongoClient("mongodb+srv://Karthik:rishi@cluster0.uj94w.mongodb.net/DB?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true")
test = client.test
db = client["DB"]
mycol = db["user_question_map"]
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
email = '{ "email": "rishist@gmail.com"}'
# result = mycol.find_one({"username": "Rishith Teja"}, {"password": False, "username": False, "_id": False})
# result = mycol.find_one({"Question": "What is your Date of Birth?"}, {})
# result = mycol.find_one({"Question": 'What is your Date of Birth?'}, {})
# result = mycol.find({"email": "rishist@gmail.com", "username": "Rishith Teja"}).count()
# mycol.delete_many({})
# k = eval(email)
# print(result)
y = json.loads(email)
print(y["email"])
# s = "{'username':'dfdsfdsf'}"
# j = eval(s)
# print(j["username"])
# print(email.email)
# id = uuid.uuid1()
# print (id)
# answer = str(mycol.find_one({"userId": 'a23527b7-d5a8-11eb-92e5-c8b29b733f0b', "Question_id": '24684bfb-d558-11eb-93a0-c8b29b733f0b'}, {"userId": False, "Question_id": False}))
# print(answer)


