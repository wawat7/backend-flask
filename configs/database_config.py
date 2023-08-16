from queries.mongo import MongoDB
from queries.sql import SqlDB


def init_mongo(env):
    return MongoDB(**{
        "host": env['MONGO_HOST'],
        "port": int(env['MONGO_PORT']),
        "database": env['MONGO_DB'],
        "username": env['MONGO_USERNAME'],
        "password": env['MONGO_PASSWORD']
    })
    
def init_sql(env):
    return SqlDB(**{
        "host": env['DATABASE_HOSTNAME'],
        "port": int(env['DATABASE_PORT']),
        "database": env['DATABASE_NAME'],
        "username": env['DATABASE_USERNAME'],
        "password": env['DATABASE_PASSWORD']
    })
    
    
def init_database(env):
    if env['DATABASE_USED'] == 'mongo':
        return init_mongo(env)
    else:
        return init_sql(env)