from flask import Flask,render_template,request,url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route("/",methods = ["post","get"])
def insert():
    if request.form.get("id")!= None:
        id = request.form.get("id")
        name = request.form.get("name")
        dept = request.form.get("dept")
        branch = request.form.get("branch")
        phone = request.form.get("phone")

        conn = sql.connect("user.db")
        cur = conn.cursor()
        cur.execute("insert into data (id,name,dept,branch,phone) values(?,?,?,?,?)",(id,name,dept,branch,phone))
        conn.commit()
    return render_template("index.html")



















if __name__ == "__main__":
    app.run(debug=True)