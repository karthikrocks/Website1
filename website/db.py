import mysql.connector

my_database = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709",
                                      database="karthikDB")
curser = my_database.cursor()


class DB():
    def getAccount(self, email):
        sql = "SELECT * FROM karthikdb.sign_up_info WHERE email='" + email + "'"
        curser.execute(sql)
        myresult = curser.fetchall()

        for x in myresult:
            print("Id: ", x[0])
            print("username: ", x[1])
            print("email: ", x[2])
            print("passwd: ", x[3])


db = DB()
# Driver Code....
# db.getAccount("rishi.teja@gmail.com")
