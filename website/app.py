import math
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from DataBase.db import db
from keys.key import encryptor
import mysql.connector
import hashlib
app = Flask(__name__)
key = encryptor.key_load(str('keys/key.key'))
app.secret_key = key
app.permanent_session_lifetime = timedelta(hours=24)


def emailValid():
    my_database = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709",
                                          database="karthikDB")
    email = request.form['em']
    curser = my_database.cursor(buffered=True)
    sql_code = "SELECT * FROM karthikdb.sign_up_info where email=%(email)s"

    result = curser.execute(sql_code, {'email': email})
    cnt = curser.rowcount
    curser.close()
    my_database.close()
    return cnt == 0


@app.route('/login-register', methods=['GET'])
def index():
    if "name" in session:
        name = session["name"]
        flash("You are already logged in!")
        return redirect(url_for("home"))
    return render_template('index.html')


@app.route('/login-register', methods=['POST'])
def main_register():

    username = request.form['u']
    email = request.form['em']
    password = request.form['pa']
    my_database = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709",
                                          database="karthikDB")
    session["name"] = username
    session["email"] = email
    session["password"] = password

    curser = my_database.cursor()

    if request.method == 'POST':

        if not emailValid():
            flash("This User already exists. Please login or sign up as a new user.")
            session.pop("name")
            return redirect(url_for("main_register"))
        if int(len(username)) != 0:
            if int(len(email)) != 0:
                if int(len(password)) != 0:
                    resultpass = hashlib.sha256(password.encode())
                    db.AddUser(username, email, resultpass.hexdigest())
                    my_database.close()
                    return redirect(url_for("setup"))
    flash("Cannot Register with no details!")
    return redirect(url_for("main_register"))

# LOGIN
@app.route('/login', methods=['POST'])
def login():
    if "name" in session:
        name = session["name"]
        return redirect(url_for("home"))
    my_database = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709",
                                          database="karthikDB")
    session.permanent = True
    name = request.form["username"]
    pwd = request.form["passwd"]
    curser = my_database.cursor(buffered=True)
    sql_code = "SELECT * FROM karthikdb.sign_up_info where username=%(user_name)s and passwd=%(password)s"
    resultpassw = hashlib.sha256(pwd.encode())
    result = curser.execute(sql_code, {'user_name': name, 'password': resultpassw.hexdigest()})
    cnt = curser.rowcount
    email = ""
    if cnt > 0:
        res = curser.fetchone()
        email = res[2]

    curser.close()
    my_database.close()

    if cnt > 0:
        session["logged_in"] = True
        session["email"] = email
        session["name"] = name
        session["pwd"] = pwd
        if "name" in session:
            name = session["name"]
            flash("Login Successful!")
            return redirect(url_for("home"))
        else:
            return render_template("my_home.html")

    else:
        flash("Invalid username or password!")
        return redirect(url_for("main_register"))


@app.route('/home')
def home():
    if "name" in session:
        name = session['name']
        return render_template('home.html', name=name)
    else:
        return render_template("my_home.html")


@app.route('/logout')
def logout():
    session.pop("name", None)
    session.pop("pwd", None)
    session.clear()
    flash(" You have been logged out")
    return redirect(url_for('main_register'))


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/details', methods=['POST', 'GET'])
def account():
    if request.method == 'POST':
        passwd = request.form["pass"]
        c_passwd = request.form["c_pass"]
        session["passw"] = passwd
        old_passwd = request.form["o_pass"]
        password = db.GetPassword(session["email"])
        if len(passwd) != 0 and len(c_passwd) != 0 and len(old_passwd) != 0:
            if passwd == c_passwd:
                if old_passwd == password:
                    db.ChangePassword(session["email"], session["passw"])
                    session["pwd"] = session["passw"]
                    flash("Password Saved")
                    return redirect(url_for("home"))
        if old_passwd != password:
            flash("Old Password Incorrect")
            return redirect(url_for("home"))

    if "name" in session:
        return render_template("account.html", username=session["name"], email=session["email"])
    else:
        flash("Please Login to view the Account details")
        return redirect(url_for("main_register"))


@app.errorhandler(404)
def page_not_found(e):
    """ note that we set the 404 status explicitly """
    return render_template('404.html'), 404


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if "name" not in session:
        flash("Please Signup to setup your account!")
        return redirect(url_for("main_register"))
    if request.method == 'POST':
        a_1 = request.form["a_1"]
        a_2 = request.form["a_2"]
        a_3 = request.form["a_3"]
        a_4 = request.form["a_4"]
        
        
        my_database = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709",
                                          database="karthikDB")
        curser = my_database.cursor()
        
        
        if len(a_1) != 0 and len(a_2) != 0 and len(a_3) != 0 and len(a_4) != 0:
            db.AddAnswer(a_1, session["email"], "What is your Date of Birth?") 
            db.AddAnswer(a_2, session["email"], "What is your fathers name?")
            db.AddAnswer(a_3, session["email"], "What's your mothers name?")
            db.AddAnswer(a_4, session["email"], "What's your School name?")
            flash("Successfully Created your account!")
            return redirect(url_for("home"))

    return render_template('q-a.html', q_1="What is your Date of Birth?", q_2="What is your fathers name?", q_3="What's your mothers name?", q_4="What's your School name?")
@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        my_database = mysql.connector.connect(host="localhost", user="root", passwd="karthi@0709",
                                          database="karthikDB")
        curser = my_database.cursor()
        a_1 = request.form["a_1"]
        a_2 = request.form["a_2"]
        a_3 = request.form["a_3"]
        UserID = db.GetUserId(session["email"])
        sql1 = "SELECT Answer FROM user_question_map WHERE userId=%(userid)s and Question_id=%(questionid)s"
        
    return render_template("forgot_pass.html", q_1="What is your Date of Birth?", q_2="What is your fathers name?", q_3="What's your mothers name?", q_4="What's your School name?")
        

if __name__ == "__main__":
    app.run(debug=True, port=1000, host='0.0.0.0')
