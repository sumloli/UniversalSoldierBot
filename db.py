import pymongo
from config import *
import random

client = pymongo.MongoClient(
    'mongodb+srv://sumloli:{}@cluster0-deits.mongodb.net/test?retryWrites=true&w=majority'.format(DB_PASS))


def db():
    database = client.sample_supplies
    collection = database.sales
    print('MongoDB version is {}'.format(client.server_info()['version']))
    print(collection)
    return f'MongoDB version is {client.server_info()["version"]}\n' + f'🐍🐍🐍🐍🐍{os.environ["test_var"]}🐍🐍🐍🐍🐍'


def db_sanya():
    today = random.choice(["красавчик", "пидор"])

    database = client.sanya
    collection = database.stats

    emp_rec1 = {'status': today}
    rec_id1 = collection.insert_one(emp_rec1)
    print("Data inserted with record id", rec_id1)

    # cursor = collection.find()
    # for record in cursor:
    #     print(record)
    # array = list(collection.find({}, {'_id': False}))
    # print(array)
    return today

def db_sanya_get_stat():
    database = client.sanya
    collection = database.stats
    data = list(collection.find({}, {'_id': False}))
    print(data)
    stat_pidr = sum(x.get('status') == 'пидор' for x in data)
    sanya_stat = int(stat_pidr / len(data) * 100)
    return f'По статистике Саня на {sanya_stat}% пидор и на {100-sanya_stat}% красавчик'