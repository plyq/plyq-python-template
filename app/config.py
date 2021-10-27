import os


class Config(object):
    # Flask.
    DEBUG = True
    LOGGING_PATH = os.getenv("LOGGING_PATH")
    FLASK_ENV = os.getenv("FLASK_ENV", "DEBUG")
    # Telegram.
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


class ProductionConfig(Config):
    DEBUG = False


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {"PROD": ProductionConfig, "DEBUG": DebugConfig}
