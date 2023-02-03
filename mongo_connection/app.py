from pymongo import *

client = MongoClient("mongodb://127.0.0.1:27017")

# if client:
#     print("connected")
# client.close()

database = client.dbcon
collection = database.tcon
collection.insert_one({
  "name": "Monisha",
  "age": 22,
  "branch": "cse",
  "rollnumber": 22
})
print("inserted")
client.close()