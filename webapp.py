import flask
import sqlite3
website=flask.Flask("__name__")

@website.route("/")
def first_page():
    return flask.render_template("homepage.html")

@website.route("/user")
def user():
    return flask.render_template("login.html")

@website.route("/login" , methods=['post'])
def second_page():
    entered_username = flask.request.form.get("username")
    entered_password = flask.request.form.get("password")
    con = sqlite3.connect("mysdp2.sqlite3")
    cur = con.cursor()
    cur.execute(f"select * from userstable where accounnumber='{entered_username}' and password='{entered_password}'")

    result = cur.fetchone()
    if result is None:
        data="Enter the valid accountnumber and password"
        return flask.render_template("login.html",data=data)
    else:

        return flask.render_template("page1.html")


@website.route("/createnew")
def createnewpage():
    return flask.render_template("registartion.html")

@website.route("/newpage" ,  methods=['post','get'])
def first():
    re_username = flask.request.form.get("username")
    re_lastname = flask.request.form.get("lastname")
    re_password = flask.request.form.get("password1")
    re_password2 = flask.request.form.get("password2")
    re_email = flask.request.form.get("email")
    re_phnumber = flask.request.form.get("phnumber")
    re_account = flask.request.form.get("accnumber")

    con = sqlite3.connect("mysdp2.sqlite3")
    cur = con.cursor()
    my_table_query = "create table if not exists userstable(name varchar(20),lastname varchar(20),password varchar(15),email varchar(30),mobileno varchar(10),accounnumber varchar(12))"
    cur.execute(my_table_query)
    cur.execute(f"select email from userstable where email='{re_email}'")
    result = cur.fetchone()
    if result != None:
        return "Email Already Exists....Try again"
    else:
        my_insert_query = f"insert into userstable values('{re_username}','{re_lastname}','{re_password}','{re_email}','{re_phnumber}','{re_account}')"
        cur.execute(my_insert_query)
        con.commit()
        return flask.render_template("login.html")
@website.route("/login/bank")
def bank():
    return flask.render_template("bank.html")

if __name__=="__main__":
    website.run(port=3000)
