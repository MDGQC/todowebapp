from flask import Flask

from .config import app_config
from .models import db, bcrypt

from .views.UserView import user_api as user_blueprint

def create_app(env_name):

    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')

    bcrypt.init_app(app)
    db.init_app(app)

    @app.route('/index', methods=['GET'])
    def index():
        return 'Hello'

    @app.route('/', methods=['GET'])
    def todowebapp_version():
        return 'Welcome in Todo Web App. ver 0.1'

    return app