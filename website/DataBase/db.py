import mysql.connector

my_database = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709",
                                      database="karthikDB")
curser = my_database.cursor(buffered=True)

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
        if accountValid(email):
            sql = "UPDATE karthikdb.sign_up_info SET passwd=%(passwd)s WHERE email=%(email)s"
            curser.execute(sql, {"email": email, "passwd": password})
            my_database.commit()
            print("User changed")
        else:
            print("Account not valid!")

    def GetPassword(self, email):
        if accountValid(email):
            sql = "SELECT * FROM karthikdb.sign_up_info WHERE email=%(email)s"
            curser.execute(sql, {"email": email})
            myresult = curser.fetchall()
            for x in myresult:
                password = x[3]
            return password
        else:
            print("Account not valid!")

    def GetQuestionId(self, question):
        question_id = 0
        sql = "SELECT Question_id FROM karthikdb.question where Question=%(question)s"
        curser.execute(sql, {"question": question})
        result = curser.fetchall()
        for x in result:
            question_id = x[0]
        return question_id
    def GetUserId(self, email):
        userID = 0
        sql = "SELECT userId FROM karthikdb.sign_up_info where email=%(email)s"
        curser.execute(sql, {"email": email})
        result = curser.fetchall()
        for x in result:
            userID = x[0]
        return userID
    def AddAnswer(self, answer, email, question):
        sql1 = "Insert into karthikdb.user_question_map(userId, Question_id, Answer) values(%(userId)s, %(Question_id)s, %(Answer)s)"
        UserId = db.GetUserId(email)
        Question_id = db.GetQuestionId(question)
        curser.execute(sql1, {"userId": UserId, "Question_id": Question_id, "Answer": answer})
        my_database.commit()
    def GetQuestion(self, id):
        sql = "SELECT Question FROM karthikdb.question where Question_id=%(Question_id)s"
        curser.execute(sql, {"Question_id": id})
        result = curser.fetchall()
        for x in result:
            r = x
        return str(r)

db = DB()
# # Driver Code....
# db.getAccount("test@test.com")
# db.AddUser("karthik", "karthik@kar", "1123")
# db.DeleteUser("karthik@kar")
# db.GetPassword("test@test.com")
# db.ChangePassword("test@test.com", "test")
# db.AddAnswer("dwedewd", "test@test.com", "dwefer")    
# db.GetQuestions(61)
db.GetQuestionId("What is your Date of Birth?")
