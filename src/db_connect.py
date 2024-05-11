import os
import pymongo as pm
# import src.constants as const


LOCAL = "0"
CLOUD = "1"
client = None


def connect_db():
    global client
    if client is None:
        print("Setting client because it is None.")
        if os.environ.get("CLOUD_MONGO", LOCAL) == CLOUD:
            password = os.environ.get("DB_PASSWORD")
            if not password:
                raise ValueError('You must set your password '
                                 + 'to use Mongo in the cloud.')
            print("Connecting to Mongo in the cloud.")
            client = pm.MongoClient(f'mongodb+srv://tnv2002:{password}'
                                    + '@cluster0.dltyban.mongodb.net/'
                                    + '?retryWrites=true&w=majority'
                                    + '&connectTimeoutMS=30000'
                                    + '&socketTimeoutMS=None'
                                    + '&connect=false'
                                    + '&maxPoolsize=1')
        else:
            print("Connecting to Mongo locally.")
            client = pm.MongoClient()
