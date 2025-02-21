import os
from dotenv import load_dotenv


COINMARKET_API = "ab30df55-e360-48c4-ac66-86339c8439cf"
load_dotenv()


#COINMARKET_API = os.getenv("COINMARKET_API")

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DBNAME = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")