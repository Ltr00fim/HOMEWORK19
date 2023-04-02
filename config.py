class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PWD_HASH_SALT = b'2423r3ef3r23232edasfdsfwdswdw2e23'
    PWD_HASH_ITERATIONS = 100_000
    JWT_SECRET = "SECRET"
    JWT_ALGORITHM = "HS256"
