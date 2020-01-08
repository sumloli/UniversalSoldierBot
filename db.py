import pymongo
from config import *

my_client = pymongo.MongoClient(
    'mongodb+srv://sumloli:{}@cluster0-deits.mongodb.net/test?retryWrites=true&w=majority'.format(DB_PASS))
try:
    print("MongoDB version is {}s".format(my_client.server_info()['version']))
except my_client.errors.OperationFailure as error:
    print(error)
    quit(1)
