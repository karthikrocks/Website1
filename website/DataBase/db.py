import mysql.connector

my_database = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709",
                                      database="karthikDB")
curser = my_database.cursor()

"""
[] = database -> connection - host-*****8=*72, user-**Jwuw8#6, password-***** (
    getaccount -[email] = gets account 
    AddUser -[name, email, passwd] - adds a user
    DeleteUser -[email] - deletes a user
    ChangePassword -[email] - changes password
    GetPassword -[email] - gets password from the database
)

"""

class DB():
    # def __init__(self, name, email, password):
    #     self.name = name
    #     self.email = email
    #     self.password = password

    def getAccount(self, email):
        sql = "SELECT * FROM karthikdb.sign_up_info WHERE email=%(email)s"
        curser.execute(sql, {"email": email})
        myresult = curser.fetchall()

        for x in myresult:
            print("Id: ", x[0])
            print("username: ", x[1])
            print("email: ", x[2])
            print("passwd: ", x[3])

    def AddUser(self, name, email, password):
        sql = "Insert into sign_up_info(username, email, passwd) values(%(name)s, %(email)s, %(password)s)"
        curser.execute(
            sql, {"name": name, "email": email, "password": password})
        my_database.commit()
        print("User added!")

    def DeleteUser(self, email):
        sql = "DELETE FROM sign_up_info WHERE email=%(email)s"
        curser.execute(sql, {"email": email})
        my_database.commit()
        print("User deleted!")

    def ChangePassword(self, email, password):
        sql = "UPDATE karthikdb.sign_up_info SET passwd=%(passwd)s WHERE email=%(email)s"
        curser.execute(sql, {"email": email, "passwd": password})
        my_database.commit()
        print("User changed")
    def GetPassword(self, email):
        sql = "SELECT * FROM karthikdb.sign_up_info WHERE email=%(email)s"
        curser.execute(sql, {"email": email})
        myresult = curser.fetchall()
        for x in myresult:
            password = x[3]
        return password



db = DB()
# Driver Code....
# db.getAccount()
# db.AddUser("karthik", "karthik@kar", "1123")
db.DeleteUser("karthik@kar")
