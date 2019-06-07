from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import sys, getopt

def create_user(elements):
   client = MongoClient(elements['config'].MONGODB_HOST, elements['config'].MONGODB_PORT)
   db = client[elements['config'].MONGODB_DB]
   collection = db['users']
   collection.insert_one({'email': elements['email'], 'password': elements['password']})
   print('Usuario creado con exito!')

def run(argv):
   try:
      opts, args = getopt.getopt(argv,"he:m:p:")
   except getopt.GetoptError:
      print('test.py -e <environment>')
      sys.exit(2)
   elements = {'config': None, 'email': '', 'password': ''}
   for opt, arg in opts:
      if opt == '-h':
         print('migrations.py -e <environment> -m <email> -p <password>')
         sys.exit()
      elif opt == "-e":
         if arg == 'development':
            from config import Development as Config
            elements['config'] = Config()
         elif arg == 'production':
            from config import Production as Config
            elements['config'] = Config()
      elif opt == "-m":
         elements['email'] = arg
      elif opt == "-p":
         elements['password'] = generate_password_hash(arg)
   create_user(elements)
if __name__ == "__main__":
   run(sys.argv[1:])