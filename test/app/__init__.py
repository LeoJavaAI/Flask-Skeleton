from flask import Flask


#http://flask.pocoo.org/docs/0.10/patterns/appfactories/
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app.users.models import db
    db.init_app(app)

    
    
    
    
    
    
    
    
    
    #Blueprints
    from app.customers.views import customers
    app.register_blueprint(customers, url_prefix='/customers', template_folder='templates')
    from app.customers.views import customers
    app.register_blueprint(customers, url_prefix='/customers', template_folder='templates')
    from app.customers.views import customers
    app.register_blueprint(customers, url_prefix='/customers', template_folder='templates')
    from app.customers.views import customers
    app.register_blueprint(customers, url_prefix='/customers', template_folder='templates')
    from app.customers.views import customers
    app.register_blueprint(customers, url_prefix='/customers', template_folder='templates')
    from app.customers.views import customers
    app.register_blueprint(customers, url_prefix='/customers', template_folder='templates')
    from app.customers.views import customers
    app.register_blueprint(customers, url_prefix='/customers', template_folder='templates')
    from app.customers.views import customers
    app.register_blueprint(customers, url_prefix='/customers'), template_folder='templates'
    from app.customers.views import customers
    app.register_blueprint(customers, url_prefix='/customers')
    from app.users.views import users
    app.register_blueprint(users, url_prefix='/users')

    return app



