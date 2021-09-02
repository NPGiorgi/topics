from starlette.config import Config

config = Config("./.env")

DEBUG = config("DEBUG", cast=bool, default=False)
DB_CONNECTION_URL = config("DB_CONNECTION_URL", cast=str)
