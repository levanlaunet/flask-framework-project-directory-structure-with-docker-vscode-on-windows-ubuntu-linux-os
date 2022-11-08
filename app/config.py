# import os

# class Config(object):
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     SECRET_KEY = 'SECRET_KEY'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# class ProductionConfig(Config):
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# class DevelopmentConfig(Config):
#     ENV="development"
#     DEVELOPMENT=True
#     DEBUG=True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')