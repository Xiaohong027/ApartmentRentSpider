from django.db import models
from mongoengine import *
# Create your models here.

connect('bishe', host='127.0.0.1', port=27017)
class HouseInfos(Document):
    url = StringField()
    title = StringField()
    info = StringField()
    price = StringField()
    source = StringField()
    content = StringField()
    direction = StringField()
    phone = StringField()
    flag = StringField()
    region = StringField()
    lon = StringField()
    lat = StringField()

    meta = {'collection': 'ty'}