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


db = DB()
# # Driver Code....
# db.getAccount("test@test.com")
# db.AddUser("karthik", "karthik@kar", "1123")
# db.DeleteUser("karthik@kar")
# db.GetPassword("test@test.com")
# db.ChangePassword("test@test.com", "test")
