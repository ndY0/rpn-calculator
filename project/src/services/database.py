from flask import g
from src.services.redis_connector import get_connection

def get_database(db_name):
    match db_name:
        case 'redis':
            if db_name not in g:
                g.redis = get_connection()
            return g.redis
        case _:
            raise Exception('unknown database: {db_name}'.format(db_name=db_name))