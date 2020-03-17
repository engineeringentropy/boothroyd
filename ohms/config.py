class Config(object):
    """Base config, in-memory sqlite database"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DB_SERVER = '192.168.1.56'

    # @property
    # def DATABASE_URI(self):         # Note: all caps
    #     return 'mysql://user@{}/foo'.format(self.DB_SERVER)

# class ProductionConfig(Config):
#     """Uses production database server."""
#     DB_SERVER = '192.168.19.32'

# class DevelopmentConfig(Config):
#     DB_SERVER = 'localhost'
#     DEBUG = True

# class TestingConfig(Config):
#     DB_SERVER = 'localhost'
#     DEBUG = True
#     DATABASE_URI = 'sqlite:///:memory:'