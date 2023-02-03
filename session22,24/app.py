from flask import Flask, render_template,request,json
from pymongo import MongoClient

app = Flask(__name__) 

client = MongoClient("mongodb://127.0.0.1:27017")


@app.route("/api", methods= ["post","get"])
def api():
    client = MongoClient("mongodb://127.0.0.1:27017")
    name = request.json
    print(name)
    database = client.user
    collection = database.detail
    for i in name:
        collection.insert_one({
            "name": i["name"],
            "course": i["course"],
            "title": i["title"]
        })
    
    print("inserted")
    client.close()
    return name

@app.route("/apibulk",methods = ["post","get"])
def apibulk():
    client = MongoClient("mongodb://127.0.0.1:27017")
    l = request.json
    database= client.user
    collection = database.detail
    collection.insert_many(l)
    print("inserted")
    client.close()
    return "success"


@app.route("/display",methods = ["post","get"])
def readall():
    client = MongoClient("mongodb://127.0.0.1:27017")
    database= client.user
    collection = database.detail
    # result = collection.find_one({"name":"Dhaya"}) 
    result = collection.find({"name":"Monisha"}) # it return object collection i f v have to know the data, so that we are using list and loop  
    print(result)
    a= [] 
    for i in result:
        a.append(i)
    client.close()
    #return (str(a))
    return render_template("table.html",data = a)   


@app.route("/read/<name>",methods = ["post","get"])
def read(name):
    client = MongoClient("mongodb://127.0.0.1:27017")
    database= client.user
    collection = database.detail
    result = collection.find({"name":name}) #findone
    print(result)

    a= [] 
    for i in result:
        a.append(i)
    client.close()
    return render_template("table.html",data = a)

@app.route("/",methods = ["post","get"])
def form():
    client = MongoClient("mongodb://127.0.0.1:27017")
    if request.form.get("name")!= None:
        name = request.form.get("name")
        course = request.form.get("course")
        title = request.form.get("title")
        database = client.user
        collection = database.detail
        collection.insert_one({"name":name,"course":course,"title":title })
        print("inserted")
        client.close()
        return "success" 
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
