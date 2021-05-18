import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709", database="KarthikDB")

my_curser = my_db.cursor()

my_curser.execute("Create  table hack(userId integer, username varchar(200), email varchar(200), "
                  "passwd varchar(200))")
