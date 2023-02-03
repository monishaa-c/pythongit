from flask import Flask, render_template,request,redirect,url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def home():
    conn = sql.connect("user.db")
    conn.row_factory = sql.Row
    cur =conn.cursor()
    cur.execute("select * from data")
    data = cur.fetchall()
    conn.commit()
    return render_template("home.html",data = data)


@app.route("/insert", methods = ["post","get"])

def insert():
    if request.form.get("id")!= None:
        id = request.form.get("id")
        user = request.form.get("username")
        conn =sql.connect("user.db")
        cur = conn.cursor()
        cur.execute("insert into data(id,username) values(?,?)",(int(id),user))
        conn.commit()
    return render_template("index.html")


@app.route("/update/<id>",methods = ["post","get"])
def update1(id):
    if request.form.get("id")!= None:
        user1 = request.form.get("username")
        conn = sql.connect("user.db")
        cur = conn.cursor()
        cur.execute("update data set username = ? where id =?", (user1,int(id)))
        conn.commit()
        return render_template("index.html")

    conn = sql.connect("user.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("select * from data where id = ?", (int(id),))
    a = cur.fetchone()
    print(a)
    return render_template("create.html", data = a )


@app.route("/delete/<id>", methods = ["get"])
def delete(id):
    conn = sql.connect("user.db")
    cur = conn.cursor()
    cur.execute("delete from data where id =?", (int(id),))
    conn.commit()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True,host='127.1.2.3',port=7000)