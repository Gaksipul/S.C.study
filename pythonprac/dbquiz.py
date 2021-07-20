from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title':'매트릭스'})
target_point = movie['point']

same_point = list(db.movies.find({'point':target_point},{'_id':False}))

for same in same_point:
    print(same['title'])