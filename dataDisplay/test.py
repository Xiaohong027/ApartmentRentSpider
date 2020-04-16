import pymongo

host = 'localhost'
port = 27017
client = pymongo.MongoClient(host,port)
bishe = client['bishe']
ty = bishe['ty']

for i in ty.find():
    info = i['info'].replace('\\n','').replace('\\t','')
    ty.update({'_id': i['_id']}, {"$set": {'info': info}}, upsert=True)
    print(i['info'])