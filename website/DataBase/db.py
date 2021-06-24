import mysql.connector
import pymongo

my_database = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709",
                                      database="karthikDB")
curser = my_database.cursor(buffered=True)
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
    sql = "SELECT * FROM karthikdb.sign_up_info WHERE email=%(email)s"
    result = curser.execute(sql, {"email": email})
    cnt = curser.rowcount
    if cnt > 0:
        return True
    else:
        return False


class DB():
    # def __init__(self, name, email, password):
    #     self.name = name
    #     self.email = email
    #     self.password = password

    def getAccount(self, email):
        if accountValid(email):
            sql = "SELECT * FROM karthikdb.sign_up_info WHERE email=%(email)s"
            curser.execute(sql, {"email": email})
            myresult = curser.fetchall()

            for x in myresult:
                print("Id: ", x[0])
                print("username: ", x[1])
                print("email: ", x[2])
                print("passwd: ", x[3])
        else:
            print("Account not valid!")

    def AddUser(self, name, email, password):
        sql = "Insert into sign_up_info(username, email, passwd) values(%(name)s, %(email)s, %(password)s)"
        curser.execute(
            sql, {"name": name, "email": email, "password": password})
        my_database.commit()
        print("User added!")

    def DeleteUser(self, email):
        if accountValid(email):
            sql = "DELETE FROM sign_up_info WHERE email=%(email)s"
            curser.execute(sql, {"email": email})
            my_database.commit()
            print("User deleted!")
        else:
            print("Account not valid!")

    def ChangePassword(self, email, password):
        db = client["DB"]
        mycol = db["users"]
        mycol.update_one({"email": email}, {"$set": {"password": password}})
    def GetPassword(self, email):
        db = client["DB"]
        mycol = db["question"]
        

    def GetQuestionId(self, question):
        db = client["DB"]
        mycol = db["question"]
        result = mycol.find_one({"Question": question}, {})
        return result
    def GetUserId(self, email):
        mydb = client["DB"]
        mycolu = mydb["users"]
        result = mycolu.find_one({"email": email}, {})
        return result
    def AddAnswer(self, answer, email, question):
        mydb = client["DB"]
        mycol = mydb["user_question_map"]
        userid = db.GetUserId(email)
        questionid = db.GetQuestionId(question)
        post = {"userId": userid, "Question_id": questionid, "Answer": answer}
        mycol.insert(post)
    def GetQuestion(self, id):
        sql = "SELECT Question FROM karthikdb.question where Question_id=%(Question_id)s"
        curser.execute(sql, {"Question_id": id})
        result = curser.fetchall()
        for x in result:
            r = x
        return str(r)
    def GetAnswer(self, userid, question_id):
        answer = ""
        sql = "SELECT * FROM karthikdb.user_question_map where Question_id=%(Question_id)s and userId=%(userid)s"
        curser.execute(sql, {"Question_id": question_id, "userid": userid})
        result = curser.fetchall()
        for x in result:
            answer = x[2]
        return answer
        
    

db = DB()
# # Driver Code....
# db.getAccount("test@test.com")
# db.AddUser("karthik", "karthik@kar", "1123")
# db.DeleteUser("karthik@kar")
# db.GetPassword("test@test.com")
# db.ChangePassword("test@test.com", "test")
# db.AddAnswer("dwedewd", "test@test.com", "dwefer")    
# db.GetQuestions(61)
# db.GetQuestionId("What is your Date of Birth?")
# db.GetAnswer1('2')
