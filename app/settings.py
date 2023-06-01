import os

import dotenv

dotenv.load_dotenv()

DB_URL = os.getenv("DB_URL")
APP_PORT = int(os.getenv("APP_PORT"))
