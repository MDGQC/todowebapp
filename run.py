from src.app import create_app

FLASK_ENV = 'development'

if __name__ == '__main__':
    env_name = FLASK_ENV
    app = create_app(env_name)

    app.run()