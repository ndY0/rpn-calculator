from redis import Redis
from flask import current_app




def get_connection():
    return Redis(host=current_app.config['REDIS_HOST'], port=current_app.config['REDIS_PORT'], db=current_app.config['REDIS_DB'])
