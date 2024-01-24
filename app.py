from flask import Flask
from .apartments.models import Base
from .config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from .apartments.routes import apartments_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
Base.metadata.create_all(bind=db.engine)

app.register_blueprint(apartments_bp)

if __name__ == '__main__':
    app.run(debug=True)
