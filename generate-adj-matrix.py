import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['organizations']
posts = db.posts

for post in posts.find():
    print post['name']
    print post['type']
    print post['about']
