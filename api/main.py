from flask import Flask
from flasgger import Swagger
from api.routes import register_routes
from api.config import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(config)

db = SQLAlchemy(app)
swagger = Swagger(app)
register_routes(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    paises = db.Column(db.String(20), unique=True, nullable=False)
    quantidade = db.Column(db.Double, nullable=False)
    valor = db.Column(db.Double, nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Banco de dados criado!")

    app.run(debug=True)
    