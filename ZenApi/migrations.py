from pymongo import MongoClient
import sys, getopt

def migrate(config):
   client = MongoClient(config.MONGODB_HOST, config.MONGODB_PORT)
   client.drop_database(config.MONGODB_DB)
   db = client[config.MONGODB_DB]
   collection_names = ['users', 'currencies', 'accounts', 'transfers', 'conversions']
   for collection_name in collection_names:
      collection = db[collection_name]
      collection.insert_one({})
      collection.delete_many({})

def run(argv):
   try:
      opts, args = getopt.getopt(argv,"he:")
   except getopt.GetoptError:
      print('test.py -e <environment>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('migrations.py -e <environment>')
         sys.exit()
      elif opt == "-e":
         if arg == 'development':
            print('development')
            from config import Development as Config
            config = Config()
            migrate(config)
         elif arg == 'production':
            print('production')
            from config import Production as Config
            config = Config()
            migrate(config)
if __name__ == "__main__":
   run(sys.argv[1:])