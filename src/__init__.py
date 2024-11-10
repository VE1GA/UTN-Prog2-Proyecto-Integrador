from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db : SQLAlchemy = SQLAlchemy()
migrate : Migrate = Migrate()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(obj=Config)

    db.init_app(app=app)

    from .routes import productos_bp
    

    app.register_blueprint(blueprint=productos_bp)

    return app