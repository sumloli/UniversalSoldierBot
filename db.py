import pymongo
from config import *

client = pymongo.MongoClient(
    'mongodb+srv://sumloli:{}@cluster0-deits.mongodb.net/test?retryWrites=true&w=majority'.format(DB_PASS))



def db():
    database = client.sample_supplies
    collection = database.sales
    print('MongoDB version is {}'.format(client.server_info()['version']))
    print(collection)
    return 'REQUESTED COLLECTION: \n{}'.format(collection) + '\nMongoDB version is {}'.format(client.server_info()['version'])


