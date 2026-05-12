# pyrefly: ignore [missing-import]
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()

def _init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        print("Bases de datos creadas")
        db.create_all()
        
        
