from flask import Flask, render_template,request
import requests
from pymongo import *

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")

@app.route("/",methods = ["post","get"])
def fund():
    lis = [145488,146679,147197,147198]
    ar = []
    for i in lis:
        url = "https://api.mfapi.in/mf/"+str(i)
        resp = requests.get(url)
        fund = resp.json().get("meta").get("fund_house")
        navi = resp.json().get("data")[0].get("nav")
        temp1 = {"id":str(i),"fund_house":fund,"nav":navi}
        ar.append(temp1)

    client = MongoClient("mongodb://localhost:27017")
    database = client.user
    collection = database.fund
    collection.insert_many(ar)
    print("inserted!")
    client.close()
    return render_template("index.html", data = ar)

@app.route("/update")
def update():
    client = MongoClient("mongodb://localhost:27017")
    database = client.user
    collection = database.detail
    collection.update_many({"name":"Monisha"},{"$set":{"course":"Reactjs"}})
    client.close()
    return "success"

@app.route("/delete")
def delete():
    client = MongoClient("mongodb://localhost:27017")
    database = client.user
    collection = database.detail
    collection.delete_many({"name":"Monisha"})
    client.close()
    return "success"

if __name__ == "__main__":
    app.run(debug=True)
