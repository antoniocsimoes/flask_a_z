import os, random, string

class Config(object):
    CSRF_ENABLE = True # modelo de segurança - token
    SECRET = '75ccceca27f33edeb8b8a86432ce9819e1fde1515d19f723d5eee93ddce8cbf9'
    # utilizada para gerar tokens
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates') # une caminhos e diretórios
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class DevelopmentConfig(Config): #herança
    TESTING =  True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' %(IP_HOST, PORT_HOST) # http://localhost:8000
    SQLALCHEMY_DATABASE_URI = 'sqlite:///curso_flask.db'

app_config = {
    'development':DevelopmentConfig(),
    'testing': None,
    'production': None
}

app_active = os.getenv('FLASK_ENV')

if app_config is None:
    app_config = 'development'
