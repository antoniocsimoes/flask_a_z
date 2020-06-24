import sys
from app import create_app
from config import app_config, app_active

config = app_config[app_active]
config.APP = create_app(app_active)

if __name__ == '__main__':
    # só rode o que está aqui dentro se o run for rodado de um terminal
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
    reload(sys) # deu problema, dá um refresh na aplicação