#DATABASE SETTINGS
db_username = 'postgres'
db_password = ''
db_name = 'users'
db_hostname = 'localhost'

DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = True
SECRET_KEY = ""
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=db_username,
                                                                                        DB_PASS=db_password,
                                                                                        DB_ADDR=db_hostname,
                                                                                        DB_NAME=db_name)
