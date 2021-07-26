import pymongo

client = pymongo.MongoClient("mongodb+srv://Karthik:rishi@cluster0.uj94w.mongodb.net/DB?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true")


"""

[] = database -> connection - host-"localhost", user-"root", password-***** (
    getaccount -[email] = gets account from the database
    AddUser -[name, email, passwd] - adds a user to the database
    DeleteUser -[email] - deletes a user
    ChangePassword -[email] - changes password
    GetPassword -[email] - gets password from the database
    AccountValid -[email] - checks if the user exists in the database
)

"""


def accountValid(email):
    db = client["DB"]
    mycol = db["users"]
    cnt = mycol.find({"email": email}).count()
    if cnt > 0:
        return True

def accountValidWithUID(uid):
    db = client["DB"]
    mycol = db["users"]
    cnt = mycol.find({"_id": uid}).count()
    if cnt > 0:
        return True



class DB():
    def ChangePassword(self, email, password):
        db = client["DB"]
        mycol = db["users"]
        mycol.update_one({"email": email}, {"$set": {"password": password}})

    def GetQuestionId(self, question):
        db = client["DB"]
        mycol = db["question"]
        result = str(mycol.find_one({"Question": question}, {}))
        r = eval(result)
        return r["_id"]
    def GetUserId(self, email):
        mydb = client["DB"]
        mycolu = mydb["users"]
        result = str(mycolu.find_one({"email": email}, {}))
        r = eval(result)
        return r["_id"]
    def AddAnswer(self, answer, email, question):
        mydb = client["DB"]
        mycol = mydb["user_question_map"]
        userid = db.GetUserId(email)
        questionid = db.GetQuestionId(question)
        post = {"userId": userid, "Question_id": questionid, "Answer": answer}
        mycol.insert(post)
    def GetAnswer(self, userid, question_id):
        mydb = client["DB"]
        mycol = mydb["user_question_map"]
        answer = str(mycol.find_one({"userId": userid, "Question_id": question_id}, {"userId": False, "Question_id": False, "_id": False}))
        r = eval(answer)
        return r["Answer"]
    def GetQuestion(answer):
        mydb = client["DB"]
        mycol = mydb["user_question_map"]
        question = str(mycol.find_one({"answer": answer}))



db = DB()
