password='password'

SQLALCHEMY_DATABASE_URI='postgresql://username:{}@localhost:5432/databasename'.format(password)
DEBUG = True
SECRET_KEY = 'development key'
