# from flask import Flask, render_template, request, redirect
# import json

# app = Flask(__name__)


# my_post = [{"title":"This is the title 2","content":"this is the content 2","published":True,"id":2,"created_at":"2022-12-15T08:41:44.888493+05:30"},{"title":"This is the title 4","content":"this is the content 4","published":True,"id":4,"created_at":"2022-12-15T08:42:21.689495+05:30"},{"title":"This is the title 5","content":"this is the content 5","published":True,"id":5,"created_at":"2022-12-15T08:42:29.122437+05:30"},{"title":"This is the title 6","content":"this is the content 6","published":True,"id":6,"created_at":"2022-12-15T08:48:46.036579+05:30"},{"title":"This is the title 7","content":"this is the content 7","published":True,"id":7,"created_at":"2022-12-15T08:49:36.170970+05:30"},{"title":"This is the title 8","content":"this is the content 8","published":True,"id":8,"created_at":"2022-12-15T08:54:30.602010+05:30"},{"title":"hi again","content":"hello again","published":True,"id":3,"created_at":"2022-12-15T08:42:15.566597+05:30"},{"title":"This is the title 9","content":"this is the content 9","published":True,"id":9,"created_at":"2022-12-15T22:42:46.765041+05:30"},{"title":"This is the title 11","content":"this is the content 11","published":True,"id":11,"created_at":"2022-12-15T22:45:41.168004+05:30"},{"title":"This is the title 12","content":"this is the content 12","published":True,"id":12,"created_at":"2022-12-15T22:47:57.880590+05:30"},{"title":"This is the title 13","content":"this is the content 13","published":True,"id":13,"created_at":"2022-12-15T22:52:03.893427+05:30"},{"title":"This is the title 14","content":"this is the content 14","published":True,"id":14,"created_at":"2022-12-15T22:53:24.159921+05:30"},{"title":"Nineth post updated","content":"This is the content for Nineth post","published":True,"id":10,"created_at":"2022-12-15T22:45:05.874094+05:30"}]


# #session9
# '''@app.route("/<index>")
# def post(index):
#     return render_template("index.html",data= my_post[int(index)])'''


# #session10
# # @app.route("/create",methods = ["POST","GET"])
# # def create_post():
# #     if request.form!= None:
# #         title = request.form.get("title")
# #         content = request.form.get("content")
# #         author = request.form.get("author")
# #         dot = {"title": title,"content":content,"author":author}
# #         my_post.append(dot)
# #         return render_template("create_post.html", data = my_post)



# #session11

# # @app.route("/home")
# # def dict():
# #     return my_post


# # sending a data from postman #task 

# @app.route("/api", methods = ["POST"])
# def api_method():
#     # print(request.json)
#     # return request.json.get("content")

#     title = request.json.get("title")
#     content = request.json.get("content")
#     author = request.json.get("author")
#     temp_dic = {"title":title,"content":content,"author":author}
#     my_post.append(temp_dic)
#     print(request.json)
#     return my_post

# #session12   #task

# @app.route("/create", methods=["POST","GET"])
# def newfun():
#     my_post[2]=request.form
#     return render_template("create_post.html", data=my_post)


# @app.route("/delete", methods=["GET","POST"])
# def delete_post():
#     my_post.pop(2)
#     return render_template("create_post.html", data=my_post)


# #session13

# @app.route("/<api_id>", methods=["POST","GET"])
# def new_fun(api_id):
#     id =request.json.get("id")
#     title=request.json.get("title")
#     content = request.json.get("content")
#     my_post[int(api_id)]["title"]=title 
#     my_post[int(api_id)]["content"]=content 
#     print(my_post[int(api_id)])
#     return my_post



# if __name__ == "__main__":
#     app.run(debug=True)

# a,*b = 10,20,30
# print(type(a))

