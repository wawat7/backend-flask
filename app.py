from flask import Flask
from routes.v1 import register_routes
from flask_restx import Api
from configs.environment_config import get_environment_variables
from configs.database_config import init_database

def create_app():
    
    env = get_environment_variables()
    database = init_database(env)
    database.connect()
    
    app = Flask(__name__)
    api = Api(app)

    register_routes(api, database)

    return app