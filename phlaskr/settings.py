import os
from local_settings import LocalConfig

class BaseConfig(LocalConfig):

    DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    COOKIE_TTL = 100060
    DEBUG = True


class ProductionConfig(BaseConfig):
    DATABASE_URI = os.environ.get('DATABASE_URL')

    DEBUG = False

class TestConfig(BaseConfig):
    DATABASE_URI = 'sqlite:///testing.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SECRET_KEY = 'TESTING'

class DevConfig(BaseConfig):
    pass


configs = dict(
    production=ProductionConfig,
    dev=DevConfig,
    test=TestConfig
)

