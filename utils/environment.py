import os

from dotenv import load_dotenv


class Environment:
    load_dotenv()

    DATABASE_URL = os.getenv("DATABASE_URL") or ""
