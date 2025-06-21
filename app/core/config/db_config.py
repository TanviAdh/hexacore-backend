
from dotenv import load_dotenv
import os
from pathlib import Path
import sys

def load_env_config():
# load enviornment variables from .env file
    Environment = os.getenv("ENV", "dev")
    print(f"Environment: {Environment}")
    ENV_FILES={
    "dev": "dev.env",
    "prod": "prod.env"
    }
    # print(f"ENV: {Enviornment}")
    env_file = ENV_FILES.get(Environment)
    # print(f"env_file: {env_file}") 
    # print(f"Path(env_file): {Path(__file__).resolve().parents[3]/env_file}")
    # print(f"path(env_file): {Path(env_file)}")

    # load the appropriate .env file
    if Environment not in ENV_FILES:
        print ("Environment not found")
        sys.exit(1)
    else:
        load_dotenv(dotenv_path=Path(__file__).resolve().parents[3]/env_file)
    # Database configuration
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_USER = os.getenv("DB_USER")

    db_config = {
        "DB_HOST": os.getenv("DB_HOST"),
        "DB_PORT": os.getenv("DB_PORT"),
        "DB_NAME": os.getenv("DB_NAME"),
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD")
    }

    print("Loaded DB Configuration:")
    for key, value in db_config.items():
        print(f"{key}: {value}")

    return db_config 