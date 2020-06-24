from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from model import User

from config import app_config, app_active

config = app_config[app_active]

def create_app(config_name):
    # __name__ -> é a própria aplicação flask
    app = Flask(__name__, template_folder='templates') 
    
    app.secret_key = config.SECRET
    app.config.from_object(app_config[app_active])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)
    db.init_app(app)

    # @ é uma anotação
    @app.route('/')
    def index():
        result = User.query.first()
        print(result.username)
        print(type(result))       
       
        return 'Hello world!'

    return app