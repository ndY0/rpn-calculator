from os import environ 

REDIS_HOST = environ.get('REDIS_HOST')
REDIS_PORT = environ.get('REDIS_PORT')
REDIS_DB = environ.get('REDIS_DB')
DB_IN_USE = environ.get('DB_IN_USE')