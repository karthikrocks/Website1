import math
from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from DataBase.db import db, accountValid
from keys.key import encryptor
import random
import string
import hashlib
import uuid
import json
from flask_pymongo import PyMongo
app = Flask(__name__)
app.secret_key = "secret"
app.permanent_session_lifetime = timedelta(hours=24)
app.config["MONGO_URI"] = "mongodb+srv://Karthik:rishi@cluster0.uj94w.mongodb.net/DB?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
mongo = PyMongo(app)
# emailValid function


def emailValid():
    email = request.form['em']
    cnt = mongo.db.users.find({'email': email}).count()
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
    session["name"] = username
    session["email"] = email
    session["password"] = password

    if request.method == 'POST':

        if not emailValid():
            flash("This User already exists. Please login or sign up as a new user.")
            session.pop("name")
            return redirect(url_for("main_register"))
        if int(len(username)) != 0:
            if int(len(email)) != 0:
                if int(len(password)) != 0:
                    resultpass = hashlib.sha256(password.encode())
                    id = uuid.uuid1()
                    post = {"_id": str(
                        id), "username": username, "email": email, "password": resultpass.hexdigest()}
                    mongo.db.users.insert(post)
                    return redirect(url_for("setup"))
    flash("Cannot Register with no details!")
    return redirect(url_for("main_register"))

# LOGIN


@app.route('/login', methods=['POST'])
def login():
    if "name" in session:
        name = session["name"]
        return redirect(url_for("home"))
    session.permanent = True
    name = request.form["username"]
    pwd = request.form["passwd"]
    resultpassw = hashlib.sha256(pwd.encode())
    cnt = mongo.db.users.find(
        {"username": name, "password": resultpassw.hexdigest()}).count()
    if cnt > 0:
        post = str(mongo.db.users.find_one({"username": name}, {
                   "password": False, "username": False, "_id": False}))
        r = eval(post)
        session["email"] = r["email"]
    if cnt > 0:
        t = db.getAccount("rishist@gmail.com")
        print(t)
        session["logged_in"] = True
        session["name"] = name
        session["password"] = pwd
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
        old_passwd = request.form["o_pass"]
        result_old_pass = hashlib.sha256(old_passwd.encode())
        passwr = session["password"]
        password = hashlib.sha256(passwr.encode())

        change_pass = hashlib.sha256(passwd.encode())
        if len(passwd) != 0 and len(c_passwd) != 0 and len(old_passwd) != 0:
            if passwd == c_passwd:
                if result_old_pass.hexdigest() == password.hexdigest():
                    db.ChangePassword(
                        session["email"], change_pass.hexdigest())
                    session["password"] = passwd
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

        if len(a_1) != 0 and len(a_2) != 0 and len(a_3) != 0 and len(a_4) != 0:
            db.AddAnswer(a_1, session["email"], "What is your Date of Birth?")
            db.AddAnswer(a_2, session["email"], "What is your fathers name?")
            db.AddAnswer(a_3, session["email"], "What's your mothers name?")
            db.AddAnswer(a_4, session["email"], "What's your School name?")
            flash("Successfully Created your account!")
            return redirect(url_for("home"))

    return render_template('q-a.html', q_1="What is your Date of Birth?", q_2="What is your fathers name?", q_3="What's your mothers name?", q_4="What's your School name?")


@app.route('/enter_email', methods=['POST', 'GET'])
def enter_email():
    if request.method == 'POST':
        email = request.form['email']
        if accountValid(email):
            if len(email) != 0:
                session["user_email"] = email
                return redirect(url_for("forgot_password"))
            else:
                return redirect(url_for("enter_email"))
        else:
            flash(
                "Account not found! Please enter the correct email address or sign up as a new user!")
            return redirect(url_for("main_register"))
    return render_template('email_enter.html')


@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if "user_email" in session:
        if request.method == "POST":
            email = session["user_email"]
            a_1 = request.form["a_1"]
            a_2 = request.form["a_2"]
            a_3 = request.form["a_3"]
            userId = db.GetUserId(email)
            if len(a_1) != 0 and len(a_2) != 0 and len(a_3) != 0:
                if a_1 == db.GetAnswer(userId, '24684bfb-d558-11eb-93a0-c8b29b733f0b'):
                    if a_2 == db.GetAnswer(userId, '153abe27-d568-11eb-b2bd-c8b29b733f0b'):
                        if a_3 == db.GetAnswer(userId, '354e4020-d568-11eb-830d-c8b29b733f0b'):
                            session["questions_correct"] = True
                            # TODO - redirect to reset password page when all answers are correct
                            return redirect(url_for("main_register"))
                        else:
                            flash("Invalid Answers!")
                            return redirect(url_for("main_register"))
                    else:
                        flash("Invalid Answers!")
                        return redirect(url_for("main_register"))
                else:
                    flash("Invalid Answers!")
                    return redirect(url_for("main_register"))

    else:
        return redirect(url_for("enter_email"))

    return render_template("forgot_pass.html", q_1="What is your Date of Birth?", q_2="What is your fathers name?", q_3="What's your mothers name?", q_4="What's your School name?")


@app.route("/reset")
def pass_reset():
    return render_template("pass_reset.html")


if __name__ == "__main__":
    app.run(debug=True, port=1000, host='0.0.0.0')
