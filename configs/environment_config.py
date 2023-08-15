from os import getenv
from dotenv import load_dotenv

load_dotenv()

def get_environment_variables():
    return {
        "API_VERSION": getenv("API_VERSION"),
        "APP_NAME": getenv("APP_NAME"),
        "DATABASE_USED": getenv("DATABASE_USED"),
        "DATABASE_HOSTNAME": getenv("DATABASE_HOSTNAME"),
        "DATABASE_NAME": getenv("DATABASE_NAME"),
        "DATABASE_PORT": getenv("DATABASE_PORT"),
        "DATABASE_USERNAME": getenv("DATABASE_USERNAME"),
        "DATABASE_PASSWORD": getenv("DATABASE_PASSWORD"),
        "MONGO_HOST": getenv("MONGO_HOST"),
        "MONGO_DB": getenv("MONGO_DB"),
        "MONGO_USERNAME": getenv("MONGO_USERNAME"),
        "MONGO_PASSWORD": getenv("MONGO_PASSWORD"),
        "MONGO_PORT": getenv("MONGO_PORT"),
        "DEBUG_MODE": getenv("DEBUG_MODE"),
    }