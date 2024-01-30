import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID",29202444 ))

    API_HASH = os.environ.get("API_HASH", "1ed7adecc635e51724dfa7300d9fb328")
