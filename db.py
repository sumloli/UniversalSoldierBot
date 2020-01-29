import pymongo
from config import *
import datetime


client = pymongo.MongoClient(
    'mongodb+srv://sumloli:{}@cluster0-deits.mongodb.net/test?retryWrites=true&w=majority'.format(DB_PASS))


def db():
    database = client.sample_supplies
    collection = database.sales
    print('MongoDB version is {}'.format(client.server_info()['version']))
    print(collection)
    return 'REQUESTED COLLECTION: \n{}'.format(collection) + '\nMongoDB version is {}'.format(client.server_info()['version']) + '🐍:{}'.format(os.environ['test_var'])


def db_sanya(input):
    database = client.sanya
    collection = database.stats

    emp_rec1 = {
        str(datetime.datetime.now()): f"{input}",
    }

    # Insert Data
    rec_id1 = collection.insert_one(emp_rec1)

    print("Data inserted with record id", rec_id1)

    # Printing the data inserted
    cursor = collection.find()
    for record in cursor:
        print(record)