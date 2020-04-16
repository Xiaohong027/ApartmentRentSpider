import pymongo

host = 'localhost'
port = 27017

client = pymongo.MongoClient(host,port)
proxies = client['proxies']
version1 = proxies['version1']

print(version1.find().count())
