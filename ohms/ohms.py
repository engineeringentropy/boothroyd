from flask import Flask 
from ohms.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from ohms.models.database.base import db
    from ohms.models.database.base import migrate
    db.init_app(app)
    migrate.init_app(app, db)

    return app