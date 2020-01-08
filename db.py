import pymongo
from config import *

my_client = pymongo.MongoClient(
    'mongodb+srv://sumloli:{}@cluster0-deits.mongodb.net/test?retryWrites=true&w=majority'.format(DB_PASS))


def db():
    print('MongoDB version is {}'.format(my_client.server_info()['version']))
    return 'MongoDB version is {}s'.format(my_client.server_info()['version'])
