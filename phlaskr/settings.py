import os
from local_settings import LocalConfig

class BaseConfig(LocalConfig):

    DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = 'testing'
    COOKIE_TTL = 100060
    DEBUG = True


class ProductionConfig(BaseConfig):
    DATABASE_URI = os.environ.get('DATABASE_URL')

    DEBUG = False

class TestConfig(BaseConfig):
    DATABASE_URI = 'sqlite:///testing.db'

class DevConfig(BaseConfig):
    pass


configs = dict(
    production=ProductionConfig,
    dev=DevConfig,
    test=TestConfig
)

