from flask import Flask
from os import path
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

#initializing my sqlalchemy database
db = SQLAlchemy()
login_manager = LoginManager()
DB_NAME = 'database.db'

#defining a function to create the app and configure the db
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "UIIUAHERD6829i9uu9vds0u9.dkuknenu.,ruureuhoe8YWNUIWID"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    db.init_app(app)
    
    #importing blueprints to register them
    from .views import views
    from .auth import auth
    from .models import User
    
    #registering my blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    
    create_database(app)
    
    login_manager.login_view="auth.login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    db.create_all(app = app)
    print ("created Dabase")