import mysql.connector

my_database = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709",
                                      database="karthikDB")
curser = my_database.cursor()


class DB():
    def getAccount(self, email):
        sql = "SELECT * FROM karthikdb.sign_up_info WHERE email=%(email)s"
        curser.execute(sql, {"email": email})
        myresult = curser.fetchall()

        for x in myresult:
            print("Id: ", x[0])
            print("username: ", x[1])
            print("email: ", x[2])
            print("passwd: ", x[3])

    def getEmail(self, userId):
        sql = "SELECT email FROM karthikdb.sign_up_info WHERE userId=%(userId)s"
        curser.execute(sql, {"userId": userId})
        result = curser.fetchall()
        print(result[0])

    def AddUser(self, name, email, password):
        sql = "Insert into sign_up_info(username, email, passwd) values(%(name)s, %(email)s, %(password)s)"
        curser.execute(
            sql, {"name": name, "email": email, "password": password})
        my_database.commit()
        print("User added!")

    def DeleteUser(self, userId):
        sql = "DELETE FROM sign_up_info WHERE userId=%(userId)s"
        curser.execute(sql, {"userId": userId})
        my_database.commit()
        print("User deleted!")

    def ChangePassword(self, email, password):
        sql = "UPDATE karthikdb.sign_up_info SET passwd=%(passwd)s WHERE email=%(email)s"
        curser.execute(sql, {"email": email, "passwd": password})
        my_database.commit()
        print("User changed")


db = DB()
# Driver Code....
# db.getAccount("rishi.teja@gmail.com")
# db.getEmail("1")
# db.AddUser("name", "test", "1234")
# db.DeleteUser(14)
