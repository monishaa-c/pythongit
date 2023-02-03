from flask import Flask, render_template,request
import requests
import json


app = Flask(__name__)


# @app.route("/")
# def api():
    
#     url = "https://api.mfapi.in/mf/100350" 

#     resp = requests.get(url)

#     print(resp.json())4

#     # return render_template("index.html", data = resp.json())

#     # return render_template("index.html", data = resp.json().get("data"))

#     return render_template("index.html", data1 = resp.json().get("data")[0].get("nav"))




l = [148919,148918,148920,148921,139616,139618,139619]
post = []

@app.route("/", methods = ["POST", "GET"])

def api_():

    for i in range(len(l)):
        url = "https://api.mfapi.in/mf/" + str(l[i])
        resp = requests.get(url)
        print(url)
        fund = resp.json().get("meta").get("fund_house")
        navi = resp.json().get("data")[0].get("nav")
        dic = {"id":l[i],"fund_house":fund,"nav":navi}
        post.append(dic)
        print(post)
    return render_template("index.html", data = post)


if __name__ == "__main__":
    app.run(debug=True)





