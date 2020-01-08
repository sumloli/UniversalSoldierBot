import pymongo
from config import *

client = pymongo.MongoClient(
    'mongodb+srv://sumloli:{}@cluster0-deits.mongodb.net/test?retryWrites=true&w=majority'.format(DB_PASS))

database = client.sample_supplies
collection = database.sales

def db():
    print('MongoDB version is {}'.format(client.server_info()['version']))
    print(collection)
    return 'MongoDB version is {}'.format(client.server_info()['version'])


