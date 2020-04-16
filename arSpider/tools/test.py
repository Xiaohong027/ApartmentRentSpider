import pymongo
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
client = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
bishe = client['bishe']
ty = bishe['ty']
a = []
for i in ty.find({'source':'107room'}):
    a.append(i)
    print(len(a))