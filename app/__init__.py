from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'some_secret'
db = SQLAlchemy(app)


#Blueprints
from app.users.views import users
app.register_blueprint(users, url_prefix='/users')