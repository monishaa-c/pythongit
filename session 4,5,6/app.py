#session-4

'''from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():

    return "Welcome!"


if __name__ == "__main__":

    app.run()     
'''

#session-5


#two list descending order

l1 = ["sun","mon","tues","wed","thur","fri","sat","sun"]

l2 = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec",]

add = l1 + l2

add.sort()

print("sorted list:", add)

print("\n")

add.reverse()

print("Reverse a list:", add)



#session-6

'''from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def hello():

    return render_template("index.html")


if __name__ == "__main__":

    app.run(debug=True)

'''

#context passing


# from flask import Flask,render_template

# app = Flask(__name__)

# my_post = {"id": "23102023"}

# @app.route("/")

# def hello():

#     return render_template("index.html", data = my_post)


# if __name__ == "__main__":

#     app.run(debug=True)



#passing data in url



from flask import Flask,render_template

app = Flask(__name__)

@app.route("/<username>")

def hello(username):

    return render_template("index.html", data = username)


if __name__ == "__main__":

    app.run(debug=True)





